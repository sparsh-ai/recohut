import pyarrow as pa

vaccinations_parquet_schema = pa.schema(
    [
        ("administeredvaccinations", pa.int64()),
        ("api_call_ts_utc", pa.timestamp("ns", "UTC")),
        ("meta_lastupdate", pa.string()),
        ("vaccinated", pa.int64()),
        ("vaccination_astrazeneca", pa.int64()),
        ("vaccination_biontech", pa.int64()),
        ("vaccination_janssen", pa.int64()),
        ("vaccination_moderna", pa.int64()),
        ("vaccination_novavax", pa.int64()),
        ("vaccination_valneva", pa.int64()),
        ("vaccination_biontechbivalent", pa.int64()),
        ("vaccination_modernabivalent", pa.int64()),
        ("vaccination_biontechinfant", pa.int64()),
    ]
)
