# MLflow

MLflow is a platform that makes it simpler to manage the entire machine learning lifecycle. It enables you to track your experiments and their results, deploy and manage your models, and package your machine learning code in a reusable, reproducible format. It provides a central model registry that supports versioning and annotating, as well as model serving capabilities. It does that by redefining experimentation logs and module structure.

At a high level, the two main components are the tracking server and the model registry, as shown in the figure below. The others, which we will look at in more detail later, are supporting components of the flow. After the model is registered, the team can build automated jobs and use REST-serving APIs to move it downstream. Notice that the open source platform itself does not support model monitoring and the like, which requires dedicated engineering work.

![smls_0302](https://user-images.githubusercontent.com/62965911/223618504-c509da0d-f1b7-4eaa-9011-689275db4da4.png)
