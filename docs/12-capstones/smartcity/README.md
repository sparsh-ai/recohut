# Smartcity

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/12-capstones/smartcity)

```
├── [4.4K]  01-dataStream
│   ├── [ 205]  README.md
│   ├── [ 286]  agent.json
│   ├── [ 774]  efo_consumer.py
│   ├── [ 814]  producer.py
│   ├── [1.2K]  producer_agent_policy.json
│   └── [ 957]  smartcity_system_message.json
├── [ 15K]  02-firehose
│   ├── [ 591]  CreateLambdaKDFLookupAddressTransform.json
│   ├── [3.7K]  KDFCreateDeliveryStreamSmartCityBikes.json
│   ├── [1.2K]  KDFLookupAddressTransform.py
│   ├── [2.2K]  KDFSmartCityDeliveryStreamPolicy.json
│   ├── [ 538]  KDFSmartCityLambdaPolicy.json
│   ├── [1.2K]  README.md
│   ├── [1.4K]  SmartCityGlueTable.json
│   ├── [ 195]  TrustPolicyForFirehose.json
│   ├── [ 194]  TrustPolicyForLambda.json
│   ├── [1.4K]  loadDynamoDBStationAddresses.py
│   └── [1.6K]  stations_addresses.csv
├── [123K]  03-analytics
│   ├── [ 19K]  flink-app
│   │   ├── [7.3K]  pom.xml
│   │   └── [ 12K]  src
│   │       └── [ 12K]  main
│   │           ├── [ 11K]  java
│   │           │   └── [ 11K]  com
│   │           │       └── [ 11K]  swipebike
│   │           │           └── [ 11K]  flink
│   │           │               ├── [5.3K]  RentalCountJob.java
│   │           │               └── [5.4K]  SwipeBikeToFirehose.java
│   │           └── [ 463]  resources
│   │               └── [ 367]  application-properties.json
│   ├── [ 12K]  flink-cdk
│   │   ├── [1.6K]  README.md
│   │   ├── [ 358]  app.py
│   │   ├── [ 362]  cdk.json
│   │   ├── [ 200]  deploy_cmd.txt
│   │   ├── [1.6K]  kda_app
│   │   │   ├── [   0]  __init__.py
│   │   │   └── [1.5K]  kda_app_stack.py
│   │   ├── [6.0K]  main_cdk
│   │   │   ├── [   0]  __init__.py
│   │   │   └── [5.9K]  main_cdk_stack.py
│   │   ├── [ 173]  requirements.txt
│   │   ├── [1.0K]  setup.py
│   │   └── [ 437]  source.bat
│   ├── [ 78K]  producer-app
│   │   ├── [   1]  readme.md
│   │   └── [ 78K]  ride-producer
│   │       ├── [ 663]  build.gradle
│   │       ├── [ 54K]  gradle
│   │       │   └── [ 54K]  wrapper
│   │       │       ├── [ 54K]  gradle-wrapper.jar
│   │       │       └── [ 202]  gradle-wrapper.properties
│   │       ├── [5.2K]  gradlew
│   │       ├── [2.1K]  gradlew.bat
│   │       ├── [  36]  settings.gradle
│   │       └── [ 16K]  src
│   │           ├── [ 14K]  com
│   │           │   └── [ 14K]  swipebike
│   │           │       ├── [1.0K]  KDABikeProducer.java
│   │           │       ├── [2.3K]  StationServiceReader.java
│   │           │       └── [ 11K]  dto
│   │           │           ├── [  78]  Behavior.java
│   │           │           ├── [ 523]  Bike.java
│   │           │           ├── [2.4K]  BikeRide.java
│   │           │           ├── [4.0K]  InTransitDTO.java
│   │           │           └── [3.6K]  Station.java
│   │           └── [1.2K]  main
│   │               └── [1.1K]  resources
│   │                   ├── [ 329]  log4j.properties
│   │                   └── [ 636]  stations.csv
│   ├── [9.8K]  producer-cdk
│   │   ├── [1.7K]  README.md
│   │   ├── [ 210]  app.py
│   │   ├── [  43]  cdk-producer.code-workspace
│   │   ├── [ 362]  cdk.json
│   │   ├── [ 561]  deploy-cmd.text
│   │   ├── [4.0K]  producer_cdk
│   │   │   ├── [   0]  __init__.py
│   │   │   └── [3.9K]  producer_cdk_stack.py
│   │   ├── [  59]  requirements.txt
│   │   ├── [1.2K]  setup.py
│   │   ├── [ 437]  source.bat
│   │   ├── [ 684]  tests
│   │   │   ├── [   0]  __init__.py
│   │   │   └── [ 556]  unit
│   │   │       ├── [   0]  __init__.py
│   │   │       └── [ 428]  test_producer_cdk_stack.py
│   │   └── [ 165]  user_data
│   │       └── [  69]  user_data.sh
│   ├── [   6]  reade.me
│   └── [3.5K]  sql-app
│       └── [3.4K]  sql-app.sql
├── [6.9K]  04-datalake
│   ├── [ 394]  AWSGlueServiceRole-GlueSwipeBikeRawPolicy.json
│   ├── [ 643]  FHSwipeBikeDataLakePolicy.json
│   ├── [ 503]  bikeStations.csv
│   ├── [ 346]  eventbridge
│   │   └── [ 250]  sampleEvent.json
│   ├── [ 554]  fhCreateFile.json
│   ├── [2.5K]  glue
│   │   └── [2.4K]  curationScript.py
│   ├── [ 722]  kdgTemplate.json
│   └── [ 992]  sql
│       ├── [ 433]  relationilizedQuery.sql
│       ├── [ 226]  stationIncome.sql
│       └── [ 173]  stationIncomeCurated.sql
├── [1.0K]  LICENSE
├── [ 400]  README.md
├── [ 210]  app.py
├── [ 362]  cdk.json
├── [  59]  requirements.txt
├── [1.2K]  setup.py
├── [ 437]  source.bat
└── [ 684]  tests
    ├── [   0]  __init__.py
    └── [ 556]  unit
        ├── [   0]  __init__.py
        └── [ 428]  test_producer_cdk_stack.py

 154K used in 36 directories, 84 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/12-capstones/smartcity)