# Developer Foundations

## Anaconda

1. Download the file from https://www.anaconda.com/products/distribution and install it
2. Create Virtual Environment by executing this command in the terminal: `conda create -n env anaconda`. This will create a viirtual environment (venv) named `env` and install all the basic packages in that environment.

#### Makefile

```makefile
install:
	wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
	bash Anaconda3-2022.10-Linux-x86_64.sh
	source ~/.bashrc
	conda create -n env python=3.9.13 anaconda
	conda activate env
```

## Jupyter Notebook

There are many free options to run jupyter notebooks:

- Jupyter lab and Jupyter notebook - Anaconda also provide Jupyter lab and Jupyter notebook tools in local machine
- Google colab - https://colab.research.google.com
- Amazon SageMaker Studio Lab - https://studiolab.sagemaker.aws
- Databricks - For free community edition, use this: https://community.cloud.databricks.com
- Jupyter-try - https://jupyter.org/try
- VS Code Jupyter notebook - This can be accessed by installing `Jupyter` extension in VS code

#### Makefile

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

## Visual Studio Code (VS Code)

1. Follow [this](https://code.visualstudio.com/docs/setup/setup-overview) guide to install VS code in your system. Alternatively, go to https://code.visualstudio.com/download and download the VS Code
1. Install the following extensions
   1. [Python Extensions Pack](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   1. Office Viewer
1. [Optional] Git Multi-branch Environment Setup - You can setup a main/feature dual branch environment linked to two different folders in your system. I have seen that the git branch navigation is a bit confusing for begineers and until you gets familiar with it (~2-3 weeks), this multi-branch setup would be helpful.

#### :microscope: Lab: Explore VS Code features

In this lab, we will explore the following features:

- Left-panel icons - Explorer, Search & replace, Git, Extensions
- Primary Side bar
- Main window and tabs
- Top central bar - Search and commands, opening a file, changing theme
- Top right bar - Toggle feature
- Command bar - opening and closing terminals, starting multiple terminals
- Bottom bar - notifications

## Github

One of the major problems with coding is to keep track of changes. It is also almost impossible to maintain a program you have multiple versions of. Another is the topic of collaboration and documentation. Which is super Important. Let’s say you work on a Spark application and your colleges need to make changes while you are on holiday. Without some code management they are in huge trouble: Where is the code? What have you changed last? Where is the documentation? How do we mark what we have changed? But if you put your code on GitHub your colleges can find your code. They can understand it through your documentation (please also have in-line comments) Developers can pull your code, make a new branch and do the changes. After your holiday you can inspect what they have done and merge it with your original code. and you end up having only one application.

> :microscope: Lab: <a href="#/01-foundations/developer/lab-git-commands/" target="_blank">Learn git commands</a>

#### Setup

1. Create GitHub Account - https://www.youtube.com/embed/QUtk-Uuq9nE
1. Install git cli by downloading [Git SCM](https://git-scm.com/downloads) and install it
1. Setup Git Credentials - https://www.youtube.com/embed/WgZIv5HI44o
1. Connect local workspace to git repo
1. Add collaborators

#### Makefile

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

#### Git-sim `[Research]`

Install - `pip install git-sim`

Commands:

```bash
git-sim reset HEAD^
git-sim merge dev
git-sim --animate reset HEAD^
```

References - https://initialcommit.com/blog/git-sim

## Bash

In Mac/Linux, Bash comes pre-installed. And in Windows, git will also install bash terminal.

> :microscope: Lab: <a href="#/01-foundations/developer/lab-bash-commands/" target="_blank">Learn bash commands</a>

## DBeaver

Go to https://dbeaver.io/download to download DBeaver.

Follow https://youtu.be/NWTX0W-WgzE for more information.
