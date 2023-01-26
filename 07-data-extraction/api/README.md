# Data Extraction from APIs

## Steps

1. [Lab: Data Extraction from archive.org](./lab-archive/)
1. [Lab: Data Extraction from exchangerates](./lab-exchangerates/)
1. [Lab: Data Extraction from coinmarketscap](./lab-extract-coinmarketcap/)
1. [Lab: Data Extraction from opennotify](./lab-extract-opennotify/)
1. [Lab: Data Extraction from saveonfoods](./lab-saveonfoods/)
1. [Lab: Data Extraction from twitter](./lab-twitter/)
1. [Lab: Data Extraction from uspopulation](./lab-uspopulation/)
1. [Lab: Data Extraction from various apis](./lab-various/)
1. [Lab: Processing REST Payloads on git api](./lab-processing-rest-payloads-git/)

## Note

### What is an API?

As we mentioned at the beginning of the chapter, API stands for Application Programming Interface.

This interface is designed to act as a connection layer between computers, or computer programs. It is therefore a type of software interface that provides a service to other pieces of software, in contrast to user interfaces, which instead connect computers to people.

An API is normally accompanied by a *specification document*, or *standard*, which describes how to build the API and how it works. A system that meets the specification is said to implement, or expose, the API. The term API can describe either the implementation or the specification.

An API is normally made of different parts, which are the tools that the programmers who write software use to interface with it. These parts are known by different names, the most common of which are *methods*, *subroutines*, or *endpoints* (we will call them endpoints in this chapter). When we use these parts, the technical term for this is *calling* them.

The API specification instructs you on how to call each endpoint, what type of requests to make, which parameters and headers to pass, which addresses to reach, and so on.

### What is the purpose of an API?

There are several reasons to introduce an API into a system. One we have already mentioned is to create the means for different pieces of software to communicate.

Another important reason is to allow access to a system by hiding its internal details and implementation, and exposing to the programmers only the parts that it is safe, and necessary, to expose.

The fact that APIs hide the internals of the systems they are interfaced with provides another benefit: if the internal system changes, in terms of technology, languages, or even workflows, the API can change in the way it connects to it, but still provide a consistent interface to the other side, the one that is exposed to the public. If we put a letter into a letterbox, we don't need to know or control how the postal service will deal with it, as long as the letter arrives at the destination. So, the interface (the letterbox) is kept consistent, while the other side (the mailman, their vehicles, technology, workflows, and so on) is free to change and evolve.

Finally, APIs are able to provide necessary features, such as **authentication** and **authorization**, and data validation. Being the layer that is exposed to the world, it makes sense that they are in charge of these tasks.

### API protocols

There are different types of API. They can be open to the public, or private. They can provide access to data, or services, or both. APIs can be written and designed using very different methods and standards, and they can employ different protocols.

These are the most common protocols:

-   **REST **(**Representational State Transfer**) is a Web services API. REST APIs are a key part of modern Web applications such as Netflix, Uber, and Amazon, among several others. In order for an API to be considered RESTful, it has to adhere to a set of rules. These include concepts like being stateless, providing a uniform interface, and client-server independence.
-   **SOAP **(**Simple Object Access Protocol**) is a well-established protocol similar to REST in that it's a type of Web API. SOAP was the first to standardize the way applications should use network connections to manage services. Its specification is very strict compared to that of REST. In general, it also requires more bandwidth.
-   **RPC **(**Remote Procedural Call**) is the oldest and simplest type of API. The implementation allows programmers to execute code on the server side by remotely calling a procedure (hence, the name). These types of API are tightly coupled with the implementation of the server they allow access to, so normally they are not made for the public, and maintaining them usually proves to be quite a complex task.

### REST — The Most Popular technology

Representational State Transfer (REST) is the most popular API development technology in modern web development. It provides a stateless architecture for data transferring. Client requests contain all the required details to fulfill the request, and the server does not keep the client’s state.

REST APIs support native HTTP caching headers and use HTTP methods (POST, GET, PUT, PATCH, and DELETE) to manipulate data. Anyone can get started with REST easily since it is simple and has a shallow learning curve.

Also, REST is easily scalable and reliable. Therefore, developers can choose it for their applications without any doubt. Even companies like Twitter, Paypal, and Google use REST APIs in their products.

