# Lab: Configuring and Securing Azure SQL Database

Azure SQL Database, a fundamental relational database as a service offered in Azure, acts as a source, destination, or even as an intermediate storage layer in data engineering pipelines. Azure SQL Database can be used to consolidate data coming from several relational data sources and build mini data warehouses or data marts. With the introduction of Hyperscale tier in Azure SQL Database, the capacity of Azure SQL Database has increased leaps and bounds too. Securing Azure SQL Database is also pivotal in protecting access to the database. Having a strong understanding of Azure SQL Database's capabilities and security options is essential for any data engineer.

In this lab, we will learn how to provision a serverless Azure SQL database, secure its connectivity to private links, integrate with Azure Key Vault to secure its credentials, configure a wake-up script to start a serverless Azure SQL database, and also configure the Hyperscale tier of Azure SQL Database.

In this lab, we'll cover the following recipes:

- Provisioning and connecting to an Azure SQL database using PowerShell
- Implementing an Azure SQL Database elastic pool using PowerShell
- Configuring a virtual network and private endpoints for Azure SQL Database
- Configuring Azure Key Vault for Azure SQL Database
- Provisioning and configuring a wake-up script for a serverless SQL database
- Configuring the Hyperscale tier of Azure SQL Database

## Recipe 1 - Provisioning and connecting to an Azure SQL database using PowerShell

In this recipe, we’ll learn how to create and connect to an Azure SQL database instance. Azure SQL Database comes in three flavors: standalone Azure SQL Database, Azure SQL Database elastic pools, and managed instances. In this recipe, we’ll create a standalone Azure SQL database.

Execute the following steps to provision an Azure SQL database:

1. Execute the following PowerShell command to create a new resource group:

   ```powershell
   New-AzResourceGroup -Name sparsh-resource-1 -Location "eastus"
   ```
2. Execute the following command to create a new Azure SQL server:

   ```powershell
   #create credential object for the Azure SQL Server admin credential
   $sqladminpassword = ConvertTo-SecureString 'Sql@Server@1234' -AsPlainText -Force
   $sqladmincredential = New-Object System.Management.Automation.PSCredential('sqladmin', $sqladminpassword)

   # create the Azure SQL Server
   New-AzSqlServer -ServerName azadesqlserver -SqlAdministratorCredentials $sqladmincredential -ResourceGroupName sparsh-resource-1 -Location "eastus"
   ```
3. Execute the following command to create a new Azure SQL database:

   ```powershell
   New-AzSqlDatabase -DatabaseName azadesqldb -Edition basic -ServerName azadesqlserver -ResourceGroupName sparsh-resource-1
   ```
4. To connect to an Azure SQL database, let’s first whitelist the IP address in the Azure SQL Server firewall. Execute the following command to whitelist the public IP address of the machine to connect to an Azure SQL database (this recipe assumes that you are connecting from your local system. To connect from a system other than your local system, change the IP address in the following command). Execute the following command in the PowerShell window to whitelist the machine’s public IP address in the Azure SQL Server firewall:

   ```powershell
   $clientip = (Invoke-RestMethod -Uri https://ipinfo.io/json).ip

   New-AzSqlServerFirewallRule -FirewallRuleName "home" -StartIpAddress $clientip -EndIpAddress $clientip -ServerName azadesqlserver -ResourceGroupName sparsh-resource-1
   ```
5. Execute the following command to connect to an Azure SQL database from SQLCMD (SQLCMD comes with the SQL Server installation, or you can download the SQLCMD utility from https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-ver15):

   ```powershell
   sqlcmd -S "azadesqlserver.database.windows.net" -U sqladmin -P "Sql@Server@1234" -d azadesqldb -Q "Select name from sys.databases"
   ```

How it works…

We first execute the New-AzSQLServer command to provision a new Azure SQL Server. The command accepts the server name, location, resource group, and login credentials.

An Azure SQL Server, unlike an on-premises SQL Server, is not a physical machine or a virtual machine (VM) that is accessible to customers.

We then execute the New-AzSQLDatabase command to create an Azure SQL database. This command accepts the database name, the Azure SQL Server name, the resource group, and the edition. There are multiple SQL database editions to choose from based on the application workload. However, for the sake of this demo, we will create a basic edition.

To connect to an Azure SQL database, we first need to whitelist the machine’s IP address in the Azure SQL Server firewall. Only whitelisted IPs are allowed to connect to the database.

To whitelist the client’s public IP, we use the New-AzSQLServerFirewallRule command. This command accepts the server name, resource group, and start and end IPs. We can whitelist either a single IP address or a range of IP addresses.

