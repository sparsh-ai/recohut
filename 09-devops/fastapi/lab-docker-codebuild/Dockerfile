FROM public.ecr.aws/lambda/python:3.8
RUN yum install -y openblas-serial\
gmp gmp-devel
COPY requirements.txt ./
RUN python3.8 -m pip install -r requirements.txt 
RUN mkdir -p /mnt/ml
RUN mkdir -p ./app
COPY app.py ./app/
COPY src/ ./app/src/
COPY __init__.py ./app/
CMD ["app.app.handler"]