# Setup VM on GCP

- [Setup VM on GCP](#setup-vm-on-gcp)
  - [SSH Keys creation](#ssh-keys-creation)
  - [VM instance creation](#vm-instance-creation)
  - [Creation of config file for SSH connection through Visual Studio Code](#creation-of-config-file-for-ssh-connection-through-visual-studio-code)
  - [Setup Visual Studio Code in local machine to use the VM machine](#setup-visual-studio-code-in-local-machine-to-use-the-vm-machine)
  - [GCP SDK credentials](#gcp-sdk-credentials)
  - [Option A: Install all applications automatically](#option-a-install-all-applications-automatically)
    - [Clone repo in vm instance](#clone-repo-in-vm-instance)
    - [Execute setup_vm.sh script](#execute-setup_vmsh-script)
  - [Option B: Install applications manually](#option-b-install-applications-manually)
    - [Remote access to VM instance](#remote-access-to-vm-instance)
    - [Download and install Anaconda for Linux in the vm instance](#download-and-install-anaconda-for-linux-in-the-vm-instance)
    - [Install docker](#install-docker)
    - [Setup docker to be run without sudo](#setup-docker-to-be-run-without-sudo)
    - [Install docker compose](#install-docker-compose)
    - [Install Terraform](#install-terraform)
    - [Install JDK](#install-jdk)
    - [Install Spark with Hadoop](#install-spark-with-hadoop)
    - [Update .bashrc with env vars](#update-bashrc-with-env-vars)
  - [GCP authentication](#gcp-authentication)


## SSH Keys creation

Check https://cloud.google.com/compute/docs/connect/create-ssh-keys . 
More specifically,
- Linux and macOS: https://cloud.google.com/compute/docs/connect/create-ssh-keys#linux-and-macos 
- Windows: https://cloud.google.com/compute/docs/connect/create-ssh-keys#windows-10-or-later

If you have gitbash, ssh-keygen command is supported. 
- Create .ssh folder under user folder 
  - Windows: C:\USERS\YOUR_USER_NAME
  - Linux: ~
- Run the command: 

  - Linux/gitbash  `ssh-keygen -t rsa -f ~/.ssh/YOUR_USER_NAME -C YOUR_USER_NAME -b 2048`
  - Windows `ssh-keygen -t rsa -f C:\USERS\YOUR_USER_NAME\.ssh\KEY_FILENAME -C YOUR_USER_NAME -b 2048`

This will generate public and private keys.
Go to Compute Engine: https://console.cloud.google.com/compute and add the public key (KEY_FILENAME.pub).
`GCP->Compute Engine->Metadata->ssh-keys->Add key`

## VM instance creation

`GCP->Compute Engine->VM instances->Create instance`
`e2-standard-4`
`Ubuntu 20.14LTS 30GB`

It is convenient to give it a name


## Creation of config file for SSH connection through Visual Studio Code

Create the config file under ~\.ssh folder (Modify the path file according to your OS):
Name of file: "config"
Contents:
    Host de-zoomcamp (name of the host/vm)
    
        Hostname 35.240.98.123 (external ip)
        User YOUR_USER_NAME
        IdentityFile c:/Users/YOUR_USER_NAME/.ssh/gcp


## Setup Visual Studio Code in local machine to use the VM machine

Download and install Visual Studio Code if needed. https://code.visualstudio.com/download
Install `Remote - SSH` extension in VSC  
  Clic on Extensions icon on the left and type `Remote - SSH` in the seach box. Install it.
Click on green button in left-bottom corner. Connect to host. de-zoomcamp is listed because config file is opened.  
Open remote folder to have access to all repository files.  
Setup VSC to port forward so that we can interact with remote services.  
CTRL+T to see terminal  
  Ports tab. Add Port. 8080 to localhost:8080  
You will have terminal opened already to continue performing commands instead of using external bash  

## GCP SDK credentials

GCP SDK is already installed in the VM. 

    gcloud --version:
    
    Google Cloud SDK 368.0.0
    alpha 2022.01.07
    beta 2022.01.07
    bq 2.0.72
    core 2022.01.07
    gsutil 5.6 
    minikube 1.24.0
    skaffold 1.35.1 

Create a folder `.google/credentials` under the `${HOME}`directory and upload the json file with the credentials generated through Google Cloud when creating the service account.  
If you use Visual Studio Code, just drag and drop the file.  
Example: `${HOME}/.google/credentials/google_credentials.json`  


## Option A: Install all applications automatically

### Clone repo in vm instance

Go to the home directory  
`cd`  

In github, fork the following repository, this will copy the repository in your github account:  
    https://github.com/MarcosMJD/ghcn-d.git  

Then, in the vm, clone the forked project repository:  
`git clone https://github.com/YOUR_GIT_USERNAME/ghcn-d.git`  

### Execute setup_vm.sh script
 Run  
  `cd ghcn-d`  
  `./setup_vm.sh`

Go to final step: [GCP authentication](#gcp-authentication)


## Option B: Install applications manually


### Remote access to VM instance  

You can use Visual Studio Code as explained above.  
In case you do not have it, you can use git bash, Windows command or similar. Change the path accordingly.

  `ssh -i /.ssh/gcp username@externalipofmachine` (you can find the external ip of the VM in Google Cloud Console)
  username is the name of the user used when creating the ssh key

 
### Download and install Anaconda for Linux in the vm instance

    mkdir bin
    cd bin
    wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
    bash Anaconda3-2021.11-Linux-x86_64.sh
      After installation choose yes to initialize Anaconda (adds some stuff in .bashrc to be executed each time user is logged in)
    type `source .bashrc` to login again and activate base environment

### Install docker

    sudo apt-get update (to fetch the list of packages)
    sudo apt-get install docker.io

### Setup docker to be run without sudo
    sudo groupadd docker  
    sudo usermod -aG docker $USER  
    newgrp docker  
    Test with `docker run hello-world` 
    
  If this method does not work, use:  

    sudo groupadd docker
    sudo gpasswd -a $USER docker
    sudo service docker restart
    source .bashrc
    Test with `docker run hello-world`  

### Install docker compose

https://github.com/docker/compose/releases  
https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64  
    mkdir bin  
    cd bin  
    wget https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -O docker-compose  
    chmod +x docker-compose  
Test with `./docker-compose version`  


### Install Terraform

Download the binary to the /bin directory  
    wget https://releases.hashicorp.com/terraform/1.1.4/terraform_1.1.4_linux_amd64.zip  
    cd /bin  
    sudo apt-get install unzip  
    unzip terraform_1.1.4_linux_amd64.zip  
    chmod +x terraform
    ./terraform -version  

### Install JDK

    sudo apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless \
    && sudo apt-get autoremove -yqq --purge \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*

### Install Spark with Hadoop

    cd 
    cd bin
    SPARK_VERSION=3.2.1
    HADOOP_VERSION=3.2
    SPARK_HOME="/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}"
    SPARK_BIN="spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"
    wget "https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/${SPARK_BIN}" -O "${SPARK_BIN}" \
        && sudo mkdir -p "${SPARK_HOME}" \
        && sudo tar xzf ${SPARK_BIN} -C "${SPARK_HOME}" --strip-components=1 \
        && rm ${SPARK_BIN}
    cd

### Update .bashrc with env vars

    cd  
    nano .bashrc to edit .bashrc or you can also use Visual Studio Code.
    Add the following:
    export PATH="${HOME}/bin:${PATH}"  
    export GOOGLE_APPLICATION_CREDENTIALS="${HOME}/.google/credentials/google_credentials.json"
    export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
    export PATH="${JAVA_HOME}/bin:${PATH}"
    export SPARK_VERSION=3.2.1
    export HADOOP_VERSION=3.2
    export SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}' 
    export PATH="${SPARK_HOME}/bin:${PATH}"
    export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
    export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.3-src.zip:$PYTHONPATH"

    Ctrl+O to save  
    Ctrl+x to exit  
    source .bashrc to execute .bashrc without having to logout and login again (reopen an interactive session)

Continue with GCP authentication

## GCP authentication

Perform de authentication:  

`gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS`  





