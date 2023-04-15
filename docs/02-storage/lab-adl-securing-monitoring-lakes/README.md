# Lab: Azure Data Lake - Securing and Monitoring

Data Lake forms the key storage layer for data engineering pipelines. Security and the monitoring of Data Lake accounts are key aspects of Data Lake maintenance. This lab will focus on configuring security controls such as firewalls, encryption, and creating private links to a Data Lake account. By the end of this lab, you will have learned how to configure a firewall, virtual network, and private link to secure the Data Lake, encrypt Data Lake using Azure Key Vault, and monitor key user actions in Data Lake.

We will be covering the following recipes in this lab:

- Configuring a firewall for an Azure Data Lake account using the Azure portal
- Configuring virtual networks for an Azure Data Lake account using the Azure portal
- Configuring private links for an Azure Data Lake account
- Configuring encryption using Azure Key Vault for Azure Data Lake
- Accessing Blob storage accounts using managed identities
- Creating an alert to monitor an Azure Data Lake account
- Securing an Azure Data Lake account with an SAS using PowerShell

## Recipe 1 - Configuring a firewall for an Azure Data Lake account using the Azure portal

Data Lake account access can be restricted to an IP or a range of IPs by whitelisting the allowed IPs in the storage account firewall. In this recipe, we'll learn to restrict access to a Data Lake account using a firewall.

To provide access to an IP or range of IPs, follow these steps:

1. On the storage account page, in the Security + Networking section, locate and select Firewalls and virtual networks
2. In the Selected networks option, scroll down to the Firewall section. To give access to your machine only, select the Add your client IP address option. To give access to a different IP or range of IPs, type in the IPs in the Address range section
3. To access storage accounts from Azure services such as Azure Data Factory and Azure Functions, check Allow Azure services on the trusted services list to access this storage account under the Exceptions heading
4. Click Save to save the configuration changes.

How it works…

Firewall settings are used to restrict access to an Azure storage account to an IP or range of IPs. Even if a storage account is public, it will only be accessible to the whitelisted IPs defined in the firewall configuration.

## Recipe 2 - Configuring virtual networks for an Azure Data Lake account using the Azure portal

A storage account can be public which is accessible to everyone, public with access to an IP or range of IPs, or private with access to selected virtual networks. In this recipe, we'll learn how to restrict access to an Azure storage account in a virtual network.

To restrict access to a virtual network, follow the given steps:

1. On the storage account page, in the Security + Network section, locate and select Firewalls and virtual networks | Selected networks
2. In the Virtual networks section, select + Add new virtual network
3. In the Create virtual network blade, provide the virtual network name, Address space details, and Subnet address range. The remainder of the configuration values are pre-filled
4. Click on Create to create the virtual network. This is created and listed in the Virtual Network section
5. Click Save to save the configuration changes

How it works…

We first created an Azure virtual network and then added it to the Azure storage account. Creating the Azure virtual network from the storage account page automatically fills in the resource group, location, and subscription information. The virtual network and the storage account should be in the same location.

The address space specifies the number of IP addresses in a given virtual network.

We also need to define the subnet within the virtual network that the storage account will belong to. We can also create a custom subnet. In our case, for the sake of simplicity, we have used the default subnet.

This allows the storage account to only be accessed by resources that belong to the given virtual network. The storage account is inaccessible to any network other than the specified virtual network.

## Recipe 3 - Configuring encryption using Azure Key Vault for Azure Data Lake

In this recipe, we will create a key vault and use it to encrypt an Azure Data Lake account.

Azure Data Lake accounts are encrypted at rest by default using Azure managed keys. However, you have the option of bringing your own key to encrypt an Azure Data Lake account. Using your own key gives better control over encryption.

Perform the following steps to add encryption to a Data Lake account using Azure Key Vault:

