<<<<<<< HEAD

# Welcome to Producer CDK Python project!

CDK app  (`producer_cdk_stack`) deploys infrastructure needed to run Producer App code on EC2 instance.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  

Make sure CDK is intalled 

```
$npm install -g aws-cdk
```

Create Pyhton Virtual environment

```
$pyhton3 -m venv .venv
```

Activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can deploy Producer Infrastructure using command like one below (change parameter values for S3 buckets they are globaly unique):

```
$ cdk deploy --parameters kdasrcbucketname=kda-upload-tmak\
 --parameters kdaoutputbucketname=kda-output-tmak\
 --parameters sourceStreamName=ProducerStream\
 --parmeters deliveryStreamName=AnalyticsOutput

```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
=======
# kinesis-book

Main Document:
https://docs.google.com/document/d/1gMlNAaQVyMTTiwFWcqNJ16KFweI3QAkOoo4PQO22gBY/edit#
>>>>>>> f9081d00953e48ae5f3637ae79d96e1e75e2447c
