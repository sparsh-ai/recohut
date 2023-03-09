# Developer Foundations

## Objective

Learn the processes you need to know, and the tools you need to have as a developer

## Anaconda

### Setup

1. Download from https://www.anaconda.com/products/distribution.
2. Install the downloaded package

### Create Virtual Environment

Open terminal and write:

```bash
conda create -n env anaconda
```

This command will create a viirtual environment (venv) named `env` and install all the basic packages in that environment.

### Makefile

```makefile
install:
	wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
	bash Anaconda3-2022.10-Linux-x86_64.sh
	source ~/.bashrc
	conda create -n env python=3.9.13 anaconda
	conda activate env
```

## Jupyter Notebooks

### Alternatives

- Anaconda Jupyter Notebooks - Here we install Anaconda IDE and it provides acceess to Jupyter lab and Jupyter notebooks in local machine
- Google Colab - https://colab.research.google.com/
- Amazon SageMaker Studio Lab - https://studiolab.sagemaker.aws
- Databricks - For free community edition, use this: https://community.cloud.databricks.com
- Jupyter-try - https://jupyter.org/try
- VS Code Jupyter notebook - This can be accessed by installing `Jupyter` extension in VS code
- Amazon SageMaker Studio - This is a paid tool

### Makefile

```makefile
writefile_custom:
# The existing writefile magic command do not allow passing variables, so this custom magic will help in passing the variables also while writing something from IPython notebooks into a file.
	#!/usr/bin/python
	from IPython.core.magic import register_line_cell_magic
	@register_line_cell_magic
	def writefile(line, cell):
		with open(line, 'w') as f:
			f.write(cell.format(**globals()))

sql_config:
	%config SqlMagic.autopandas=True
	%config SqlMagic.displaycon=False
	%config SqlMagic.feedback=False
	%config SqlMagic.displaylimit=5
	%reload_ext sql

watermark:
	%reload_ext watermark
	%watermark -a "Sparsh A." -m -iv -u -t -d
```

## Visual Studio Code

### Install

Follow [this](https://code.visualstudio.com/docs/setup/setup-overview) guide to install VS code in your system.

### Extensions

Once the VS code is installed, also install [this](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension.

* [ ] Python Extensions Pack
* [ ] Office Viewer

### Understanding VSCode Features

* [ ] Left-panel icons - Explorer, Search & replace, Git, Extensions
* [ ] Primary Side bar
* [ ] Main window and tabs
* [ ] Top central bar - Search and commands, opening a file, changing theme
* [ ] Top right bar - Toggle feature
* [ ] Command bar - opening and closing terminals, starting multiple terminals
* [ ] Bottom bar - notifications

### Optional: Git Multi-branch Environment Setup

You can setup a main/feature dual branch environment linked to two different folders in your system. I have seen that the git branch navigation is a bit confusing for begineers and until you gets familiar with it (~2-3 weeks), this multi-branch setup would be helpful.

## Github

Why this is important: One of the major problems with coding is to keep track of changes. It is also almost impossible to maintain a program you have multiple versions of. Another is the topic of collaboration and documentation. Which is super Important. Let’s say you work on a Spark application and your colleges need to make changes while you are on holiday. Without some code management they are in huge trouble: Where is the code? What have you changed last? Where is the documentation? How do we mark what we have changed? But if you put your code on GitHub your colleges can find your code. They can understand it through your documentation (please also have in-line comments) Developers can pull your code, make a new branch and do the changes. After your holiday you can inspect what they have done and merge it with your original code. and you end up having only one application.

### Setup

1. Download [Git SCM](https://git-scm.com/downloads)
2. Install the downloaded file
3. Create GitHub Account - https://www.youtube.com/embed/QUtk-Uuq9nE
4. Setup Git Credentials - https://www.youtube.com/embed/WgZIv5HI44o

### Git commands

![atlassian-git-cheatsheet-1](https://user-images.githubusercontent.com/62965911/212006609-a871bf80-a26e-4ab6-996b-eaab0a14f5b4.png)

![atlassian-git-cheatsheet-2](https://user-images.githubusercontent.com/62965911/212006617-88e6eb6b-b6d3-4a25-8827-4cfa0ab63d41.png)

### Makefile

```makefile
general:
	git init
	git remote add origin https://github.com/datalaker/de
	git checkout -b main
	git add .
	git commit -m "commit"
	git pull --rebase origin main
	git push origin main
ssh-connect:
	ssh-keygen -t rsa -b 4096 -C "<email>"
	eval $(ssh-agent -s)
	ssh-add ~/.ssh/id_rsa
	cat ~/.ssh/id_rsa.pub
```

### Git-sim `[Research]`

Install - `pip install git-sim`

Commands:

```bash
git-sim reset HEAD^
git-sim merge dev
git-sim --animate reset HEAD^
```

References - https://initialcommit.com/blog/git-sim

## DBeaver

### Setup

Watch and follow this video: https://youtu.be/NWTX0W-WgzE

## Labs

1. Visual Studio Code (vscode)
   1. Download and Install vscode
   2. Understand vscode features
   3. Install extensions in vscode
3. Anaconda
   1. Download and Install Anaconda
   2. Create virtual environment in anaconda
   3. Create jupyter notebook in vscode and connect to venv
4. Github
   1. Create github account
   2. Install git cli
   3. Create git repo and add students as collaborator
   4. Connect local workspace to git repo
5. [Learn git command](01-foundations/developer/lab-git-basics/)
6. [Learn bash command](01-foundations/developer/lab-bash/)
7. Download and Install DBeaver

## Note for Windows users

1. Go to https://code.visualstudio.com/download and click on Windows icon to download the VS Code
2. Install the VS Code by following instructions
3. Go to https://git-scm.com/download/win and click on the Windows installer to download git
4. Install the git by following instructions
5. Bash - Git will also install the Bash shell
6. Go to https://www.anaconda.com/products/distribution and click on the download button
7. Install the Anaconda by following instructions
8. Go to https://dbeaver.io/download and click on Windows installer to download DBeaver
9. Install the DBeaver by following instructions
