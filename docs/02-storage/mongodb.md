# MongoDB

```makefile
install:
	wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
	tar -xf mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
	export PATH=$PATH:/home/project/mongodb-database-tools-ubuntu1804-x86_64-100.3.1/bin

start_server:
	start_mongo

connect:
	mongo -u <username> -p <password> --authenticationDatabase admin local
	mongosh "mongodb+srv://cluster0.mongodb.net/myFirstDatabase" --apiVersion 1 --username admin

version:
	db.version()
	mongoimport --version
	mongoexport --version

list_databases:
	show dbs

create_database:
	use training

create_collection:
	db.createCollection("mycollection")

list_collections:
	show collections

insert_record:
	db.mycollection.insert({"color":"white","example":"milk"})

import_data:
	mongoimport -u <username> --authenticationDatabase admin --db catalog --collection <collection_name> --file <filename>

	mongoimport --uri "mongodb+srv://admin:@cluster0.mongodb.net/catalog?retryWrites=true&w=majority" --collection electronics --drop --file data/catalog.json

export_data:
	mongoexport -u <username> --authenticationDatabase admin --db=catalog --collection=<collection_name> --type=csv --fields=_id,type,model --out=<filename.csv>
```