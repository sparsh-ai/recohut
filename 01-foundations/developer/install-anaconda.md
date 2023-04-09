# Install Anaconda

1. Download the file from https://www.anaconda.com/products/distribution and install it
2. Create Virtual Environment by executing this command in the terminal: `conda create -n env anaconda`. This will create a viirtual environment (venv) named `env` and install all the basic packages in that environment.

```makefile
install:
	wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
	bash Anaconda3-2022.10-Linux-x86_64.sh
	source ~/.bashrc
	conda create -n env python=3.9.13 anaconda
	conda activate env
```