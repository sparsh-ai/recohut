# Setup Git

One of the major problems with coding is to keep track of changes. It is also almost impossible to maintain a program you have multiple versions of. Another is the topic of collaboration and documentation. Which is super Important. Let’s say you work on a Spark application and your colleges need to make changes while you are on holiday. Without some code management they are in huge trouble: Where is the code? What have you changed last? Where is the documentation? How do we mark what we have changed? But if you put your code on GitHub your colleges can find your code. They can understand it through your documentation (please also have in-line comments) Developers can pull your code, make a new branch and do the changes. After your holiday you can inspect what they have done and merge it with your original code. and you end up having only one application.

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