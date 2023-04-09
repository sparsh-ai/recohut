# Azure Batch Example

# In this example, we will learn how to create an Azure Batch account and setup a pool of VMs to execute the job. 
# We will then learn how to run an application on the pool and download the results. Y

$resourceGroup = "<INSERT RESOURCE GROUP NAME>"
$storageAccount ="<INSERT STORAGE ACCOUNT NAME>"
$batchAccount ="<INSERT STORAGE ACCOUNT NAME>"

$appName = "sampleApp"
$poolName = "samplePool"
$jobName = "sampleJob"
$taskName= "sampleTask"
$region = "East US"

# Creat the Resource group if not already created
az group create --name $resourceGroup --location $region
#	Create a Batch Account as shown.
az batch account create -g $resourceGroup -n $batchAccount -l $region
#	Create a Storage account as shown.
az storage account create -g $resourceGroup -n $storageAccount -l $region --sku Standard_LRS
#	Now, link the storage account to the batch account.
az batch account set -g $resourceGroup -n $batchAccount --storage-account $storageAccount
#	Next, create a pool using Ubuntu VMs to run our Batch application. This operation takes a few minutes.
az batch pool create --id $poolName --vm-size Standard_A1_v2 --target-dedicated-nodes 2  --image canonical:ubuntuserver:18.04-LTS --node-agent-sku-id "batch.node.ubuntu 18.04"
#	You can check the status of the pool creation as shown.
az batch pool show --pool-id $poolName --query "allocationState"
#	Next, create an application that needs to be run by the Batch job.
az batch application create --resource-group $resourceGroup --name $batchAccount --application-name $appName
#	Next, create a Job 
az batch job create --id $jobName --pool-id $poolName 

#	Create the tasks under the job. The tasks will start running as soon as you create them.
for i in {1..4}
do
   az batch task create --task-id $taskName$i --job-id $jobName  --command-line "/bin/bash -c 'printenv; sleep 30s'"
done
#	Monitor the jobs as shown.
az batch task show --job-id $jobName --task-id $taskName

#	Download the results as shown.
az batch task file download --job-id $jobName --task-id $taskName --file-path stdout.txt --destination ./stdout.txt

#	Finally, you can delete each of the entities as shown:
az batch job delete --job-id $jobName
az batch task delete -job-id $jobName --task-id $taskName
az batch pool delete --pool-id $poolName