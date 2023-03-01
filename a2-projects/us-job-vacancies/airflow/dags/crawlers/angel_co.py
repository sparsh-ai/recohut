import math

from airflow.hooks.base_hook import BaseHook

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import configparser

import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

from crawlers.common import aws

from pyvirtualdisplay import Display


def selenium_create_driver(executable_path=r'/usr/local/bin/chromedriver', options=None, capabilities=None):
    if options is None:
        options = Options()

    return webdriver.Chrome(options=options, executable_path=executable_path, desired_capabilities=capabilities)


def lazy_get_element(driver, css_selector, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def accept_cookies(driver):
    driver.implicitly_wait(5)

    accept_cookies_button = lazy_get_element(driver, '.c-button.c-button--blue')
    accept_cookies_btn_is_interactable = accept_cookies_button.is_displayed() and accept_cookies_button.is_enabled()
    if accept_cookies_button is not None and accept_cookies_btn_is_interactable:
        accept_cookies_button.click()


def do_login(driver):
    login_button = lazy_get_element(driver, 'a.auth.login')
    if login_button is not None:
        login_button.click()
    else:
        print('Cant follow to the login page')
        return

    driver.implicitly_wait(1)

    email_input = lazy_get_element(driver, '#user_email')
    password_input = lazy_get_element(driver, '#user_password')

    if email_input is None or password_input is None:
        print('Cant follow to type the email/password')
        return
    
    angel_co_conn = BaseHook.get_connection('angel_co')

    email_input.send_keys(angel_co_conn.login)
    password_input.send_keys(angel_co_conn.password)

    login_form_button = lazy_get_element(driver, '.s-form input[type="submit"]')
    if login_form_button is None:
        print('Cant find the login form button? Cant follow with the script')
    login_form_button.click()


def clean_all_filters(driver, selector):
    """
    Had to go to a recursive approach to clean all filters as our element tree changes each time we delete
    a filter
    :param driver:
    :param selector:
    :return:
    """
    filters_buttons = driver.find_elements_by_css_selector(selector)

    if not filters_buttons:
        return

    filters_buttons[0].click()
    driver.implicitly_wait(1)

    if len(filters_buttons) > 1:
        clean_all_filters(driver, selector)


def mouseover_element(driver, selector):
    element = lazy_get_element(driver, selector)
    if not element:
        return False

    hover_action = ActionChains(driver).move_to_element(element)
    hover_action.perform()
    return True


def result_pages_count(driver):
    results_count = driver.find_element_by_css_selector('.job_listings.browse_filters .count-box .label-container')
    results_count_txt = results_count.get_attribute('innerText')
    total_results = int(
        results_count_txt.replace('startups', '')
            .replace(',', '')
            .replace('.', '')
            .strip()
    )
    results_per_page = 10
    return math.floor(total_results / results_per_page)


def scroll_down_all_pages(driver):
    startup_container = driver.find_element_by_css_selector('.find.g-module.startup-container')
    current_checksum = startup_container.get_attribute('data-checksum')
    last_pages_count = len(driver.find_elements_by_css_selector('.find.g-module.startup-container > div'))

    print('The current checksum is: ' + current_checksum)
    pages = result_pages_count(driver)
    for i in range(1, pages):
        print('page: {}/{}'.format(i, pages))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        should_outer_break = True
        for i in range(1, 60):
            time.sleep(1)
            new_pages_count = len(driver.find_elements_by_css_selector('.find.g-module.startup-container > div'))
            if new_pages_count > last_pages_count:
                should_outer_break = False
                break

        if should_outer_break:
            break


def save_all_startup_jobs(driver, output_directory):
    startups_divs = driver.find_elements_by_css_selector(
        # '#startups_content > .job_listings.browse_startups > ' +
        '.find.g-module.startup-container > div > .job_listings.browse_startups_table > ' +
        '.job_listings.browse_startups_table_row'
    )
    total_startups_divs = len(startups_divs)
    print('Total startups divs: {}'.format(total_startups_divs))
    startups_divs_it = 0
    aws_credentials = aws.get_credentials()
    for startup_div in startups_divs:
        startups_divs_it = startups_divs_it + 1
        startup_div_id = startup_div.get_attribute('data-id')
        html_content = startup_div.get_attribute('outerHTML')
        aws.create_file_on_s3_from_string(
            html_content, 
            '{}/{}.html'.format(output_directory, startup_div_id),
            aws_credentials,
            'text/html'
        )
        print('Saving startup div {}/{}'.format(startups_divs_it, total_startups_divs))


def main():
    display = Display(visible=0, size=(1440, 900))
    display.start()

    options = Options()
    # options.headless = True
    options.add_argument("window-size=1920,1080")
    options.add_argument("disable-gpu")
    options.add_argument("disable-extensions")
    options.add_argument("proxy-server='direct://'")
    options.add_argument("proxy-bypass-list=*")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_argument("disable-dev-shm-usage")

    driver = selenium_create_driver(options=options)
    driver.set_window_size(1440, 900)
    driver.maximize_window()

    driver.get('https://angel.co')

    driver.implicitly_wait(5)

    accept_cookies(driver)

    do_login(driver)
    
    driver.implicitly_wait(15)
    
    driver.get('https://angel.co/jobs')

    lazy_get_element(driver, '.remove-filter.delete')  # wait until the remove filter buttons appear
    # then, find all remove filter buttons

    clean_all_filters(driver, '.remove-filter.delete')

    driver.implicitly_wait(20)

    mouseover_element(driver, '.dropdown-filter[data-menu="compensation"]')

    driver.implicitly_wait(1)

    dropdown_menu_option = lazy_get_element(driver, '.filter-row[data-key="visa"]')
    dropdown_menu_option.click()

    print('Waiting for visa sponsor jobs')
    driver.implicitly_wait(30)
    print('waiting done. there are only visa sponsor jobs?')

    # after cleaning all filter's

    # Waiting for the startup div that holds the jobs listing
    lazy_get_element(
        driver,
        '#startups_content > .job_listings.browse_startups > .find.g-module.startup-container > div > '+
        '.job_listings.browse_startups_table[data-job-filter=\'{"visa":"true"}\']'
    )

    scroll_down_all_pages(driver)

    save_all_startup_jobs(driver, 'crawlers/angel_co')

    display.stop()


if __name__ == '__main__':
    main()
