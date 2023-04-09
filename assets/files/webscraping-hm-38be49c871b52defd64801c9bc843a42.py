# Imports
import os
import re
import logging
import requests
import pandas as pd
import numpy  as np
from datetime   import datetime
from bs4        import BeautifulSoup
from sqlalchemy import create_engine

# Functions
def get_showroom(url, headers):
    page = requests.get(url, headers=headers) # accessing url
    soup = BeautifulSoup(page.text, 'html.parser') # beautifulSoup object

    total_item = soup.find_all('h2', class_='load-more-heading')[0].get('data-total') # total items available
    page_number = np.round(int(total_item)/ 36) + 1 # rounded necessary page number 
    url_complete = url + '?page-size=' + str(int(page_number*36)) # new url -> now with all items in the same page
    url = url_complete # complete h&m url
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'} # user agent
    page = requests.get(url, headers=headers) # accessing url
    soup = BeautifulSoup(page.text, 'html.parser') # new BeautifulSoup Object
    products = soup.find('ul', class_='products-listing small') # finding products full list

    product_list = products.find_all('article', class_='hm-product-item') # getting each product
    product_id = [p.get('data-articlecode') for p in product_list] # product id
    product_type = [p.get('data-category') for p in product_list] # product_type
    data = pd.DataFrame([product_id, product_type]).T # building the Initial DataFrame
    data.columns = ['product_id', 'product_type']
    data['product_id'] = data['product_id'].astype(str) # adjustments
    data['style_id'] = data['product_id'].apply(lambda x: x[:-3])
    data['color_id'] = data['product_id'].apply(lambda x: x[-3:])
    df_scraped = data.copy()

    return df_scraped

def get_product_attributes(df_scraped):
    df_compositions = pd.DataFrame()
    # API Requests
    for i in range(len(df_scraped)):
        url = 'https://www2.hm.com/en_us/productpage.' + df_scraped.loc[i, 'product_id'] + '.html'
        logger.debug('Product: %s', url)
        page = requests.get(url, headers=headers)

        # Beautiful Object
        soup = BeautifulSoup(page.text, 'html.parser') 

        ############################################################# Extracting Color ####################################################
        id_color_list = soup.find_all('a', class_='filter-option miniature active') + soup.find_all('a', class_='filter-option miniature')

        color_name = [p.get('data-color') for p in id_color_list] # getting the color
        product_id = [p.get('data-articlecode') for p in id_color_list] # getting the ID - each color has a individual ID (last 3 digits)

        df_color = pd.DataFrame([product_id, color_name]).T
        df_color.columns = ['product_id', 'color_name']

        for j in range(len(df_color)):
            ####################################### API Requests #######################################
            url = 'https://www2.hm.com/en_us/productpage.' + df_color.loc[j, 'product_id'] + '.html'
            logger.debug('Color: %s', url)
            page = requests.get(url, headers=headers)    
            soup = BeautifulSoup(page.text, 'html.parser') # beautiful object
            
            ####################################### Product Name #######################################
            product_name = soup.find_all('hm-product-name', id='js-product-name')
            product_name = product_name[0].get_text().strip()
            
            product_price = soup.find_all('div', class_='price parbase')
            product_price = product_price[0].get_text().strip()

            ##################################################### Extracting Fit and Composition ###########################################
            product_composition_list = soup.find_all('div', class_='details-attributes-list-item') # attributes list
            product_composition = [list(filter(None, item.get_text().split('\n'))) for item in product_composition_list]
            
            if product_composition != []: # if not empty
                df_composition_ref = pd.DataFrame(product_composition).T # creating Dataframe from product_composition list
                df_composition_ref.columns = df_composition_ref.iloc[0, :] # sets the first row as columns
                df_composition = df_composition_ref[['Fit', 'Composition', 'Art. No.']] # selecting only necessary columns
                df_composition = df_composition[df_composition['Composition'].notnull()]
                df_composition = df_composition.iloc[1:].fillna(method='ffill') # dealing with NaN's

                # Replacing Shell
                df_composition['Composition'] = df_composition['Composition'].replace('Shell: ', '', regex=True)

                # Renaming columns
                df_composition = df_composition.rename(columns = {'Fit' : 'fit', 'Composition' : 'composition', 'Art. No.' : 'product_id'})

                # Adding product_name and product_price
                df_composition['product_name'] = product_name
                df_composition['product_price'] = product_price
                ##################################################### Merging ###############################################################
                # Color + Composition
                df_composition = pd.merge(df_composition, df_color, how='left', on='product_id')

                # Attributes
                df_compositions = pd.concat([df_compositions, df_composition], axis=0)
            
            else: # if empty
                None

    # Generate Style ID + Color ID
    df_compositions['style_id'] = df_compositions['product_id'].apply(lambda x: x[:-3]) # product_id = style_id + color_id
    df_compositions['color_id'] = df_compositions['product_id'].apply(lambda x: x[-3:])

    # scraping datetime
    df_compositions['scraping_datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')        

    # Merging
    df_raw = pd.merge(df_scraped[['product_type', 'style_id']], df_compositions, how='left', on='style_id')

    return df_raw

