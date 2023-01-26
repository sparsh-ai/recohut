from requests import Session
import pandas as pd
import json
import os


def main():
    base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    params = {"start": "1", "limit": "100", "convert": "USD"}

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": os.getenv('COIN_MARKETCAP_API_KEY'),
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(base_url, params=params)

    if response.status_code != 200:
        if response.status_code != 404:
            print("Error in request url.", response.status_code)
        else:
            print("There was a problem retrieving data: ", response.text)

    else:
        response_text = response.text
        response_json_object = json.loads(response_text)
        df = pd.DataFrame(response_json_object["data"])
        df.to_csv("test.csv")


if __name__ == "__main__":
    main()