#### Benefits of REST

- You can assuredly implement CRUD operations using standard HTTP methods.
- REST has been there for a long period, and almost every developer knows how to use it.
- It supports caching.
- It is scalable and provides separation between the client and the server.
- You can integrate it into multiple applications with ease.

#### Drawbacks of REST

- It has over-fetching and under-fetching issues.
- It can’t maintain states.
- It has large payload sizes.
- The number of endpoints drastically increases as the application scales.
- It isn’t easy to update database schema or data structures.

#### When to Choose REST

REST is the best choice if you do not have any specific requirements. For example, if you are new to development, using REST is the perfect match since it has a shallow learning curve. In addition, it has a large ecosystem, and you can easily find solutions to any problem you face.

Also, you would better use REST when dealing with many requests and limited bandwidth. You can use its caching support to improve performance in such situations.

Overall, we can not limit the use of REST to certain types of applications. For example, you can use REST if your application explicitly requires GraphQL or gRPC.

### GraphQL- A Client-Driven Standard

GraphQL is a data query language introduced in 2015. It allows developers to pinpoint and fetch the exact data they need. Compared to REST, GraphQL is a client-driven approach where the client can decide what data is needed, how to fetch data and the format. It also resolves the over-fetching and under-fetching issues since the client can pinpoint the required data.

GraphQL manipulates the data using queries, mutations, and subscriptions.

- Queries — To request data from the server.
- Mutations — To modify server-side data.
- Subscriptions — To get live updates when data gets updated.

GitHub is one of the biggest companies that use GraphQL. It switched to GraphQL from REST in 2016, and it significantly helped GitHub in its rapid growth.

#### Benefits of GraphQL

- It is highly flexible and delivers precisely what the client needs.
- It has no over-fetching and under-fetching.
- It is supported by well-known languages, including JavaScript, Java, Python, Ruby, and PHP.
- It allows customizing the structure of the data.
- A single query can contain fields from multiple resources.

#### Drawbacks of GraphQL

- Queries can be complex.
- It lacks built-in caching support.
- Learning GraphQL can be challenging compared to REST.
- It does not support file upload by default.

#### When to Choose GraphQL

GraphQL is an excellent choice for querying databases with many records. You can eliminate the over-fetching with GraphQL and only retrieve the necessary data in specific formats to increase the application performance. Also, GraphQL is well suited for situations where you need to aggregate data from multiple resources.

You can also useGraphQL when you do not entirely understand how the client uses the API. With GraphQL, you do not need to define a strict contract upfront. Instead, you can gradually build up the API based on client feedback.

### gRPC — A Performance-Oriented Technology

gRPC is an evolved version of remote procedure calls introduced by Google in 2016. It is a lightweight solution and provides maximum performance using minimum resources.

gRPC follows a contract-based approach to communication. It requires both client and the server to have contracts before starting the communication. gRPC uses Protobuf(a declarative language) for contract creation, and it generates compatible codes for both client and the server using a selected language.

There are 4 communication methods supported by gRPC:

- Unary — First, the client makes a single request to the server. Then, the server sends a single response.
- Client-Streaming — First, the client streams a series of requests to the server, followed by a message to inform that the stream is over. Finally, the server sends a single reply.
- Server-Streaming — First, the client makes a single request to the server. Then, the server sends a stream of messages to the client.
- Bidirectional Streaming — Both client and the server can send messages at any time after establishing the initial connection.

#### Benefits of gRPC

- It is open source. So developers can modify it as needed.
- It supports multiple languages, including JavaScript, Java, C, C++, C#, Kotlin, Python, Go, and PHP.
- It is capable of load balancing.
- It uses HTTP2 by default to reduce the latency compared to REST APIs.
- It serializes data in binary format.
- It supports full-duplex streaming.

#### Drawbacks of gRPC

- It doesn’t come with browser support by default.
- It doesn’t have firm community support compared to REST and GraphQL.

#### When to Choose gRPC

gRPC is an excellent option for communication between devices with low resources. For example, IoT devices, smart devices, and cameras can benefit from using gRPC since it optimizes the performance using minimum resources.

In addition to that, gRPC can be used in microservices architecture to handle communications between services since it can communicate with services written in different languages.