def data_cleaning(df_raw):
    df_raw.rename(columns = {'fit' : 'product_fit', 'color_name' : 'product_color', 'composition' : 'product_composition'}, inplace=True) 
    df_raw['product_color'] = df_raw['product_color'].apply(lambda x: x.replace(' ', '_').lower() if pd.notnull(x) else x)
    df_raw['product_fit'] = df_raw['product_fit'].apply(lambda x: x.replace(' ', '_').lower() if pd.notnull(x) else x)
    df_raw['product_name'] = df_raw['product_name'].apply(lambda x: x.replace(' ', '_').lower() if pd.notnull(x) else x)
    df_raw['product_price'] = df_raw['product_price'].apply(lambda x: x.replace('$', ' ') if pd.notnull(x) else x)
    df_raw['product_price'] = pd.to_numeric(df_raw['product_price'])
    df_raw['scraping_datetime'] = pd.to_datetime(df_raw['scraping_datetime'])

    df_raw = df_raw[~df_raw['product_composition'].str.contains('Pocket lining', na=False)] # removing all lines that contain Pocket lining
    df_raw = df_raw[~df_raw['product_composition'].str.contains('Lining', na=False)] # removing all lines that contain Lining
    df_raw = df_raw[~df_raw['product_composition'].str.contains('Pocket', na=False)].reset_index().drop(columns=['index']) # removing all lines that Pocket

    df_aux = df_raw['product_composition'].str.split(',', expand=True) # auxiliary column
    # Cotton
    df_aux['cotton'] = np.where(df_aux[0].str.contains('Cotton'), df_aux[0], np.nan) # puts the cotton values on 'cotton' column if df1' first column contains 'Cotton', else puts NaN's
    df_aux['cotton'] = np.where(df_aux[1].str.contains('Cotton'), df_aux[1], df_aux['cotton']) # there're some cotton values on the second column 

    #  Spandex
    df_aux['spandex'] = np.where(df_aux[1].str.contains('Spandex'), df_aux[1], np.nan) # puts the spandex values on 'spandex' column if df1' second column contains 'Spandex', else puts NaN's
    df_aux['spandex'] = np.where(df_aux[2].str.contains('Spandex'), df_aux[2], df_aux['spandex']) # there're some spandex values on the third column

    # Polyester
    df_aux['polyester'] = np.where(df_aux[1].str.contains('Polyester'), df_aux[1], np.nan) # puts the polyester values on 'polyester' column if df1' second column contains 'Polyester', else puts NaN's

    # Elastomultiester 
    df_aux['elastomultiester'] = np.where(df_aux[1].str.contains('Elastomultiester'), df_aux[1], np.nan) # puts the elastomultiester values on 'elastomultiester' column if df1' second column contains 'Elastomultiester', else puts NaN's

    # Lyocell
    df_aux['lyocell'] = np.where(df_aux[0].str.contains('Lyocell'), df_aux[0], np.nan) # puts the lyocell values on 'lyocell' column if df1' first column contains 'Lyocell', else puts NaN's
    df_aux['lyocell'] = np.where(df_aux[1].str.contains('Lyocell'), df_aux[1], df_aux['lyocell']) # there're some lyocell values on the second column

    # Rayon
    df_aux['rayon'] = np.where(df_aux[0].str.contains('Rayon'), df_aux[0], np.nan) # puts the rayon values on 'rayon' column if df1' first column contains 'rayon', else puts NaN's
    df_aux['rayon'] = np.where(df_aux[2].str.contains('Rayon'), df_aux[2], df_aux['rayon']) # there're some spandex values on the third column

    # Cleaning
    df_aux = df_aux.drop(columns=[0, 1, 2]) # dropping auxiliary columns
    df_raw = pd.concat([df_raw, df_aux], axis=1) # concat df_aux and df_raw
    df_raw = df_raw.drop(columns=['product_composition']) # dropping product_composition column

    # Extracting only the actual numbers
    df_raw['cotton'] = df_raw['cotton'].apply(lambda x: int(re.search('\d+', x).group(0)) / 100 if pd.notnull(x) else 0) 
    df_raw['spandex'] = df_raw['spandex'].apply(lambda x: int(re.search('\d+', x).group(0)) / 100 if pd.notnull(x) else 0)
    df_raw['polyester'] = df_raw['polyester'].apply(lambda x: int(re.search('\d+', x).group(0)) / 100 if pd.notnull(x) else 0) 
    df_raw['elastomultiester'] = df_raw['elastomultiester'].apply(lambda x: int(re.search('\d+', x).group(0)) / 100 if pd.notnull(x) else 0) 
    df_raw['lyocell'] = df_raw['lyocell'].apply(lambda x: int(re.search('\d+', x).group(0)) / 100 if pd.notnull(x) else 0) 
    df_raw['rayon'] = df_raw['rayon'].apply(lambda x: int(re.search('\d+', x).group(0)) / 100 if pd.notnull(x) else 0) 

    df = df_raw.drop_duplicates().copy() # dropping duplicates

    df = df[['product_id', 'style_id', 'color_id', 'product_name', 'product_type', 
            'product_fit', 'product_color',  'cotton', 'spandex', 'polyester', 
            'elastomultiester', 'lyocell', 'rayon', 'product_price', 'scraping_datetime']] # rearranging columns

    return df