1. Log in to portal.azure.com, click on Create a resource, search for Key Vault, and click on Create. Provide the key vault details, Click on Review + Create
2. Go to the storage account to be encrypted. Search for Encryption on the left. Click on Encryption and select Customer-managed keys as the Encryption type. Click on Select a key vault and key at the bottom
3. On the new screen, Select a key, select Key vault as Key store type and select the newly created KeyVault as Key vault. Click on Create new key
4. Provide a name for the key to be used for encryption of the storage account. The default option, Generate, ensures that the key is generated automatically. Click on Create
5. Once the key is created, the screen automatically moves to the key vault selection page in the Blob storage, and the newly created key is selected as the key. Click on Select
6. The screen moves to the encryption page on the Blob storage page. Click on Save to complete the encryption configuration

How it works…

As the newly created key vault has been set for encryption on an Azure Data Lake account, all Data Lake operations (read, write, and metadata) will use the key from Key Vault to encrypt and decrypt the data in Data Lake. The encryption and decryption operations are fully transparent and have no impact on users' operations.

The Data Lake account automatically gets permissions on the key vault to extract the key and perform encryption on data. You can verify this by opening the key vault in the Azure portal and clicking on Access Policies. Note that the storage account has been granted Get, wrap, and unwrap permissions on the keys.

## Recipt 4 - Creating an alert to monitor an Azure storage account

We can create an alert on multiple available metrics to monitor an Azure storage account. To create an alert, we need to define the trigger condition and the action to be performed when the alert is triggered. In this recipe, we'll create an alert to send an email if the used capacity metrics for an Azure storage account exceed 5 MB. The used capacity threshold of 5 MB is not a standard and is deliberately kept low to explain the alert functionality.

Follow these steps to create an alert:

1. On the storage account page, search for alert and open Alerts in the Monitoring section
2. On the Alerts page, click on + New alert rule:
3. On the Alerts | Create alert rule page, observe that the storage account is listed by default in the Resource section. You can add multiple storage accounts in the same alert. Under the Condition section, click Add condition
4. On the Configure signal logic page, select Used capacity under Signal name
5. On the Configure signal logic page, under Alert logic, set Operator to Greater than, Aggregation type to Average, and configure the threshold to 5 MiB. We need to provide the value in bytes
6. Click Done to configure the trigger. The condition is added, and we'll be taken back to the Create alert rule page
7. The next step is to add an action to perform when the alert condition is reached. On the Create alert rule page, in the ACTIONS GROUPS section, click Create
8. On the Add action group page, provide the Action group name, Display name, and Resource group details
9. In Notifications, provide an email address. Click on Review + Create
10. Click on Create to create the action group. We are then taken back to the Create rule page. The Email action is listed in the Action Groups section.
11. The next step is to define the Severity, Alert rule name, and Alert rule description details
12. Click the Create alert rule button to create the alert.
13. The next step is to trigger the alert. To do that, download BigFile.csv from the data folder to the Azure storage account. The triggered alerts are listed on the Alerts page.
14. An email is sent to the email ID specified in the email action group.

How it works…

Setting up an alert is easy. At first, we need to define the alert condition (a trigger or signal). An alert condition defines the metrics and threshold that, when breached, trigger the alert. We can define more than one condition on multiple metrics for one alert.

We then need to define the action to be performed when the alert condition is reached. We can define more than one action for an alert. In our example, in addition to sending an email when the used capacity is more than 5 MB, we can configure Azure Automation to delete the old blobs/files in order to maintain the Azure storage capacity within 5 MB.

There are other signals, such as transactions, ingress, egress, availability, Success Server Latency, and Success E2E Latency, on which alerts can be defined. Detailed information on monitoring Azure storage is available at https://docs.microsoft.com/en-us/azure/storage/common/storage-monitoring-diagnosing-troubleshooting.

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/02-storage/lab-adl-securing-monitoring-lakes)

```
├── [9.9K]  README.md
├── [ 154]  data
│   └── [  58]  download.sh
└── [ 11K]  main.ipynb

  21K used in 1 directory, 3 files
```

## Notebook

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/02-storage/lab-adl-securing-monitoring-lakes/main.ipynb)
