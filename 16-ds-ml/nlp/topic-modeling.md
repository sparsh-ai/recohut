# Topic Modeling

![content-concepts-raw-nlp-topic-modeling-img](https://user-images.githubusercontent.com/62965911/216823108-f57ec710-01e0-4f24-9696-d9c2dcb32cc8.png)

## **Introduction**

- **Definition:** Topic modeling is an unsupervised machine learning technique that’s capable of scanning a set of documents, detecting word and phrase patterns within them, and automatically clustering word groups and similar expressions that best characterize a set of documents.
- **Applications:** Identify emerging themes and topics
- **Scope:** No scope decided yet
- **Tools:** Gensim

## Models

### LSA

The core idea is to take a matrix of what we have — documents and terms — and decompose it into a separate document-topic matrix and a topic-term matrix.

### Process flow

Step 1: Collect Text Data

Fetch from database, scrap from the internet or use public datasets. Setup the database connection and fetch the data into python environment.

Step 2: Data Preparation

Explore the data, validate it and create preprocessing strategy. Clean the data and make it ready for modeling.

Step 3: Model Building

Start the training process and track the progress and experiments. Validate the final set of models and select/assemble the final model.

Step 4: UAT Testing

Wrap the model inference engine in API for client testing

Step 5: Deployment

Deploy the model on cloud or edge as per the requirement

Step 6: Documentation

Prepare the documentation and transfer all assets to the client

## Use Cases

### Identify Themes and Emerging Issues in ServiceNow Incident Tickets

Extracted key phrases from the incident ticket descriptions and trained an LSA topic model on these phrases to identify emerging themes and incident topics. This enabled a proactive approach to manage and contain the issues and thus increasing CSAT. Check out [this](https://www.notion.so/ServiceNow-Advanced-Analytics-1D5F3-f35e7f17377544c8b11cdf624e5da800) notion.

### IT Support Ticket Management

In Helpdesk, almost 30–40% of incident tickets are not routed to the right team and the tickets keep roaming around and around and by the time it reaches the right team, the issue might have widespread and reached the top management inviting a lot of trouble. To solve this issue, we built a system with 6 deliverables: Key Phrase Analysis, Topic Modeling, Ticket Classification, Trend, Seasonality and Outlier Analysis, PowerBI Dashboard to visually represent the KPIs and dividing tickets into standard vs. non-standard template responses. Check out [this](https://www.notion.so/ESMCafe-IT-Support-Ticket-Management-69965830d39d486194f9a2f1222a81d8) notion.
