# Cloud Computing

Renting someone else's server: this definition of the cloud is my favorite, very simple, to the point, definition of what the cloud really is. So as long as you don't need to buy your own machine to store and process data, you are using the cloud.

But increasingly, after some leading cloud providers such as Google Cloud and Amazon Web Services having gained more traction and technology maturity, the terminology is becoming representative of sets of architecture, managed services, and highly scalable environments that define how we build solutions. For data engineering, that means building data products using collections of services, APIs, and trusting the underlying infrastructure of the cloud provider one hundred percent.

Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider like Amazon Web Services (AWS).

<iframe width="100%" height="480" src="https://www.youtube.com/embed/mxT233EdY5c" title="What is Cloud Computing? | Amazon Web Services" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Who is using cloud computing?

Organizations of every type, size, and industry are using the cloud for a wide variety of use cases, such as data backup, disaster recovery, email, virtual desktops, software development and testing, big data analytics, and customer-facing web applications. For example, healthcare companies are using the cloud to develop more personalized treatments for patients. Financial services companies are using the cloud to power real-time fraud detection and prevention. And video game makers are using the cloud to deliver online games to millions of players around the world.

## Benefits of cloud computing

![511918_1_En_1_Fig7_HTML](https://user-images.githubusercontent.com/62965911/218317770-983bb98a-0d1e-4365-a795-c0ae15474ef9.jpeg)

### Agility

The cloud gives you easy access to a broad range of technologies so that you can innovate faster and build nearly anything that you can imagine. You can quickly spin up resources as you need them–from infrastructure services, such as compute, storage, and databases, to Internet of Things, machine learning, data lakes and analytics, and much more.

You can deploy technology services in a matter of minutes, and get from idea to implementation several orders of magnitude faster than before. This gives you the freedom to experiment, test new ideas to differentiate customer experiences, and transform your business.

Cloud providers are constantly innovating and adding new services and technologies to their offerings depending on what they learn from multiple customers. Leveraging state-of-the-art services and technologies helps you innovate faster for your business scenarios, compared with having in-house developers who might not have the necessary breadth of knowledge across the industry.

### Elasticity

With cloud computing, you don’t have to over-provision resources up front to handle peak levels of business activity in the future. Instead, you provision the amount of resources that you actually need. You can scale these resources up or down to instantly grow and shrink capacity as your business needs change.

The resources that you need for your business are highly dynamic in nature, and there are times when you need to provision resources for planned and unplanned increases in usage. When you maintain and run your hardware, you are tied to the hardware you have as the ceiling for the growth you can support in your business. Cloud resources have an elastic scale, and you can burst into high demand by leveraging additional resources in a few clicks.

### Cost savings

The cloud allows you to trade fixed expenses (such as data centers and physical servers) for variable expenses, and only pay for IT as you consume it. Plus, the variable expenses are much lower than what you would pay to do it yourself because of the economies of scale.

### Lowered TCO

TCO refers to the total cost of ownership of the technical solution you maintain, including the datacenter costs, the software costs, and the salaries of people who need to be employed to manage the operations. In almost all cases, barring a few exceptions, the TCO is significantly lower for building solutions on the cloud compared with the solutions that are built in house and deployed in your on-premises datacenter. This is because you can focus on hiring software teams to write code for your business logic while the cloud providers take care of all other hardware and software needs for you. Some of the contributors to this lowered cost include the following:

**Cost of hardware**

The cloud providers own, build, and support the hardware resources at a lower cost than if you were to build and run your own datacenters, maintain hardware, and renew your hardware when the support runs out. Further, with the advances made in hardware, cloud providers enable newer hardware to be accessible much faster than if you were to build your own datacenters.

**Cost of software**

In addition to building and maintaining hardware, one of the key efforts for an IT organization is to support and deploy operating systems and keep them updated. Typically, these updates involve planned downtimes that can also be disruptive to your organization. The cloud providers take care of this cycle without burdening your IT department. In almost all cases, these updates happen in an abstracted fashion so that you don’t need to be affected by any downtime.

**Pay for what you use**

Most of the cloud services work on a subscription-based billing model, which means that you pay for what you use. If you have resources that are used for certain hours of the day or certain days of the week, you only pay for that time, which is a lot less expensive than having hardware all the time even if you don’t use it.

### Deploy globally in minutes

With the cloud, you can expand to new geographic regions and deploy globally in minutes. For example, AWS has infrastructure all over the world, so you can deploy your application in multiple physical locations with just a few clicks. Putting applications in closer proximity to end users reduces latency and improves their experience.

## The evolution of the generations

- Gen 1: On-Premises and Traditional IT Ops
- Gen 2: Hybrid cloud, infrastructure (VM) focused
- Gen 3: Cloud first, agile operations
- Gen 4: Cloud native, born in cloud

## Types of cloud computing

The three main types of cloud computing include Infrastructure as a Service, Platform as a Service, and Software as a Service. Each type of cloud computing provides different levels of control, flexibility, and management so that you can select the right set of services for your needs.

### Infrastructure as a Service (IaaS)

IaaS contains the basic building blocks for cloud IT. It typically provides access to networking features, computers (virtual or on dedicated hardware), and data storage space. IaaS gives you the highest level of flexibility and management control over your IT resources. It is most similar to the existing IT resources with which many IT departments and developers are familiar.

### Platform as a Service (PaaS)

PaaS removes the need for you to manage underlying infrastructure (usually hardware and operating systems), and allows you to focus on the deployment and management of your applications. This helps you be more efficient as you don’t need to worry about resource procurement, capacity planning, software maintenance, patching, or any of the other undifferentiated heavy lifting involved in running your application.

### Software as a Service (SaaS)

SaaS provides you with a complete product that is run and managed by the service provider. In most cases, people referring to SaaS are referring to end-user applications (such as web-based email). With a SaaS offering, you don’t have to think about how the service is maintained or how the underlying infrastructure is managed. You only need to think about how you will use that particular software.

## Comparison of Cloud Services

<html>
<table>
<thead>
  <tr>
    <th>Service</th>
    <th>Amazon Web Services (AWS)</th>
    <th>Microsoft Azure</th>
    <th>Google Cloud Platform (GCP)</th>
  </tr>
</thead>
<tbody>
  <tr>
      <td colspan='4'><center><b>Servers and Containers</b></center></td>
  </tr>
  <tr>
    <td>Virtual Servers</td>
    <td>Elastic Cloud Compute</td>
    <td>Virtual Machines</td>
    <td>Google Compute Engine</td>
  </tr>
  <tr>
    <td>Serverless Computing</td>
    <td>Lambda</td>
    <td>Azure Functions</td>
    <td>Cloud Functions</td>
  </tr>
  <tr>
    <td>Kubernetes Management</td>
    <td>Elastic Kubernetes Service</td>
    <td>Kubernetes Service</td>
    <td>Kubernetes Engine</td>
  </tr>
  <tr>
    <td colspan='4'><center><b>Data Storage</b></center></td>
  </tr>
  <tr>
    <td>Object Storage</td>
    <td>Simple Storage Service</td>
    <td>Azure Blob</td>
    <td>Cloud Storage</td>
  </tr>
  <tr>
    <td>File Storage</td>
    <td>Elastic File Storage</td>
    <td>Azure Files</td>
    <td>Filestore</td>
  </tr>
  <tr>
    <td>Block Storage</td>
    <td>Elastic Block Storage</td>
    <td>Azure Disk</td>
    <td>Persistent Disk</td>
  </tr>
  <tr>
    <td>Relational Database</td>
    <td>Relational Database Service</td>
    <td>SQL Database</td>
    <td>Cloud SQL</td>
  </tr>
  <tr>
    <td>NoSQL Database</td>
    <td>DynamoDB</td>
    <td>Cosmos DB</td>
    <td>Firestore</td>
  </tr>
  <tr>
    <td colspan='4'><center><b>Network</b></center></td>
  </tr>
  <tr>
    <td>Virtual Network</td>
    <td>Virtual Private Cloud</td>
    <td>Azure VNet</td>
    <td>Virtual Private Network</td>
  </tr>
  <tr>
    <td>Content Delivery Network</td>
    <td>CloudFront</td>
    <td>Azure CDN</td>
    <td>Cloud CDN</td>
  </tr>
  <tr>
    <td>DNS Service</td>
    <td>Route 53</td>
    <td>Traffic Manager</td>
    <td>Cloud DNS</td>
  </tr>
  <tr>
    <td colspan='4'><center><b>Security and Authorization</b></center></td>
  </tr>
  <tr>
    <td>Authentication and Authorization</td>
    <td>IAM</td>
    <td>Azure Active Directory</td>
    <td>Cloud IAM</td>
  </tr>
  <tr>
    <td>Key Management</td>
    <td>KMS</td>
    <td>Azure Key Vault</td>
    <td>KMS</td>
  </tr>
  <tr>
    <td>Network Security</td>
    <td>AWS WAF</td>
    <td>Application Gateway</td>
    <td>Cloud Armor</td>
  </tr>
</tbody>
</table>
</html>
