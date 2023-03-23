# Data Science

Data science is used in a variety of ways. Some data scientists focus on the analytics side of things, pulling out hidden patterns and insights from data, then communicating these results with visualizations and statistics. Others work on creating predictive models in order to predict future events, such as predicting whether someone will put solar panels on their house. Yet others work on models for classification; for example, classifying the make and model of a car in an image. One thing ties all applications of data science together: the data. Anywhere you have enough data, you can use data science to accomplish things that seem like magic to the casual observer.

## Use Cases

Some of the many uses of machine learning across industries:

![smls_0101](https://user-images.githubusercontent.com/62965911/223616499-f68e16e9-56ff-4cb6-8d79-3580ee6d33a1.png)

## The data science origin story

There's a saying in the data science community that's been around for a while, and it goes: "*A data scientist is better than any computer scientist at statistics, and better than any statistician at computer programming*." This encapsulates the general skills of most data scientists, as well as the history of the field.

Data science combines computer programming with statistics, and some even call data science applied statistics. Conversely, some statisticians think data science is *only* statistics. So, while we might say data science dates back to the roots of statistics in the 19th century, the roots of modern data science actually begin around the year 2000. At this time, the internet was beginning to bloom, and with it, the advent of big data. The amount of data generated from the web resulted in the new field of data science being born.

A brief timeline of key historical data science events is as follows:

- **1962**: John Tukey writes *The Future of Data Analysis*, where he envisions a new field for learning insights from data
- **1977**: Tukey publishes the book *Exploratory Data Analysis*, which is a key part of data science today
- **1991**: Guido Van Rossum publishes the Python programming language online for the first time, which goes on to become the top data science language used at the time of writing
- **1993**: The R programming language is publicly released, which goes on to become the second most-used data science general-purpose language
- **1996**: The International Federation of Classification Societies holds a conference titled "*Data Science, Classification and Related Methods*" – possibly the first time "data science" was used to refer to something similar to modern data science
- **1997**: Jeff Wu proposes renaming statistics "data science" in an inauguration lecture at the University of Michigan
- **2001**: William Cleveland publishes a paper describing a new field, "data science," which expands on data analysis
- **2008**: Jeff Hammerbacher and DJ Patil use the term "data scientist" in job postings after trying to come up with a good job title for their work
- **2010**: Kaggle.com launches as an online data science community and data science competition website
- **2010s**: Universities begin offering masters and bachelor's degrees in data science; data science job postings explode to new heights year after year; big breakthroughs are made in deep learning; the number of data science software libraries and publications burgeons.
- **2012**: Harvard Business Review publishes the notorious article entitled *Data Scientist: The Sexiest Job of the 21st Century*, which adds fuel to the data science fire.
- **2015**: DJ Patil becomes the chief data scientist of the US for two years.
- **2015**: TensorFlow (a deep learning and machine learning library) is released.
- **2018**: Google releases cloud AutoML, democratizing a new automatic technique for machine learning and data science.
- **2020**: Amazon SageMaker Studio is released, which is a cloud tool for building, training, deploying, and analyzing machine learning models.

## Frameworks

### **CRISP-DM**

**CRISP-DM** stands for **Cross-Industry Standard Process for Data Mining** and has been around since the late 1990s. It's a six-step process, illustrated in the diagram below.

![content-concepts-raw-data-science-untitled](https://user-images.githubusercontent.com/62965911/219950480-67e6d155-de43-4c10-9c19-75d390376bc5.png)

### **TDSP**

**TDSP**, or the **Team Data Science Process**, was developed by Microsoft and launched in 2016. It's obviously much more modern than CRISP-DM, and so is almost certainly a better choice for running a data science project today.

The five steps of the process are similar to CRISP-DM, as shown in the figure below.

![content-concepts-raw-data-science-untitled-1](https://user-images.githubusercontent.com/62965911/219950476-16e44757-2da1-469b-bf22-8fac13b58ed2.png)

A reproduction of the TDSP process flow diagram.

Although the life cycle graphic looks quite different,  TDSP’s project lifecycle is like CRISP-DM and includes five iterative stages:

1. **Business Understanding:** define objectives and identify data sources
2. **Data Acquisition and Understanding:** ingest data and determine if it can answer the presenting question (effectively combines *Data Understanding* and *Data Cleaning* from CRISP-DM)
3. **Modeling:** feature engineering and model training (combines *Modeling* and *Evaluation*)
4. **Deployment:** deploy into a production environment
5. **Customer Acceptance:** customer validation if the system meets business needs (a phase not explicitly covered by CRISP-DM)

## Model Deployment

### Prototype vs. Production

If you are working on any proof-of-concept or performing [user acceptance testing (UAT)](https://www.functionize.com/blog/user-acceptance-testing/), you can use the prototype pipeline (1st column).

### Step 1: Model

Scikit, Tensorflow, and Pytorch are good frameworks for model building. [Teachable Machine](https://teachablemachine.withgoogle.com/) is good for quick and easy prototyping (applicable for limited use cases like pose estimation)

### Step 2: App

**Prototype:** I use [Gradio](https://www.gradio.app/) a lot for serving my model. Gradio wraps my model as an API in less than 5 mins with minimal coding. [Streamlit](https://www.streamlit.io/) is my favorite. It takes 20-30 mins for wrapping and gives lots of functionality and flexibility. [H2O Wave](https://h2oai.github.io/wave/) is making some waves in recent months.

**Production:** FastAPI is actually fast for serving models as an API. FlaskAPI comes next. For the dashboard, my favorite is Plotly Dash. It is very powerful and flexible. Tableau is the industry favorite. PowerBI and Google Data Studio are very user friendly and powerful.

### Step 3: Container

**Prototype:** For some use cases (privacy reasons), I use the local machine. Otherwise, I prefer to use Colab as my container.

**Production:** Docker is my favorite container for shipping out ML models.

### Step 4: Hosting (on cloud)

**Prototype:** Again colab for privacy-free use cases. It can host for half a day. Heroku is my favorite if multi-day hosting is required for prototype testing.

**Production:** EBS is nice. I use it hosting my APIs. Kubernetes is good for the orchestration of these APIs.

### Step 5: Hosting (on edge)

**Prototype:** ml5.js allows me to directly serve ML models on the browser.

**Production:** TF.js and TFLite are my favorites for serving on the browser and on mobile respectively.

## Mathematics

## Labs

1. [Probability Theory and the Sample Space Analysis](https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2022-01-21-probability.ipynb)
2. [Cool Stats Visuals](https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2022-01-21-stat-visuals.ipynb)
3. [Statistics and Linear Algebra for Data Science](https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2022-01-22-statistics.ipynb)

## Coding Notebooks

1. https://nbviewer.org/github/adipola/ml-with-apache-spark/tree/main/notebooks/
