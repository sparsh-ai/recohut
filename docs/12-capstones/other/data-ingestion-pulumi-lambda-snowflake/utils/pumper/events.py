import uuid
import time
from random import choice


# some variables to simulate random stuff
# random clients / orgs, to simulate a multi-tenant scenario
TIDs = [ str(uuid.uuid4()) for _ in range(5) ]
# random user agents
USER_AGENTs = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
    'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
]
# random languages
LANGUAGEs = [
    'it-IT',
    'en-US',
    'es-ES',
    'fr-FR',
    'fr-CA'
    'ta-IN',
    'zh-CN',
    'zu-ZA'
]
# random screen resolutions
SCREEN_RESs = [
    '1440x900',
    '1920×1080',
    '1366×768',
    '1536×864'
]
BASE_URL = "http://www.jacopotagliabue.it/?page={}"


def map_session_to_metadata(session_id: str, _array: list):
    return _array[hash(session_id) % len(_array)]


def create_base_properties(row: dict):
    new_cid = str(uuid.uuid5(uuid.NAMESPACE_DNS, row['session_id_hash']))
    # make sure the length is what SF expects
    assert len(new_cid) == 36
    
    return { 
        # we use the placeholder URL and use the actual hash as param
        "dl": BASE_URL.format(row['hashed_url']),
        # current epoch in millisec, so that every event is new at every run
        "tm": round(time.time() * 1000), 
        # random event id
        "z": str(uuid.uuid4()),
        "sr": map_session_to_metadata(session_id=row['session_id_hash'], _array=SCREEN_RESs),
        "sd": "30-bit",
        "ul": map_session_to_metadata(session_id=row['session_id_hash'], _array=LANGUAGEs),
        "ua": map_session_to_metadata(session_id=row['session_id_hash'], _array=USER_AGENTs),
        "de": "UTF-8",
        "tid": map_session_to_metadata(session_id=row['session_id_hash'], _array=TIDs),
        # use session id as the client id in the GA sense
        "cid": new_cid
        }


def create_product_properties(sku: str, properties: dict):
    return {
        "pr1id": sku,
        "pr1pr": properties['price_bucket'] if properties else '0.0',
        "pr1ca": properties['category_hash'] if properties else 'NOCAT'
    }


def create_pageview(row: dict):
    basic = create_base_properties(row)
    pageview = {
        "t": "pageview",
    }
    return  {**basic, **pageview}


def create_detail(row: dict, metadata: dict):
    basic = create_base_properties(row)
    product = create_product_properties(row['product_sku_hash'], metadata)
    detail = {
        "t": "event",
        "pa": "detail"
    }
    return  {**basic, **detail, **product}


def create_add(row: dict, metadata: dict):
    product = create_product_properties(row['product_sku_hash'], metadata)
    basic = create_base_properties(row)
    add = {
        "t": "event",
        "pa": "add"
    }
    return  {**basic, **add, **product}


def create_remove(row: dict, metadata: dict):
    product = create_product_properties(row['product_sku_hash'], metadata)
    basic = create_base_properties(row)
    remove = {
        "t": "event",
        "pa": "remove"
    }
    return  {**basic, **remove, **product}


def create_purchase(row: dict, metadata: dict):
    product = create_product_properties(row['product_sku_hash'], metadata)
    basic = create_base_properties(row)
    purchase = {
        "t": "event",
        "pa": "purchase",
        # transaction id: https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters#ti
        "ti": str(uuid.uuid4()),
        # revenue, here = to the product price
        "tr": float(product['pr1pr']) if product['pr1pr'] else 0.0
    }
    return  {**basic, **purchase, **product}