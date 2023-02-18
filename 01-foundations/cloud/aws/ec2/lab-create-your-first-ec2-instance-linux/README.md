# Create Your First Amazon EC2 Instance (Linux)

## Description

Amazon Elastic Compute Cloud (EC2) is one of the most popular AWS services. EC2 allows you to launch different types of cloud instances and pay for them with a pay-per-use model. EC2 allows you to have operating system level control of your computing resources while running in Amazon's computing environment. Amazon EC2 reduces the time required to obtain and boot new server instances from days or weeks to minutes. This allows you to quickly scale capacity, both up and down, as your computing requirements change. Amazon EC2 allows you to build and configure your instances as you like, from your desired operating system to your applications.

![env drawio](https://user-images.githubusercontent.com/62965911/219856832-5dc3a360-cbb1-4ac2-9e01-6784fb46256b.svg)

By completing this Hands-on Lab, you will be able to launch and configure your first Amazon EC2 instance using the AWS Management Console.

## Lab Objectives

Upon completion of this lab, you will be able to:

- Configure and launch an instance in EC2
- Understand the Instance States and other critical instance information
- Generate and use a Secure Shell (SSH) public/private key pair
- Connect to a running Linux instance using an SSH client
- Extract metadata about your running instance
- Terminate an instance

## Lab Prerequisites

You should be familiar with:

- Conceptual understanding of EC2
- Conceptual understanding of SSH client software, protocol, and keys
- Some Linux shell/command understanding is helpful, but not required

## Steps

### Creating an EC2 Instance

- Click the **Launch instance** drop-down and click **Launch instance.** You will be directed to the Launch an instance wizard.
- In the **Name and tags** section, an optional name can be added that will create a tag that will have the key of **Name**. Additional tags can also be created here. Tags are specified as Key/Value pairs. They are not mandatory although it is useful to tag all of your AWS resources in production environments to stay organized. You can leave the tags empty for this lab.
- In the **Application and OS Images** section, select the **Amazon Linux** option under **Quick Start.**
- As you can see, Amazon provides many AMIs, including the most popular versions of Linux and Windows, often in 32-bit and 64-bit variants. Look at the supporting text to find out what other software packages and development languages are already installed on the image (such as Perl, Python, Java, etc.). You can think of AMIs as the blueprint or DNA of the instance you plan to launch.
- In the **Instance Type** section, you should not change any options. Simply make sure the default **t2.micro** is selected. For whatever Instance Type is selected, the **Currently selected** list provides a helpful summary of hardware resources (such as the CPU type, number of virtual CPUs, memory, and pricing).
- In the **Key pair** section, click on **Create new key pair**, enter *keypair* for the **Key pair name**, keep the default value for **Key pair type** and **Private key file format**, and click **Create key pair**. The key pair will begin downloading a file named keypair.pem on your local system. It contains a private key that you can use to connect to the EC2 instance via SSH. 
- In the **Network settings** section, read the supporting text under **Security groups (Firewall)**, and ensure the **Allow SSH traffic from** box is checked and **Anywhere** is selected.
- NOTE - The **Warning** from AWS is letting you know the default configuration for the security group that is about to be created will grant SSH access from any source IP address (0.0.0.0/0). Production environments should be more restrictive. For the purposes of this lab, this configuration is fine.
- TIP - A handy feature for testing purposes is to select **My IP** from the **Source** drop-down. That will restrict SSH access to only your current IP address. In network environments with Dynamic Host Configuration Protocol (DHCP), multiple routers or firewalls, and other features that make IP addresses subject to change, this setting is not a permanent security feature. However, it is sometimes a helpful feature while you perform various tests using your EC2 instance.
- In the **Configure storage** section, ensure the default values of **8 GiB** and **gp2 Root volume** is selected. The default values work fine here. There is no need to add additional volumes, encrypt volumes, or change any other settings. Simply note this is where you can change storage settings if needed.
- Click on **Advanced details** to expand the section and take a minute to look over the various configurations. 
- You can configure many different options on this page of the wizard, but it's best to keep your first launch simple. Skim the different fields, but leave the default values. If you are particularly interested in any particular field, hover over the **i** information icon next to it for a basic description.  The information icon is a useful feature for easing your learning curve while using the AWS Console. In many cases, the help text also includes a link to related documentation. To summarize a few key points:
  - You will launch a single instance
  - The EC2 service will launch the instance into one of several subnets in the US West (Oregon) region
- Review the **Summary** section, and click **Launch instance** when ready. A confirmation page will let you know that your instance is launching.
- Click the **View all instances** (lower right) to close the confirmation page and return to the **Instances** screen of the EC2 console.
- You can view the status of your instance on the **Instances** screen of the EC2 console:

![image-20220531143919-16-b15f4d18-4066-4145-ace4-2c3cd5b370f0](https://user-images.githubusercontent.com/62965911/219857222-a0a49d1c-e90a-4d74-b186-32c440e01fa3.png)

*Warning*: If you see the error compute-optimizer:GetEnrollmentStatus, just ignore it, it doesn't prevent the lab from working.

The **Details** tab contains a wealth of information on your instance. When you launch an instance, its initial **Instance state** defaults to Pending. After the instance starts, its **Instance state** transitions to Running, and it receives a Public IPv4 address and **Public IPv4 DNS** name. It typically takes about 30 seconds for the AWS Linux instance to transition to a running state.

Congratulations...you just launched your first EC2 instance!

**Summary**

In this lab step, you launched an EC2 instance. You learned key areas of configuration for your EC2 instance using the Launch Instance wizard. Although many configuration options were left at their default values, you should have a pretty good understanding of the type of configuration options available to you within the wizard. Now that you have a running instance, you can treat it as any other Linux host. That is, you can connect to it, install and configure software, develop applications, and other tasks. You also learned how to generate your own SSH key pair for connecting to a running Linux instance. It is important to learn the mechanics behind accomplishing this.

### Converting a PEM Key to a PPK Key (Windows Users Only)

*Note: This step is only required for Windows users. If you are using Mac or Linux you can directly use the PEM file you downloaded. Proceed to the next lab step if you are running Mac or Linux.*

Connecting to a running Linux instance using an SSH client requires a public/private key pair. Windows does not ship with an SSH client. PuTTY is a common SSH client, which is free to download and use. However, PuTTY does not support the PEM (Privacy Enhanced Mail) key format. The key downloaded from AWS is PEM format, so it must be converted to PPK (PuTTY Private Key). Fortunately, PuTTYgen converts PEM key files to PPK format. PuTTYgen is also free to download and use.

**Instructions**

1\. If you do not already have PuTTYgen, download the PuTTYgen executable from the following link: [PuTTYgen](https://the.earth.li/~sgtatham/putty/latest/w32/puttygen.exe "PuTTYgen").

2\. Start PuTTYgen. (no installation is required)

3\. Click **Load** and browse to the location of the private key file that you want to convert (for example keypair.pem). By default, PuTTYgen displays only files with a .ppk extension. You'll need to change the drop-down adjacent to **File name** to **All Files** in order to see your PEM file.

4\. Select your .pem key file and click **Open**. PuTTYgen displays the success message.

5\. Click **OK**. PuTTYgen displays a dialog with information about the key you loaded, including the public key and the fingerprint.

6\. Click **Save private key** to save the key in PuTTY's format. Do NOT select a passphrase. (Additional security is not required.) Be sure to save your private key somewhere secure.

**Summary**

Now you are ready to use PuTTY for connecting to the running Linux instance created in a previous lab step. The PuTTY SSH client will use the key pair format it requires for the private key to connect to the instance. The running Linux instance already has the public key on it.

### Connecting to an Instance using SSH

In order to manage a remote Linux server, you must employ an SSH client. Secure Shell (SSH) is a cryptographic network protocol for securing data communication. It establishes a secure channel over an insecure network. Common applications include remote command-line login and remote command execution.

Linux distributions and macOS ship with a functional SSH client that accepts standard PEM keys. Windows does not ship with an SSH client. Therefore, this lab step includes instructions for users running Linux/macOS *and* Windows on their local host. Only one of them is required depending on your local operating system.

**Instructions (Linux / macOS Users)**

Open your Terminal application and Run the following ssh command:

```sh
ssh -i /*path/to/your/keypair.pem* user@server-ip
```

- `server-ip` is the Public IP of your server, found on the **Details** tab of the running instance in the EC2 Console
- `user` is the remote system user (ec2-user for Amazon Linux) that will be used for the remote authentication. In this lab, you must use **ec2-user**.

Note that the Amazon Linux AMIs typically use `ec2-user` as a username. Other popular Linux distributions use the following user names:

- Debian: admin
- RedHat: ec2-user
- Ubuntu: ubuntu

Assuming that you selected the Amazon Linux AMI, your assigned public IP is 123.123.123.123, and your keypair (named "keypair.pem") is stored in /home/youruser/keypair.pem, the example command to run is: 

```sh
ssh -i /home/youruser/keypair.pem <ec2-user@123.123.123.123>
```

*Note*: You can find the Public IP under the AWS EC2 console, and choosing the available EC2 instance.

***Important!** Your SSH client may refuse to start the connection, warning that the key file is unprotected. You should deny the file access to any other system users by changing its permissions. From the directory where the public key is stored on your local machine, issue the following command and then try again:

```sh
chmod 400  /home/youruser/keypair.pem
```

The change mode (`chmod`) command shown above will change the permissions on your private key file so only you can read it. No other users on the system can modify it, or even read it.

**Instructions (Windows Users)**

Windows has no SSH client, so you must install one. This part of the lab step will use PuTTY (freely available [here](http://www.putty.org/) on their website) and a previously converted PEM key (converted to PPK using PuTTYgen).

- Open PuTTY and insert the EC2 instance public IP Address in the **Host Name** field.

*Note*: You can find the Public IP under the AWS EC2 console, and choosing the available EC2 instance.

- Navigate to **Connection **>** SSH **>** Auth **>** Credentials** in the left pane, click **Browse...** under **Private key file for authentication**, double-click the PPK file you created with PuTTYgen, and click **Open.**

After a few seconds, you will see the authentication form.

3\. Login as *ec2-user* and you will see the EC2 server welcome banner and be placed in the Linux shell.

### Getting the EC2 Instance Metadata

Now you are ready to send the first commands to your EC2 Linux instance. In this lab step, you will check the EC2 instance metadata, which is only available from within the instance itself. Instance metadata is data about your instance that you can use to configure or manage the running instance. In order to obtain the instance metadata you will use the curl utility. cURL (Client URL) is a free, open-source project, and already loaded on your instance. cURL is a great way to transfer data using one of its supported protocols (such as HTTP).

*Note*: The IP address used below (169.254.169.254) is a special use address to return metadata information tied to EC2 instances.

- List all instance metadata by issuing the following command:

```sh
curl -w "\n" http://169.254.169.254/latest/meta-data/
```

To extract specific metadata append keywords to the end of the http path URL provided in the curl request. For example, you can easily check the list of security groups attached to the instance, its ID, the hostname, or the AMI ID. The "-w" command-line option tells curl to write the output to standard output (STDOUT).

- Enter the following commands to extract specific metadata associated with your running instance: 

```sh
curl -w "\n" http://169.254.169.254/latest/meta-data/security-groups
curl -w "\n" http://169.254.169.254/latest/meta-data/ami-id
curl -w "\n" http://169.254.169.254/latest/meta-data/hostname
curl -w "\n" http://169.254.169.254/latest/meta-data/instance-id
curl -w "\n" http://169.254.169.254/latest/meta-data/instance-type
```

- Enter the following command to get the public SSH key of the attached key pair using the public-keys metadata:

```sh
curl -w "\n" http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
```

**Summary **

In this lab step, you learned how you can obtain instance metadata. This metadata can be extremely useful if you want to automate the setup of new instances.

### Terminating an EC2 Instance

AWS bills EC2 usage per second in most cases. It's good to learn how to stop or terminate an instance from the AWS console. When you are sure that you no longer need an instance, you can terminate it. The specific instance and the data on the root volume (system disk) is not recoverable (by default) however. So be sure you don't need it before terminating an instance. If you stop an instance, you can start it again later (and access data on all the disks). In this lab step, you will terminate a running EC2 instance.

1\. Return to the EC2 console in your browser.

2\. Click **Instances** in the left navigation pane. Select the running instance, then click the dropdown menu at the top middle of the page **Instance State > Terminate instance.**

3\. Read the **Warning** from AWS, then click the **Terminate** button in the **Terminate Instances** confirmation dialog.

 4. Watch as the **Instance State** transitions from **running** to **shutting-down** and finally to **terminated.**

Your instance and the data stored on its root volume are completely destroyed. 

**Summary**

In this lab step, you terminated your running EC2 Linux instance. Any open connections to the instance were severed.  You learned more about the state of your instance as it transitions, along with the main difference between stopping and terminating an instance.
