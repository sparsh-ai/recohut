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

## Deep Learning

### What is Deep Learning?

![pg3_Image_3](https://user-images.githubusercontent.com/62965911/228470889-e20467b0-d506-473d-99eb-c6c7898b90ee.jpeg)

### The Rosenblatt Perceptron

The perceptron is an artificial neuron, that is, a model of a biological neuron.

![pg30_Image_6](https://user-images.githubusercontent.com/62965911/228531087-492b9509-3168-4bb5-a82a-9dbdcf25eddc.jpeg)

The neuron receives stimuli on the dendrites, and in cases of sufficient stimuli, the neuron fires (also known as getting activated or excited) and outputs stimulus on its axon, which is transmitted to other neurons that have synaptic connections to the excited neuron. Synaptic signals can be excitatory or inhibitory; that is, some signals can prevent a neuron from firing instead of causing it to fire.

A **perceptron** is a type of **artificial neuron**. It sums up the inputs to compute an intermediate value _z_, which is fed to an **activation function**. The perceptron uses the **sign function** as an activation function, but **other artificial neurons use other functions**.

The perceptron consists of a computational unit, a number of inputs, each with an associated input weight, and a single output:

![pg31_Image_7](https://user-images.githubusercontent.com/62965911/228531930-d901d5a1-a63e-41e8-8757-74e6147c8f95.jpeg)

#### Code snippet

```py
# First element in vector x must be 1.
# Length of w and x must be n+1 for neuron with n inputs.
def compute_output(w, x):
    z = 0.0
    for i in range(len(w)):
        z += x[i] * w[i] # Compute sum of weighted inputs
    if z < 0: # Apply sign function
        return -1
    else:
        return 1
```

#### Example of a Two-Input Perceptron

![pg34_Image_11](https://user-images.githubusercontent.com/62965911/228533452-755225d2-dab5-4e6b-b835-3d23d80ce92d.jpeg)

#### Perceptron and the NAND Gate

Behavior of a Perceptron with Two Inputs:

| X0 | X1              | X2              | W0\*X0 | W1\*X1 | W2\*X2 | _Z_  | _Y_             |
|----|-----------------|-----------------|--------|--------|--------|------|-----------------|
| 1  | −1<br>`(False)` | −1<br>`(False)` | 0.9    | 0.6    | 0.5    | 2.0  | 1<br>`(True)`   |
| 1  | 1<br>`(True)`   | −1<br>`(False)` | 0.9    | −0.6   | 0.5    | 0.8  | 1<br>`(True)`   |
| 1  | −1<br>`(False)` | 1<br>`(True)`   | 0.9    | 0.6    | −0.5   | 1.0  | 1<br>`(True)`   |
| 1  | 1<br>`(True)`   | 1<br>`(True)`   | 0.9    | −0.6   | −0.5   | −0.2 | −1<br>`(False)` |

The table shows the inputs and the outputs, the intermediate values after applying the weights, as well as the sum before applying the activation function. Note what happens if we interpret the inputs and outputs as Boolean values, where –1 represents `False` and +1 represents `True`. The perceptron with these specific weights implements a `NAND` gate! Paraphrasing Nielsen, this is comforting because we know that by combining multiple `NAND` gates, we can build any logical function, but it is also kind of disappointing because we thought that neural networks were going to be something much more exciting than just Boolean logic (Nielsen, 2015).

#### Perceptron Learning Algorithm

<a target="_blank" href="https://colab.research.google.com/gist/sparsh-ai/2f9831067b06b1adfa49455f893b2211/perceptron-learning.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

#### Limitation of Perceptron

Perceptron can learn straight line functions (e.g. NAND) but unable to learn curved line functions (e.g. XOR). One suggested solution for this is to use multi-level perceptron, which is close to a deep neural network because of its hidden-layer approach.

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
