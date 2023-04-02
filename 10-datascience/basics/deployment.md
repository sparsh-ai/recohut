# Model Deployment

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