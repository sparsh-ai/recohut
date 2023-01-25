import awswrangler as wr
from datetime import datetime
import pandas as pd
from prefect import task, flow, get_run_logger
from prefect.blocks.system import String
from prefect.task_runners import SequentialTaskRunner
import requests
from typing import Any, Dict

import os
from prefect_slack import SlackWebhook
from prefect_slack.messages import send_incoming_webhook_message


@task
def extract_prices() -> Dict[str, Any]:
    url = (
        "https://min-api.cryptocompare.com/data/pricemulti?"
        "fsyms=BTC,ETH,REP,DASH&tsyms=USD"
    )
    response = requests.get(url)
    prices = response.json()
    logger = get_run_logger()
    logger.info("Received data: %s", prices)
    return prices


@task
def transform_prices(json_data: Dict[str, Any]) -> pd.DataFrame:
    df = pd.DataFrame(json_data)
    now = datetime.utcnow()
    logger = get_run_logger()
    logger.info("Adding a column TIME with current time: %s", now)
    df["TIME"] = now
    return df.reset_index(drop=True)


@task
def load_prices(df: pd.DataFrame) -> None:
    table_name = "crypto"
    wr.s3.to_parquet(
        df=df,
        path="s3://prefectdata/crypto/",
        dataset=True,
        mode="append",
        database="default",
        table=table_name,
    )
    logger = get_run_logger()
    logger.info("Table %s in Athena data lake successfully updated 🚀", table_name)


@flow(task_runner=SequentialTaskRunner())
def real_time_flow():
    # Real-time data pipeline
    raw_prices = extract_prices()
    transformed_data = transform_prices(raw_prices)
    load_prices(transformed_data)

    # Taking action in real-time
    thresh_value = float(String.load("price").value)
    curr_price = raw_prices.get("BTC").get("USD")
    logger = get_run_logger()
    if curr_price < thresh_value:
        message = f"ALERT: Price ({curr_price}) is below threshold ({thresh_value})!"
        logger.info(message)
        send_incoming_webhook_message(
            slack_webhook=SlackWebhook(os.environ["SLACK_WEBHOOK_URL"]),
            text=message,
        )
    else:
        logger.info("Current price (%d) is too high. Skipping alert", curr_price)

    # logger.info("🚀 Real-time streaming workflows made easy! 🎉️ 🥳 🚀")


if __name__ == "__main__":
    while True:
        real_time_flow()
