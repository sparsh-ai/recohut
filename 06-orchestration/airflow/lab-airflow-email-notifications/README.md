# Airflow Email Notifications

1. Create AWS SES Identity with Email [here](https://us-east-1.console.aws.amazon.com/ses/home?region=us-east-1#/verified-identities/create).
1. Configure Airflow Email setting with the following parameters:
   ```yaml
   [email]
    # Email backend to use
    email_backend = airflow.providers.amazon.aws.utils.emailer.send_email

    # Email connection to use
    email_conn_id = aws_default

    # Whether email alerts should be sent when a task is retried
    default_email_on_retry = True

    # Whether email alerts should be sent when a task failed
    default_email_on_failure = True

    # Email address that will be used as sender address.
    from_email = Airflow <sprsag@gmail.com>
   ```
2. Run the DAG