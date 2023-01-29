# Building Recommender System from Scratch

## Overview

1. Front-end website built with Plotly Dash
2. Clickstream data collection using Divolte pipeline
3. Model building in python
4. Recommendation Serving

## Architecture

![RecoFront-Techstack](https://user-images.githubusercontent.com/62965911/215308906-b16c222f-b621-41c2-950b-4df276f50d15.png)

## How to Run
Note: Refer to video for in-depth understanding of the project
1. Install the python requirements
2. Go to sandbox subfolder and run docker compose to start the data collector pipeline
3. Go to recommender -> api subfolder and build+run docker to start the recommender microservice
4. Run the app1.py to start the front-end and enjoy!

PS: app1.py is the main app file of this project.

## Dashboard

```python
#@markdown **RecoFront**
!pip install dash dash-html-components dash-core-components dash_auth
!pip install dash-table jupyter-dash dash_daq dash_bootstrap_components visdcc
# !kill -9 $(lsof -t -i:8081)
!pip install -q colab-everything
from colab_everything import ColabCustom
ColabCustom("python3 app1.py", port=8051)
```

![K8X2lR](https://user-images.githubusercontent.com/62965911/215309109-b82f7b47-448b-4c35-9795-a5fcd7e88d1c.gif)

## How to restore backup in Cassandra

- Start the docker compose and attach the cassandra shell (regular step)
- Now copy the whole snapshot data into the newly created folder

![snap300421](https://user-images.githubusercontent.com/62965911/215308907-0c94001c-9415-4794-8881-8809af66d70b.png)

- Refresh the database - ```nodetool refresh demo click_stream```

## How to build docker

```
docker build -t model1.1 .
docker run -d --name reco-model-cb -p 8080:80 model1.1
docker stop reco-model-cb
docker rm reco-model-cb
```

## Project Structure

```
├── [6.1K]  README.md
├── [5.6K]  app1.py
├── [3.6K]  app2.py
├── [   0]  app3.py
├── [3.7K]  apps
│   ├── [1.2K]  app_auth.py
│   ├── [1.1K]  app_basic.py
│   └── [1.2K]  authapp.py
├── [ 40K]  assets
│   ├── [ 12K]  base-styles.css
│   ├── [2.4K]  fonts.css
│   ├── [9.0K]  my-logo-2.svg
│   ├── [ 16K]  spc-custom-styles.css
│   └── [ 137]  users.py
├── [ 18K]  base.py
├── [  59]  data-download.sh
├── [2.8K]  etc
│   ├── [2.6K]  commands.txt
│   └── [ 126]  requirements.txt
├── [ 12K]  notebooks
│   └── [ 12K]  Read\ data\ from\ cassandra.ipynb
├── [ 704]  recommender
│   ├── [ 160]  data
│   └── [ 416]  model1
├── [5.3K]  sandbox
│   ├── [2.2K]  _README.md
│   ├── [ 322]  click_stream_consumer.env
│   ├── [ 224]  consumer
│   ├── [  96]  djmojo
│   ├── [  96]  docker
│   └── [2.1K]  docker-compose.yml
└── [ 134]  temp.py

 1011K used in 12 directories, 24 files
```