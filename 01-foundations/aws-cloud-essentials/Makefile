install:
	pip install awscli

setup:
	aws configure

sts-identity:
	aws sts get-caller-identity

secret_manager_get_values:
	aws secretsmanager get-secret-value --secret-id wysde --query SecretString --output text

s3_create_bucket:
	TS=$(date +%s)
	aws s3api create-bucket --bucket <bucket-name>-$TS --region us-east-1

create_policy:
	aws iam create-policy --policy-name <policy-name> --policy-document file://<file-name>.json

create_role:
	aws iam create-role --role-name <role-name> --assume-role-policy-document file://role-trust.json

attach_policy_to_role:
	aws iam attach-role-policy --policy-arn <> --role-name <>

create-redshift-cluster:
# Use the following command to create a two-node dc2.large cluster with the minimal set of parameters of cluster-identifier (any unique identifier for the cluster), node-type/number-of-nodes and the master user credentials. Replace $MasterUserPassword in the following command with a password of your choice. The password must be 8-64 characters long and must contain at least one uppercase letter, one lowercase letter, and one number. You can use any printable ASCII character except /, "", or, or @:
	aws redshift create-cluster --node-type dc2.large --number-of-nodes 2 --master-username adminuser --master-user-password $MasterUserPassword --cluster-identifier myredshiftcluster
# It will take a few minutes to create the cluster. You can monitor the status of the cluster creation process using the following command:
	aws redshift describe-clusters --cluster-identifier myredshiftcluster
# Note that "ClusterStatus": "available" indicates that the cluster is ready for use and that you can connect to it using the "Address": "myredshiftcluster.abcdefghijk.eu-west-1.redshift.amazonaws.com" endpoint. The cluster is now ready. Now, you use an ODBC/JDBC to connect to the Amazon Redshift cluster.

