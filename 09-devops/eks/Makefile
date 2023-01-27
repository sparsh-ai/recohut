Installation-MacOS:
	aws sts get-caller-identity
	brew tap weaveworks/tap
	brew install weaveworks/tap/eksctl
	aws eks update-kubeconfig --region us-east-1 --name kubeflow-poc
# If your current user is different from the user/role used to create EKS, you will get the Unauthorized error. Follow this blog to easily resolve this issue: https://aws.amazon.com/premiumsupport/knowledge-center/eks-api-server-unauthorized-error/
Installation-Linux:
	curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
	sudo mv /tmp/eksctl /usr/local/bin
	eksctl create cluster --name my-cluster --region region-code
	export NODEGROUP_NAME=$(eksctl get nodegroups --cluster kubeflow-poc -o json | jq -r '.[0].Name')
	eksctl scale nodegroup --cluster kubeflow-poc --name $NODEGROUP_NAME --nodes 6 --nodes-max 6
	curl --silent --location "https://github.com/kubeflow/kfctl/releases/download/v1.0.1/kfctl_v1.0.1-0-gf3edb9b_linux.tar.gz" | tar xz -C /tmp
	sudo mv -v /tmp/kfctl /usr/local/bin
kf-install.sh:
	cat << EoF > 
	export AWS_CLUSTER_NAME=kubeflow-poc
	export KF_NAME=\${AWS_CLUSTER_NAME}

	export BASE_DIR=${HOME}/environment
	export KF_DIR=\${BASE_DIR}/\${KF_NAME}

	# export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws_cognito.v1.0.1.yaml"
	export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws.v1.0.1.yaml"

	export CONFIG_FILE=\${KF_DIR}/kfctl_aws.yaml
	EoF

	source kf-install.sh

	mkdir -p ${KF_DIR}
	cd ${KF_DIR}

	wget -O kfctl_aws.yaml $CONFIG_URI
# Reference: https://www.eksworkshop.com/advanced/420_kubeflow/install/
Install `kubectl`:
	sed -i '/region: us-east-1/ a \      enablePodIamPolicy: true' ${CONFIG_FILE}
	sed -i -e 's/kubeflow-aws/'"$AWS_CLUSTER_NAME"'/' ${CONFIG_FILE}
	sed -i "s@us-west-2@$AWS_REGION@" ${CONFIG_FILE}
	sed -i "s@roles:@#roles:@" ${CONFIG_FILE}
	sed -i "s@- eksctl-kubeflow-poc-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx@#- eksctl-kubeflow-poc-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx@" ${CONFIG_FILE}
	curl -o aws-iam-authenticator https://amazon-eks.s3.us-west-2.amazonaws.com/1.15.10/2020-02-22/bin/linux/amd64/aws-iam-authenticator
	chmod +x aws-iam-authenticator
	sudo mv aws-iam-authenticator /usr/local/bin
	cd ${KF_DIR}
	kfctl apply -V -f ${CONFIG_FILE}
	kubectl -n kubeflow get all
	kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
Deleting EKS:
	kubectl get svc --all-namespaces
	eksctl delete cluster --name kubeflow-poc