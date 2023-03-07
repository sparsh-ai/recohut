# FastAPI

## Objective

Designing and developing REST APIs with FastAPI

## Steps

### Lab: Online Academic Discussion Forum API

This application must provide online support for knowledge construction and communication mechanism among students, faculty, family members, or users in an organization. It is a microservice application that can establish an exchange of ideas and discuss unlimited topics, including social activities and educational ideas among users. This application uses the FastAPI framework.

### Lab: Online Book Reselling System API

This prototype is an online book repository that accepts used books for cataloging. The books are classified according to the genre and given details for profiling. Users can purchase from this book catalogs, and all purchases have receipts. All order, payment, and purchasing transactions are recorded for auditing purposes. In totality, this prototype can be a basis for an e-commerce platform for used book exchange and sale. This application uses the FastAPI framework.

### Lab: FastAPI integrated with the Databricks Lakehouse

At its core, a Data Lakehouse enables efficient and secure access to data stored in a Data Lake. This architecture promises to blend all the great qualities of a data lake (object storage, unstructured data, etc.) and those of a traditional data warehouse (ACID transactions, performance, etc.) Hence, Data lake + house.

Developers in the Lakehouse can leverage various standard tools for data analytics, engineering, and ML workloads. So, can an application developer also leverage Lakehouse to build a scalable data application? Short answer: Yes!

We will create a simple FastAPI server with a backend database on a Databricks Lakehouse that supports full create, read, update and delete (CRUD) operations with SQLAlchemy.

### Lab: FastAPI Applications

In this lab, we will practice building couple of more applications using the FastAPI framework.

1. Auction System
2. ERP System
3. Todo App
4. Task Planner System

### Lab: FastAPI DevOps

In this lab, we will build and deploy a FastAPI. We will deploy it in a serverless manner using AWS's SAM (Serverless Application Model) framework. We will also use Cloudformation stack to automate the pipeline CICD.

### Lab: FastAPI Lakehouse

In this lab, we will create a CRUD database features in FastAPI. We will use Delta-based Lakehouse as our database. We will generate some synthetic data using Python's Faker library.

### Lab: Fitness Club Management System API

This prototype is an application designed to manage transactions in a gym center. This system allows scheduling of gym customers to available gym classes like aerobics, boxing, circuit, pilates, etc. It also maps gym trainers to classes where registered gym-goers are registered. As part of the control and tracking mechanism, the prototype manages the attendance of the trainers and gym-goers. This application uses the FastAPI framework.

### Lab: NewsStand Manegement System API

This prototype is a portal for managing newspaper sales and distribution. The system caters to several newspaper organizations for marketing, sales, and content management. The system requires each organization to register their respective representative(s) for the login credentials to access the system. After user approval, the representative can manage and approve the content of their daily issue based on the agreed budget and scopes. The application has services that can monitor sales periodically and create a pool of messengers paid to deliver the papers to different outlets. Moreover, the system can track customers and the outlets where they bought their newspapers. The prototype is an initial attempt to create a platform for a newspaper management portal. This application uses the FastAPI framework.

### Lab: Poverty Analysis System API

The prototype is about gathering poverty-related data from a sample size of respondents. The project has two microservices: the piccolo-relational, which uses a relational database, and the piccolo-mongo, which uses the NoSQL database. The piccolo-relational features only highlight descriptive statistics, plotting of data, formulation of linear and nonlinear models, and solving the roots of the models. The transactions in this project utilize mainly the NumPy, pandas, scipy, and matplotlib modules. On the other hand, the piccolo-mongo focuses on workflow using Celery and Redis, GraphQL with graphene 3, and Ne04J operations. The prototypes can still be enhanced and expanded to cater to more mathematical and symbolic computations. This application uses the FastAPI framework.

### Lab: Online Recipe System API

This prototype aims to store various recipes on any menu to be viewed and rated by visitors. It even classifies the recipes according to the place of origin and menu type. Users may search for their desired recipe for reference, rating, and feedback purposes. It has a feature that allows users to attach keywords to each recipe for search purposes. The microservice application is an initial architecture for a robust online recipe platform. This application uses the FastAPI framework driven by Python 3.8. No database included yet. The requirements.txt will guide you with the dependencies. Just install by running: pip install -r requirements.txt ## Details It is feasible to use a repository-service pattern in some complex FastAPI applications through DI. The repository-service pattern is responsible for the creation of the repository layer of the application, which manages the Creation, Reading, Updates, and Deletion (CRUD) of data source. A repository layer requires data models that depict the table schemas of a collection or database. The repository layer needs the service layer to establish a connection with other parts of the application. The service layer operates like a business layer, where the data sources and business processes meet to derive all the necessary objects needed by the REST API. The communication between the repository and service layers can only be possible by creating injectables.

### Lab: Online Restaurant Review System API

This prototype is a feedback and rating system designed for various restaurants. Users are required to answer survey questions regarding the restaurant's ambiance, menu, and hospitality. Aside from survey systems, the application can provide a nominal and numerical approach to the rating system. Overall, the prototype can be a foundation for a scalable survey system. This application uses the FastAPI framework.

### Lab: Intelligent Tourist System API

This application creates an interconnection between location, visits, visitors, and tourist spots in a particular place. The application highlights API services that store dynamic and fixed enum data in a Python collection about tourist posts in every locality in a country, state, city, or province. There is also a simulation of a mini-reservation mechanism given for each user or visitor. This prototype will be a good backbone for a travelogue-style microservice architecture that can be applied in tourism-related businesses. This application uses the FastAPI framework.