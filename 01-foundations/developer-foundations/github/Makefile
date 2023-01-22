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