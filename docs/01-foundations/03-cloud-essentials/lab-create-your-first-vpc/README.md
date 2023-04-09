# Introduction to Virtual Private Cloud (VPC)

## Description

Amazon Virtual Private Cloud (VPC) lets you provision a logically isolated section of the Amazon Web Services (AWS) Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including the selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. This hands-on lab guides you through the creation of a VPC and some of its common sub-resources.

![env drawio](https://user-images.githubusercontent.com/62965911/219861286-e0541d5f-19aa-4aa8-adb3-f2822376f70d.svg)

## Learning Objectives

Upon completion of this lab you will be able to:

- Use the AWS Management Console to create a VPC
- Use the AWS Management Console to create resources that work with Amazon VPC, including a subnet and an internet gateway
- Configure routing for your VPC using a route table
- Create and manage an EC2 instance and an associated Elastic IP Address (EIP) within your VPC

## Prerequisites

You should be familiar with:

- Some familiarity with basic networking principles is helpful but not required
- Some familiarity with the AWS Management Console is helpful but not required

## Steps

### Creating a VPC

#### Introduction

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center with the benefits of using the scalable infrastructure of AWS. It is logically isolated from other virtual networks in the AWS cloud.

You can create a new VPC using the AWS Management Console.

#### Instructions

1\. In the AWS Management Console search bar, enter *VPC*, and click the **VPC** result under **Services.**

2\. From the VPC dashboard, click on **Your VPCs** link in the sidebar menu. This page lists all previously created VPCs. Every new AWS account comes with a **Default VPC**.

3\. Click **Create VPC** to begin creating a new VPC.

4\. Specify the following VPC details on the Create VPC page then click **Create VPC:**

- **Resources to create**: Select **VPC only**
- **Name tag**: `de-labs`. This is the name for your VPC; doing so creates a tag with a key of Name and the value that you specify.
- **CIDR block**: `10.0.0.0/16`. You should specify a CIDR block from the private (non-publicly routable) IP address ranges as specified in RFC 1918.
- **IPv6 CIDR block**: No IPv6 CIDR block. VPCs support IPv6 addresses but this is not a focus for this Lab.
- **Tenancy**: `Default`. Dedicated tenancy ensures your instances run on single-tenant hardware. 

Amazon creates the requested VPC and the following linked services:

- a **DHCP options set** (this set enables DNS for instances that need to communicate over the VPC's Internet gateway) 
- a **Route Table** (it contains a set of rules, called *routes*, that are used to determine where network traffic is directed) 
- a **Network ACL** (it is a list of rules to determine whether traffic is allowed in or out of any subnet associated with the network ACL)

*Note:* No Subnets or Internet Gateways are automatically created -- you need to add them manually.

#### Summary

In this Lab Step, you created a VPC. In the following steps, you will create additional resources within the VPC.

### Creating a VPC subnet

#### Introduction

A VPC subnet is a range of IP addresses in your VPC. You can add one or more subnets in each Availability Zone, but each subnet must reside entirely within one Availability Zone and cannot span zones. Availability Zones are distinct locations that are engineered to be isolated from failures in other Availability Zones. By launching instances in separate Availability Zones, you can protect your applications from the failure of a single location.

You can create a new subnet for your previously created VPC using the AWS Management Console.

#### Instructions

- From the VPC dashboard, click the **Subnets** link in the sidebar menu.
- The Subnets page lists all previously created subnets. At this point, there are four automatically created default subnets associated with the default VPC. When you have many subnets, you can use the **Filter by VPC** feature for listing only the subnets linked to a specific VPC.
- Click **Create Subnet** to begin creating a new subnet.
- In the **Create Subnet** form, specify the following Subnet details then click **Create subnet**:
  - **VPC ID**: `de-labs`. 
  - **Subnet Name**: `Public-A`. This is the name for your subnet; doing so creates a tag with a key of Name and the value that you specify.
  - **Availability Zone**: `us-west-2a`. 
  - **CIDR block**: `10.0.0.0/24`. You should specify a CIDR block in the selected VPC.

#### Summary

In this Lab Step, you created a subnet for your AWS VPC.

### Creating a VPC Internet Gateway

#### Introduction

An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between instances in your VPC and the Internet. It imposes no availability risks or bandwidth constraints on your network traffic. An internet gateway serves two purposes: to provide a target in your VPC route tables for internet-routable traffic and to perform network address translation (NAT) for instances that have been assigned public IP addresses.

You can create a new internet gateway for your previously created VPC using the AWS Management Console.

#### Instructions

- From the VPC dashboard, click the **Internet gateways** link in the sidebar menu.
- Click **Create Internet Gateway** to begin creating a new gateway.
- On the **Create internet gateway** form, enter *labs-gw* in the **Name tag** field and then click Create internet gateway.
- Click **Actions -> Attach to VPC** to attach to a VPC.
- In the **Attach to VPC** page, select the VPC `de-labs` from the list, and then click **Attach Internet gateway.**

#### Summary

In this Lab Step, you created an internet gateway for your VPC.

### Connecting the Internet Gateway to the VPC Route Table

#### Introduction

To use an internet gateway your subnet's route table must contain a route that directs internet-bound traffic to the internet gateway. You can scope the route to all destinations not explicitly known to the route table (0.0.0.0/0), or you can scope the route to a narrower range of IP addresses; for example, the public IP addresses of your company's public endpoints outside of AWS, or the Elastic IP addresses of other Amazon EC2 instances outside your VPC. If your subnet is associated with a route table that has a route to an internet gateway, it's known as a public subnet.

You can add routes to your previously created VPC route table using the AWS Management Console.

#### Instructions

- From the VPC dashboard, click the **Route table**s link in the sidebar menu.
- Select the **Main** route table for the `de-labs` VPC.
- Select the **Routes** tab. Routes are a set of rules which are used to determine where network traffic is directed.
- Click the **Edit routes** button.
- Click **Add route** and set the following values before clicking **Save changes**:
  - **Destination**: Enter `0.0.0.0/0` as the CIDR block
  - **Target**: Click **Internet Gateway** and then select your previously-created internet gateway

This sets all external traffic for the main route table of your VPC to go through the internet gateway.

#### Summary

In this Lab Step, you configured your VPC's main route table to route external traffic to the internet gateway, which enabled internet connectivity for your VPC.

### Creating an EC2 instance

#### Introduction

In this Lab Step you will create an EC2 instance inside your VPC.

#### Instructions

- In the AWS Management Console search bar, enter *EC2*, and click the **EC2** result under **Services.
- From the EC2 dashboard, click **Launch instance** > Launch instance.
- Under **Application and OS Images**, select Amazon Linux.
- Under **Instance type**, select t2.micro.
- Under **Key pair**, select Proceed without a key pair.
- Click on **Edit** within the **Network settings** section and select the following values:
  - **VPC**: Make sure the de-labs VPC is selected
  - **Subnet**: Select Public-A | US-west-2a
  - **Auto-assign Public IP**: Select Enable
  - **Inbound security group rules**: Click **Add security group rule**, and select **All traffic** for **Type** and **Anywhere** for **Source type**
- Under **Summary**, click Launch instance.
- Click on the ID of the instance you have created.
- Select the instance, ensure it is in the **Running** state, and record the **Public IPv4 address** found in the **Details** tab of the EC2 instance.

Open a terminal window on your computer (command prompt or PowerShell window on Windows or terminal on mac OSX and Linux) and execute the following command, replacing *`<PublicIPAddress>`* with the IP address you recorded:

```bash
ping `<PublicIPAddress>`
```

#### Summary

In this Lab Step, you created an EC2 instance within your AWS VPC and used its public IP address to ping it.

### Allocating and Associating an Elastic IP

#### Introduction

An Elastic IP address (EIP) is a static and public IP address that you can associate with an EC2 instance. EIPs have the benefit of not changing when you stop and start an EC2 instance, whereas the default public IP that comes with an EC2 instance may change. This gives you the benefit of a reliable IP address to associate with your EC2 instance. In this Lab Step you will allocate an EIP and associate it with your EC2 instance.

#### Instructions

- Navigate to the [VPC dashboard](https://us-west-2.console.aws.amazon.com/vpc/home?region=us-west-2).
- From the VPC dashboard, click on **Elastic IPs** link in the sidebar menu.
- Click **Allocate Elastic IP address** and then click Allocate.
- Review the newly-created EIP.
- With the EIP still selected, click **Actions** > **Associate Elastic IP address** and then select the following values:
  - **Resource type**: Instance
  - **Instance**: Select the only instance from the drop-down list. It is the instance you created.
  - **Private IP**: Leave this blank to have an available Private IP automatically assigned.
- Click **Associate** to associate the EIP to the selected EC2 instance.
- Notice the EIP now has an instance ID in the **Associated instance ID** column, corresponding to the EC2 instance you associated it with.
- Copy the **Allocated IPv4 address** in the **Summary** tab.

In a terminal window, Use the ping utility to ping the new EIP. If you successfully ping, it means the EIP was associated with your EC2 instance:

```bash
ping <Elastic_IP_Address>
```

*Reminder*: Use *Control-C* on Windows and on a Mac to stop the ping test.

#### Summary

In this Lab Step, you allocated an Elastic IP Address and associated it with your EC2 instance.
