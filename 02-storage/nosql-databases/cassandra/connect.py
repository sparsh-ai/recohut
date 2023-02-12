import os
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from datetime import datetime
import pandas as pd
from datetime import datetime

from cassandra.cqlengine.management import sync_table
from cassandra.policies import TokenAwarePolicy
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import (
    Cluster,
    DCAwareRoundRobinPolicy
)
from cassandra.cqlengine.connection import (
    register_connection,
    set_default_connection
)

CASSANDRA_USERNAME='cassandra'
CASSANDRA_PASSWORD='cassandra'
CASSANDRA_HOST='127.0.0.1'
CASSANDRA_PORT=9042
session = None
cluster = None

auth_provider = PlainTextAuthProvider(username=CASSANDRA_USERNAME, password=CASSANDRA_PASSWORD)
cluster = Cluster([CASSANDRA_HOST],
load_balancing_policy=TokenAwarePolicy(DCAwareRoundRobinPolicy()),
port=CASSANDRA_PORT,
auth_provider=auth_provider,
executor_threads=2,
protocol_version=4,
)           

session = cluster.connect()
register_connection(str(session), session=session)
set_default_connection(str(session))
rows = session.execute('select * from demo.click_stream;')
df = pd.DataFrame(list(rows))
df.head()