def data_insert(df):
    df_insert = df.copy()
    conn = create_engine('postgresql://brunodifranco:ExoCs9IRXJ6u@ep-soft-disk-362766.us-east-2.aws.neon.tech:5432/neondb', echo=False) # connection
    df_insert.to_sql('hm', con=conn, if_exists='append', index=False) # inserting data to table 
    return None

if __name__ == "__main__":
    # Log Files
    path = 'C:/Users/bruno/OneDrive/Documentos/repos/python-ds-ao-dev/star-jeans-etl/'
    if not os.path.exists(path + 'Logs'):
        os.makedirs(path + 'Logs')

    logging.basicConfig(
        filename= path + 'Logs/webscraping-hm.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')   

    logger = logging.getLogger('star-jeans-etl')

    # Parameters
    url = 'https://www2.hm.com/en_us/men/products/jeans.html'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'} # user agent
    
    # Extraction    
    df_scraped = get_showroom(url, headers) # Job 01
    logger.info('data showroom extraction done')

    df_raw = get_product_attributes(df_scraped) # Job 02
    logger.info('data product attributes extraction done')
    
    # Transformation
    df = data_cleaning(df_raw) # Job 03
    logger.info('data cleaning done')
    
    # Load
    data_insert(df) # Job 04
    logger.info('data insert done')