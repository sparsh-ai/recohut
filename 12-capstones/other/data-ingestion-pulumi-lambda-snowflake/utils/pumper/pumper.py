"""

    This simple script will use real-world e-commerce data coming from the Coveo dataset to send realistic
    events to the /collect endpoint that powers the ingestion pipeline at the heart of this repository.

    The dataset is freely available for research purposes at:

    https://github.com/coveooss/SIGIR-ecom-data-challenge

    Don't forget to star the repo if you use the dataset ;-)

    Of course, you could send to /collect your own Google Analytics-like events if you wish, or even totally
    random events: while nothing hinges on the specificity of the chosen data stream, we thought it was better for
    pedagogical reasons to actually use events coming from a real distribution.

"""


import time
import os
from datetime import datetime
from events import create_pageview, create_add, create_detail, create_purchase, create_remove
import csv
from typing import Union


async def post_all_events(collect_url: str, events: list):
    import aiohttp

    async with aiohttp.ClientSession() as session:
        for idx, event in enumerate(events):
            # print some debugging stuff
            if idx and idx % 500 == 0:
                print("Reached {} events!".format(idx))
            async with session.post(collect_url, json=event) as resp:
                await resp.read()

    return

def create_artificial_event(row: dict, product_metadata: dict) -> Union[dict, None]:
    event = None
    if row['event_type'] == 'pageview':
        event = create_pageview(row)
    elif row['event_type'] == 'event_product':
        if row['product_action'] == 'detail':
            event = create_detail(row, product_metadata)
        elif row['product_action'] == 'add':
            event = create_add(row, product_metadata)
        elif row['product_action'] == 'remove':
            event = create_remove(row, product_metadata)
        elif row['product_action'] == 'purchase':
            event = create_purchase(row, product_metadata)
        else:
            raise Exception("Product action not valid: {}".format(row['product_action']))
    else:
        raise Exception("Event type not valid: {}".format(row['event_type']))

    return event


def get_catalog_map(catalog_file: str, is_debug: bool=False) -> dict:
    catalog_map = dict()

    with open(catalog_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            catalog_map[row['product_sku_hash']] = row

    if is_debug:
        print("We have a total of {} skus".format(len(catalog_map)))

    return catalog_map


def prepare_events(dataset_file: str, catalog_map: dict, n_events: int):
    events = []
    with open(dataset_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader):
            # quit if limit has been reached
            if idx >= n_events:
                print("Reached {} events!".format(idx))
                break
            # print some debugging stuff
            if idx and idx % 5000 == 0:
                print("Reached {} events!".format(idx))
            # build event
            product_metadata = catalog_map.get(row['product_sku_hash'], None) if row['product_sku_hash'] else None
            event = create_artificial_event(row, product_metadata)
            # if the event is created, add it to the list
            if event:
                events.append(event)

    return events


def pumper_loop(dataset_file: str, catalog_map: dict, collect_url: str, n_events: int) -> bool:
    """

    Loop over the browsing dataset, join with catalog data and prepare the events.
    When events are ready, send the events to collect using asyncio

    """
    import asyncio

    events_to_send = prepare_events(dataset_file, catalog_map, n_events)
    # send events in async loop
    print("Sending {} events to /collect".format(len(events_to_send)))
    start_time = time.time()
    asyncio.run(post_all_events(collect_url, events_to_send))
    print("--- %s seconds ---" % (time.time() - start_time))

    return True


def pump_events(
    data_folder: str,
    collect_url: str,
    n_events: int
):
    """
        Main orchestrating function:

        loop over a dataset of real events, simulate Google Analytics-like payloads and send
        them to the ingestion endpoint
    """
    print("\n============> Start processing at {}\n".format(datetime.utcnow()))
    # first, get a map product id (SKU) -> metadata
    catalog_map = get_catalog_map(os.path.join(data_folder, 'sku_to_content.csv'), is_debug=True)
    # loop over browsing event and sends them
    pumper_loop(os.path.join(data_folder, 'browsing_train.csv'), catalog_map, collect_url, n_events)
    # all done, say goodbye
    print("\n============> All done at {}\n\nSee you, space cowboy\n".format(datetime.utcnow()))
    return


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

    # make sure we have the data folder variable set, otherwise fail
    # make sure we know where to send events
    assert os.environ['COLLECT_URL']

    pump_events(
        data_folder=os.environ.get('DATA_FOLDER', './dataset'),
        collect_url=os.environ['COLLECT_URL'],
        n_events=int(os.environ.get('N_EVENTS', 1000)),
    )
