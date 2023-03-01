# Travel Recommendation System

TravelBuddy is a startup working on building am AI-based recommendation system that will recommend travel products (e.g. hotels, destination places, restaurants) to its users. You are hired as an AI developer that will handle the end-to-end development and maintenance of this AI system.

Your goals and responsibilities include:

1. Communicate with Product owners to understand the business requirements for various use cases and develop AI models to fulfil those requirements.
2. Develop a GUI for the product owners to interact with the AI models in order to improve their understanding of the AI systems and perform regular user acceptance tests.
3. Develop an API that will be consumed by the front-end team to fetch product recommendations for the given inputs.
4. Create a documentation platform and document all the work for the product owners and stakeholders to keep themselves updated on all the latest developments.
5. Deploy the AI API, Dashboard GUI and Documentation platform on AWS.
6. Implement CI/CD capabilities in the deployment pipelines so that the user fronts - API, Dashboard and Documentation Platforms, keeps getting updated automatically with the new features.
7. Design the systems in an auto-scalable manner so that the increased workloads can be handled by the existing pipelines without changed any underlying design.
8. The overall monthly budget should not exceed a fixed amount and therefore, serverless systems and services should be used as much as possible.

There are multiple use cases, you need to work on them one by one:

1. Rule-based recommendation model to calculate a score for the given input product.
2. Rule-based recommendation model to identify the adjacent products in the product lines.
3. Data-based recommendation model to identify the similar products.
4. Data-based recommendation model to recommend the next-best product in the product lines.
5. Data-based product similarity model that will use product's metadata - title, description, images and videos - to identify similar products.
6. Data-based performance metrics on dashboard - Hit rate, Bounce rate, MRR and NDCG.
7. Data-based recommendation model to find the trending products on the internet and recommend similar products available in the product catalog.

## Dashboard

![dash1](https://user-images.githubusercontent.com/62965911/219868412-a72a5ec6-360e-45b6-b0f2-4381fb9a402f.png)

![dash2](https://user-images.githubusercontent.com/62965911/219868417-65680336-b604-437e-993d-4f796ec744a7.png)

## Solution

- AI based pre-trained and fine-tuned models are used for Text, Image and Video processing.
- Matrix factorization for similar product recommendations.
- LSTM for next-best product recommendations.
- FastAPI for API.
- Streamlit for dashboard.
- Docusaurus for documentation.
- Python 3.9 for all kind of development.
- AWS CodePipeline for CICD.
- AWS ECS, ECR, S3 and Lambda for Serverless design.
- Other AWS services as per requirements - e.g. AWS DMS for data pull and sync between storages.