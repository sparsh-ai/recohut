# Disaster Response Pipeline

![wall](https://user-images.githubusercontent.com/62965911/211199160-a8e841d9-cb03-4fa0-ace8-453495d7c8a3.png)

There were 323 recorded natural disasters worldwide in 2022. Although most people only hear the Amber Alerts go off 🔊, there are disaster response teams in place, and they need to respond fast! I think we can agree that that's a difficult job. Now, imagine how difficult that must be with a vast amount of data coming through several channels, and one has to decipher which data is actionable quickly. That job just became more difficult.

Creating solutions that help disaster response teams make the right decisions fast would prove immensely helpful to our society in such events. Therefore, introductory projects such as this one can be scaled to near perfection (as they may be with Palantir's many decision-making offerings). Open-source connoisseurs can contribute to similar projects and help protect people worldwide, one disaster at a time.

Our goal is to build a web app to emergency worker that help classify instantaeously new disaster messages in several categories. With such a classification, the emergency worker can send the messages to the appropriate disaster relief agency. The web app is based on model trained on the analysis of older disaster data provided from Appen. An API will allow the emergency worker to interface with the web app by inserting new messsage, get the related categories and get some vizualizations of the database content.

We will:

1. Perform ETL and save the data in SQLite database
2. Train model using Scikit-learn library
3. Create a Flask-based App and Serve the application

## Dashboard

![dash](https://user-images.githubusercontent.com/62965911/211199156-a0fdfea1-5af2-4678-9e47-f6d2f9744496.png)

![dash-response](https://user-images.githubusercontent.com/62965911/215279205-02e0673c-842d-41b9-932b-bb3727cacda0.png)