We can connect to an Azure SQL database from SQL Server Management Studio (SSMS), SQLCMD, or Azure Data Studio, or with a programming language using the appropriate SQL Server drivers. When connecting to an Azure SQL database, we need to specify the server name as azuresqlservername.database.windows.net, and then specify the Azure SQL database to connect to.

## Recipe 2 - Implementing an Azure SQL Database elastic pool using PowerShell

An elastic pool is a cost-effective mechanism to group single Azure SQL databases with varying peak usage times. For example, consider 20 different SQL databases with varying usage patterns, each S3 Standard storage class requiring 100 database throughput units (DTUs) to run. We need to pay for 100 DTUs separately. However, we can group all of them in an elastic pool of S3 Standard storage classes. In this case, we only need to pay for elastic pool pricing and not for each individual SQL database.

In this recipe, we’ll create an elastic pool of multiple single Azure databases.

1. Create the Azure SQL Server
   ```powershell
   New-AzSqlServer -ServerName azadesqlserver -SqlAdministratorCredentials $sqladmincredential -Location "eastus" -ResourceGroupName sparshadesql

   #Execute the following query to create an elastic pool.
   New-AzSqlElasticPool -ElasticPoolName adepool -ServerName azadesqlserver -Edition standard -Dtu 100 -DatabaseDtuMin 20 -DatabaseDtuMax 100 -ResourceGroupName sparshadesql
   ```
2. Execute the following query to create and add an Azure SQL database to an elastic pool
   ```powershell
   New-AzSqlDatabase -DatabaseName azadedb1 -ElasticPoolName adepool -ServerName azadesqlserver -ResourceGroupName sparshadesql
   ```
3. Execute the following query to create a new Azure SQL database outside of the elastic pool
   ```powershell
   New-AzSqlDatabase -DatabaseName azadedb2 -Edition Standard -RequestedServiceObjectiveName S3 -ServerName azadesqlserver -ResourceGroupName sparshadesql
   ```
4. Execute the following query to add the azadedb2 database created in the preceding step to the elastic pool:
   ```powershell
   $db = Get-AzSqlDatabase -DatabaseName azadedb2 -ServerName azadesqlserver -ResourceGroupName sparshadesql
   $db | Set-AzSqlDatabase -ElasticPoolName adepool
   ```
5. To verify this in the Azure portal, log in with your Azure account. Navigate to All resources | azadesqlserver | SQL elastic pools | adepool | Configure and click on the Databases tab.
6. Execute the following command to remove an Azure SQL database from an elastic pool. To move a database out of an elastic pool, we need to set the edition and the service objective explicitly:
   ```powershell
   $db = Get-AzSqlDatabase -DatabaseName azadedb2 -ServerName azadesqlserver -ResourceGroupName sparshadesql
   $db | Set-AzSqlDatabase -Edition Standard -RequestedServiceObjectiveName S3
   ```
7. Execute the following command to remove an elastic pool. An elastic pool has to be empty before it can be removed. Execute the following query to remove all the databases in an elastic pool:
   ```powershell
   # get elastic pool object
   $epool = Get-AzSqlElasticPool -ElasticPoolName adepool -ServerName azadesqlserver -ResourceGroupName sparshadesql

   # get all databases in an elastic pool
   $epdbs = $epool | Get-AzSqlElasticPoolDatabase

   # change the edition of all databases in an elastic pool to standard S3
   foreach($db in $epdbs) {
   $db | Set-AzSqlDatabase -Edition Standard -RequestedServiceObjectiveName S3
   }

   # Remove an elastic pool
   $epool | Remove-AzSqlElasticPool
   ```

NOTE

The command sets the edition of the SQL databases to Standard. This is for demo purposes only. If this is to be done in production, modify the edition and the service objective accordingly.

How it works…

We create an elastic pool using the New-AzSqlElasticPool command. In addition to the parameters, such as the server name, resource group name, compute model, compute generation, and edition, which are the same as when we created a new Azure SQL database, we can also specify DatabaseMinDtu and DatabaseMaxDtu. DatabaseMinDtu specifies the minimum amount of DTUs that all the databases in an elastic pool can have. DatabaseMaxDtu is the maximum amount of DTUs that a database can consume in an elastic pool.

Similarly, for the vCore-based purchasing model, we can specify DatabaseVCoreMin and DatabaseVCoreMax.

To add a new database to an elastic pool, specify the elastic pool name at the time of database creation using the New-AzSqlDatabase command.

To add an existing database to an elastic pool, modify the database using Set-AzSqlDatabase to specify the elastic pool name.

To remove a database from an elastic pool, modify the database using the Set-AzSqlDatabase command to specify a database edition explicitly.

To remove an elastic pool, first, empty it by moving all of the databases out of the elastic pool, and then remove it using the Remove-AzSqlElasticPool command.

## Notebook

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/02-storage/lab-azure-sql-securing-databases/main.ipynb)