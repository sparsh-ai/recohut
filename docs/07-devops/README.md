# DevOps

## Infra-as-Code (IaC)

![iac-flow](https://user-images.githubusercontent.com/62965911/214911780-9806c6d6-9355-46e8-82cd-2286b6892b0f.png)

Infrastructure as code (IaC) refers to the management of existing infrastructure components such as storage devices, networking, and communication channels as well as load balancers and servers. It is also a method for automating the provisioning of IT infrastructure that uses a high-level descriptive coding language. Developers are freed of the burden of manually provisioning and maintaining servers, operating systems, database connections, storage, and other infrastructure components while creating, testing, and delivering software applications. Alternatively, they may go with automation.

Infrastructure management has been a time-consuming full-time profession for decades. However, critical infrastructure management has evolved considerably during the last decade. Microsoft Azure, Google, Oracle, and Amazon Web Services are just a few of the public cloud providers that provide essential infrastructure management services to its thousands of customers. You may have heard the term infrastructure as code as the popularity of public cloud platforms has grown, as has access to and consumption of the infrastructure the platforms offer.

Before we had fancy DevOps titles and job descriptions, we were lowly system administrators, or sysadmins for short. Those were the dark, pre-cloud days when we had to load the trunks of our cars with bare-metal servers and drive to a colocation (colo) facility to rack the servers, wire them, attach a wheeled monitor/keyboard/mouse to them, and set them up one by one. Grig still shudders to think about the hours he spent in colos, in blinding light and freezing A/C. We had to be wizards at Bash scripting, then we graduated to Perl, and the more fortunate of us to Python. As the saying went, the internet circa 2004 was held together with duct tape and bubble gum.

Somewhere during the period of 2006 to 2007, we discovered the magical world of Amazon EC2 instances. We were able to provision servers through a simple point-and-click interface, or through command-line tools. No more driving to colocation facilities, no more stacking and wiring bare-metal servers. We could go wild and launch 10 EC2 instances at a time. Or even 20! Or even 100! The sky was the limit. However, we quickly figured out that manually connecting to each EC2 instance using SSH and then setting up our applications on every instance separately was not going to scale. It was fairly easy to provision the instances themselves. What was difficult was to install the required packages for our applications, add the correct users, make sure the file permissions looked right, and finally install and configure our applications. To scratch this itch, the first generation of infrastructure automation software came into being, represented by “configuration management” tools. Puppet was the first well-known configuration management tool, released in 2005 and predated the release of Amazon EC2. Other such tools that were launched on the heels of Puppet were Chef in 2008, followed by SaltStack in 2011, and Ansible in 2012.

By 2009, the world was ready to welcome the arrival of a new term: DevOps. To this day, there are competing definitions of DevOps. What is interesting is that it came into being in the tumultuous early days of infrastructure software automation. While there are important people and culture aspects to DevOps, one thing stands out in this chapter: the ability to automate the provisioning, configuration, and deployment of infrastructure and applications.

By 2011, it was getting hard to keep track of all the services comprising the Amazon Web Services (AWS) suite. The cloud was much more complicated than raw compute power (Amazon EC2) and object storage (Amazon S3). Applications started to rely on multiple services interacting with each other, and tools were needed to help automate the provisioning of these services. Amazon didn’t wait long to fill this need, and in 2011 it started offering just such a tool: AWS CloudFormation. This was one of the first moments when we could truly say that we were able to describe our infrastructure through code. CloudFormation opened the doors to a new generation of Infrastructure as Code (IaC) tools, which were operating at the layer of the cloud infrastructure itself, underneath the layer served by the first-generation configuration management tools.

By 2014, AWS had launched dozens of services. That was the year when another important tool in the world of IaC came into being: Terraform, by HashiCorp. To this day, the two most used IaC tools are CloudFormation and Terraform.

Another important development in the world of IaC and DevOps was taking place sometime between late 2013 and early 2014: the release of Docker, which came to be synonymous with container technologies. Although containers had been around for a number of years, the great benefit that Docker brought to the table was that it wrapped technologies such as Linux containers and cgroups into an easy-to-use API and command-line interface (CLI) toolset that significantly lowered the barrier of entry for people who wanted to package their applications into containers that could be deployed and run wherever Docker was running.

The usage and mindshare of Docker exploded and damaged the popularity of the first-generation configuration management tools (Puppet, Chef, Ansible, SaltStack). The companies behind these tools are reeling at the moment and are all trying to stay afloat and current by reinventing themselves as cloud friendly. Before the advent of Docker, you would provision the infrastructure for your application with an IaC tool such as CloudFormation or Terraform, then deploy the application itself (code and configuration) with a configuration management tool such as Puppet, Chef, Ansible, or SaltStack. Docker suddenly made these configuration management tools obsolete, since it provided a means for you to package your application (code + configuration) in a Docker container that would then run inside the infrastructure provisioned by the IaC tools.

Fast-forward to 2020 and it is easy to feel lost as a DevOps practitioner when faced with the multitude of infrastructure automation tools available.

One way to differentiate IaC tools is by looking at the layer at which they operate. Tools such as CloudFormation and Terraform operate at the cloud infrastructure layer. They allow you to provision cloud resources such as compute, storage, and networking, as well as various services such as databases, message queues, data analytics, and many others. Configuration management tools such as Puppet, Chef, Ansible, and SaltStack typically operate at the application layer, making sure that all the required packages are installed for your application, and that the application itself is configured correctly (although many of these tools also have modules that can provision cloud resources). Docker also operates at the application layer.

Another way to compare IaC tools is by dividing them into declarative versus imperative categories. You can tell an automation tool what to do in a declarative manner where you describe the state of the system that you are trying to achieve. Puppet, CloudFormation, and Terraform operate in a declarative manner. Alternatively, you can use an automation tool in a procedural or imperative manner, where you specify the exact steps needed by the tool to achieve the desired system state. Chef and Ansible operate in an imperative manner. SaltStack can operate in both declarative and imperative manners.

Let’s look at the desired state of the system as a blueprint for the construction of a building, let’s say a stadium. You use procedural tools like Chef and Ansible to build the stadium, section by section and row by row inside each section. You need to keep track of the state of the stadium and the progress of the construction. Using declarative tools such as Puppet, CloudFormation, and Terraform, you first put together the blueprint for the stadium. The tool then makes sure that the construction achieves the state depicted in the blueprint.

One dimension is the way you specify the desired state of the system. In CloudFormation, you do it with JSON or YAML syntax, while in Terraform you do it with the proprietary HashiCorp Configuration Language (HCL) syntax. In contrast, Pulumi and the AWS Cloud Development Kit (CDK) allow you to use real programming languages, including Python, for specifying the desired state of the system.

Another dimension is the cloud providers supported by each tool. Since CloudFormation is an Amazon service, it stands to reason that it focuses on AWS (although one can define non-AWS resources with CloudFormation when using the custom resources feature). The same is true for the AWS CDK. In contrast, Terraform supports many cloud providers, as does Pulumi.

### Benefits

There are many benefits to using IaC in the data engineering field. Some of the main benefits include:

- Reproducibility: With IaC, data engineers can easily reproduce their infrastructure in different environments. This is useful for testing, staging, and production environments, as well as for disaster recovery.
- Collaboration: IaC allows data engineers to collaborate more effectively on infrastructure projects. They can use version control systems to track changes to their code, and they can use code review tools to ensure that their code is of high quality.
- Documentation: Code is a form of documentation, and IaC provides a clear and concise way to document the data engineering infrastructure. This is useful for onboarding new team members and for maintaining the infrastructure over time.
- Scalability: IaC makes it easy for data engineers to scale their infrastructure up or down as needed. They can use code to define their infrastructure in a way that is flexible and adaptable to changing needs.

### Tools

There are many tools and technologies that data engineers can use to implement IaC. Some popular options include:

- Terraform: Terraform is an open-source IaC tool that allows data engineers to define and manage their infrastructure as code. It supports a wide range of infrastructure providers, including AWS, Azure, and Google Cloud.
- Puppet: Puppet is an open-source IaC tool that allows data engineers to automate the configuration of their infrastructure. It uses a declarative language called Puppet DSL to define the desired state of the infrastructure, and it ensures that the infrastructure is always in that state.
- Ansible: Ansible is an open-source IaC tool that allows data engineers to automate the deployment and configuration of their infrastructure. It uses a simple YAML syntax to define the desired state of the infrastructure, and it can be used to manage a wide range of infrastructure types.

## CI/CD Pipelines

A CI/CD pipeline automates the process of software delivery. It builds code, runs tests, and helps you to safely deploy a new version of the software. CI/CD pipeline reduces manual errors, provides feedback to developers, and allows fast product iterations.

CI/CD pipeline introduces automation and continuous monitoring throughout the lifecycle of a software product. It involves from the integration and testing phase to delivery and deployment. These connected practices are referred as CI/CD pipeline.

### What is Continuous Integration, Continuous Delivery, and Continuous Deployment?

- **Continuous integration** is a software development method where members of the team can integrate their work at least once a day. In this method, every integration is checked by an automated build to search the error.
- **Continuous delivery** is a software engineering method in which a team develops software products in a short cycle. It ensures that software can be easily released at any time.
- **Continuous deployment** is a software engineering process in which product functionalities are delivered using automatic deployment. It helps testers to validate whether the codebase changes are correct, and it is stable or not.

### Stages of a CI/CD pipeline

A CI/CD pipeline is a runnable specification of the steps that any developer should perform to deliver a new version of any software. Failure in each and every stage triggers a notification via email, Slack, or other communication platforms. It enables responsible developers to know about the important issues.

#### Source Stage

In the source stage, CI/CD pipeline is triggered by a code repository. Any change in the program triggers a notification to the CI/CD tool that runs an equivalent pipeline. Other common triggers include user-initiated workflows, automated schedules, and the results of other pipelines.

#### Build Stage

This is the second stage of the CI/CD Pipeline in which you merge the source code and its dependencies. It is done mainly to build a runnable instance of software that you can potentially ship to the end-user.

Programs that are written in languages like C++, Java, C, or Go language should be compiled. On the other hand, JavaScript, Python, and Ruby programs can work without the build stage.

Failure to pass the build stage means there is a fundamental project misconfiguration, so it is better that you address such issue immediately.

#### Test Stage

Test Stage includes the execution of automated tests to validate the correctness of code and the behaviour of the software. This stage prevents easily reproducible bugs from reaching the clients. It is the responsibility of developers to write automated tests.

#### Deploy Stage

This is the last stage where your product goes live. Once the build has successfully passed through all the required test scenarios, it is ready to deploy to live server.

### Example of CI/CD Pipeline

Here is example of CI/CD pipeline:

- **Source Code Control:** Host code on GitHub as a private repository. This will help you to integrate your application with major services and software.
- **Continuous integration:** Use continuous integration and delivery platform CircleCI and commit every code. When the changes notify, this tool will pull the code available in GitHub and process to build and run the test.
- **Deploy code to UAT:** Configure CircleCI to deploy your code to AWS UAT server.
- **Deploy to production:** You have to reuse continuous integration steps for deploying code to UAT.

### Summary

* A CI/CD pipeline automates the process of software delivery.
* CI/CD pipeline introduces automation and continuous monitoring throughout the lifecycle of a software product.
* Continuous integration is a software development method where members of the team can integrate their work at least once a day.
* Continuous delivery is a software engineering method in which a team develops software products in a short cycle.
* Continuous deployment is a software engineering process in which product functionalities are delivered using automatic deployment.
* There are four stages of a CI/CD pipeline 1) Source Stage, 2) Build Stage, 3) Test Stage, 4) Deploy Stage.
* Important CI/CD tools are Jenkins, Bambo, and Circle CI.
* CI/CD pipeline can improve reliability.
* CI/CD pipeline makes IT team more attractive to developers.
* Cycle time is the time taken to go from the build stage to production.
* Development frequency allows you to analyse bottlenecks you find during automation.
* Change Lead Time measures the start time of the development phase to deployment.
* Change Failure Rate focuses on the number of times development get succeeds vs. the number of times it fails.
* MTTR (Mean Time to Recovery) is the amount of time required by your team to recover from failure.
* MTTF (Mean Time to Failure) measures the amount of time between fixes and outages.
