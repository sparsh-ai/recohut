#!/bin/bash

# Run using ./setup.sh

if ! [ -d ./bin ];
then
    echo -e '\nCreating ~/bin directory\n'
    mkdir -p bin
fi

if ! [  -d ./bin/anaconda3 ]; then
    cd bin
    echo -e '\nInstalling anaconda3...\n'
    echo -e "Downloading anaconda3..."
    wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh -O ./Anaconda3-2021.11-Linux-x86_64.sh
    echo -e "Running anaconda3 script..."
    # -b run install in batch mode (without manual intervention), it is expected the license terms are agreed upon
    # -p install prefix, defaults to $PREFIX, must not contain spaces.
    bash ./Anaconda3-2021.11-Linux-x86_64.sh -b -p ~/bin/anaconda3

    echo -e "Removing anaconda installation script..."
    rm ./Anaconda3-2021.11-Linux-x86_64.sh

    #activate conda
    eval "$(/home/$USER/bin/anaconda3/bin/conda shell.bash hook)"

    echo -e "Running conda init..."
    conda init
    # Using -y flag to auto-approve
    echo -e "Running conda update..."
    conda update -y conda

    cd
else
    echo -e "anaconda already installed."
fi

echo -e "\nRunning sudo apt-get update...\n"
sudo apt-get update

echo -e "\nInstalling Docker...\n"
sudo apt-get -y install docker.io

echo -e "\nInstalling docker-compose...\n"
cd 
cd bin
wget https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-linux-x86_64 -O docker-compose
sudo chmod +x docker-compose


echo -e "\nInstalling Terraform...\n"
wget https://releases.hashicorp.com/terraform/1.1.4/terraform_1.1.4_linux_amd64.zip
sudo apt-get install unzip
unzip terraform_1.1.4_linux_amd64.zip
rm terraform_1.1.4_linux_amd64.zip

echo -e "\nInstalling java 11 jre...\n"
## jdk files and Variables
sudo apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless \
    && sudo apt-get autoremove -yqq --purge \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*
## Finish jdk files and Variables

echo -e "\nInstalling Spark with Hadoop...\n"
## Spark files and Variables
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
## Finish Spark files and Variables

echo -e "\nSetup .bashrc...\n"

echo -e '' >> ~/.bashrc
echo -e 'export PATH=${HOME}/bin:${PATH}' >> ~/.bashrc
echo -e '' >> ~/.bashrc
echo -e 'export GOOGLE_APPLICATION_CREDENTIALS="${HOME}/.google/credentials/google_credentials.json"' >> ~/.bashrc
echo -e '' >> ~/.bashrc
echo -e 'export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"' >> ~/.bashrc
echo -e 'export PATH="${JAVA_HOME}/bin:${PATH}"' >> ~/.bashrc
echo -e '' >> ~/.bashrc

echo -e 'export SPARK_VERSION=3.2.1' >> ~/.bashrc
echo -e 'export HADOOP_VERSION=3.2' >> ~/.bashrc
echo -e 'export SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}' >> ~/.bashrc
echo -e 'export PATH="${SPARK_HOME}/bin:${PATH}"' >> ~/.bashrc
echo -e '' >> ~/.bashrc
echo -e 'export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"' >> ~/.bashrc
echo -e 'export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.3-src.zip:$PYTHONPATH"' >> ~/.bashrc

# eval "$(cat ~/.bashrc | tail -n +10)" # A hack because source .bashrc doesn't work inside the script
# However, this eval hack does not work when executing ./setup.sh but works when executing . ./setup.sh (which means run script in current shell)
# So it is better just to use newgrp at the end of the script

terraform -version
sudo docker --version
docker-compose version
echo "anaconda-navigator version $(anaconda-navigator --version)"
anaconda --version
conda --version
java -version
${SPARK_HOME}/bin/spark-submit --version --version # Path var is not updated yet. 

echo -e "\nSetting up Docker without sudo setup...\n"
sudo groupadd docker 
sudo usermod -aG docker $USER  
newgrp docker
