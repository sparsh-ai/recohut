from pymysqlreplication import BinLogStreamReader
from pymysqlreplication import row_event
import configparser
import pymysqlreplication

# get the MySQL connection info
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
password = parser.get("mysql_config", "password")

mysql_settings = {
    "host": hostname,
    "port": int(port),
    "user": username,
    "passwd": password
}

b_stream = BinLogStreamReader(
    connection_settings = mysql_settings,
    server_id = 1159723530,
    only_events = [row_event.DeleteRowsEvent,
        row_event.WriteRowsEvent,
        row_event.UpdateRowsEvent]
)
print("bin log stream")

with open('logs.txt','w') as f:
    for event in b_stream:
        f.write(event.packet.dump()+'\n')


b_stream.close()