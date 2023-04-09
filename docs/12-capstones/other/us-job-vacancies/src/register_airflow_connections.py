from create_cluster import (
    # Configuration parse function
    config_parse_file, config_get_dict,
    # AWS Credentials
    KEY, SECRET,
    # PostgreSQL Credentials
    DWH_DB, DWH_DB_USER, DWH_DB_PASSWORD,
    DWH_HOST, DWH_PORT,
)
from airflow import settings
from airflow.models import Connection


def main():
    config_parse_file()
    cfgs = config_get_dict()

    connections = [
        Connection(
            conn_id="pgsql", conn_type="postgres",
            host=cfgs['DWH_HOST'], port=cfgs['DWH_PORT'], schema=cfgs['DWH_DB'], login=cfgs['DWH_DB_USER'],
            password=cfgs['DWH_DB_PASSWORD'],
        ),
        Connection(
            conn_id="aws_credentials", conn_type="aws",
            login=cfgs['KEY'], password=cfgs['SECRET']
        ),
        Connection(
            conn_id="github_jobs", conn_type="http",
            schema="https", host="jobs.github.com",
        ),
        Connection(
            conn_id="landing_jobs", conn_type="http",
            schema="https", host="landing.jobs",
        ),
        Connection(
            conn_id="stackoverflow_jobs", conn_type="http",
            schema="https", host="stackoverflow.com",
        )
    ]
    session = settings.Session()

    for new_conn in connections:
        if not (session.query(Connection).filter(Connection.conn_id == new_conn.conn_id).first()):
            print(new_conn.debug_info())
            session.add(new_conn)
            session.commit()
        else:
            msg = '\n\tA connection with `conn_id`={conn_id} already exists\n'
            msg = msg.format(conn_id=new_conn.conn_id)
            print(msg)
            existent_connection = session.query(Connection).filter(Connection.conn_id == new_conn.conn_id).first()
            print(existent_connection.debug_info())

    print('\nConnections created!\n')


if __name__ == '__main__':
    main()