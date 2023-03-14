# Webshoes

**Webshoes** is a fictitious sales company of shoes and accessories that is being created. The company's business areas have defined that Webshoes will have an online store and that the store will need to have personalized experiences. The requirements that the business areas have passed to the project development team are as follows:

- **Online store** -- The online store should have a simple catalog with the 12 different products of the brand
- **Smart banner** -- If the customer clicks on a product, similar products should appear in a **Recommended** banner, with products that have the same characteristics as the one selected, but only products that the customer has not purchased yet
- **Sales conversion messages** -- If the customer does not complete the sale and has logged into the portal, the online store should contact the customer via email and a message on their cell phone later, with the triggering of a few messages created for conversion of the sale

By analyzing these business requirements, we can do the following *technical decomposition* to select the appropriate data storage:

- **Online store** -- A repository to store the product catalog, a repository to register the sales through the shopping cart, and a repository to store customer login
- **Smart banner** -- Depending on the customer and product selected, a near real-time interaction of banner customization
- **Sales conversion messages** -- Will be processed after the customer leaves the online store (closing their login session) and depends on their actions while browsing the website and purchase history

Now, with the knowledge gained in this module, can you help me to select suitable storage types for each requirement?

Come on, let's go! Here are the solutions:

- **Online store** -- *Transactional workload*. A SQL relational or NoSQL database can assist in this scenario very well, as it will have product entities, customers, login information, and shopping carts, among others, already related in the database.
- **Smart banner** -- *Analytical workload*. For near real-time processing, data streaming is required, capturing the behavior of the client and crossing it with the other historical data. In this case, an analytical base can process the information and return the application/banner to the appropriate message for customization.
- **Sales conversion messages** -- *Analytical workload*. In this case, the customer will have left the store, and we do not need to work with data streaming but rather a batch load of data. It is important to evaluate with the business area how long it is optimal to send messages to target customers, and the analytical base will process the information, generating the message list to be fired.

Therefore, each use case can define a different data workload type, which influences our database decision.