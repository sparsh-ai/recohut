# syntax=docker/dockerfile:1.4
FROM public.ecr.aws/lambda/python:3.9

ARG VERSION
ARG ENV

WORKDIR /

RUN yum install -y zip unzip && yum clean all
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install

COPY requirements.txt  .
RUN pip install --no-cache-dir -r requirements.txt --target lambda_layer/python && \
    cd lambda_layer && \
    zip -r "../lambda_layer_${ENV}_${VERSION}.zip" . \
    -x '*/boto3/*' \
    -x '*/botocore/*' \
    -x '*__pycache__*' && \
    cd ..

RUN --mount=type=secret,id=AWS_ACCESS_KEY_ID \
    --mount=type=secret,id=AWS_SECRET_ACCESS_KEY \
    --mount=type=secret,id=AWS_REGION \
    --mount=type=secret,id=AWS_SESSION_TOKEN \
    export AWS_ACCESS_KEY_ID=$(cat /run/secrets/AWS_ACCESS_KEY_ID) &&\
    export AWS_SECRET_ACCESS_KEY=$(cat /run/secrets/AWS_SECRET_ACCESS_KEY) &&\
    export AWS_REGION=$(cat /run/secrets/AWS_REGION) &&\
    export AWS_SESSION_TOKEN=$(cat /run/secrets/AWS_SESSION_TOKEN) &&\
    aws s3 cp "lambda_layer_${ENV}_${VERSION}.zip" "s3://data-pipeline-lambda-layers/data-pipeline/${ENV}/csse/lambda_layer_${ENV}_${VERSION}.zip"
