FROM python:3.8
# Install dependencies
RUN pip install --upgrade pip setuptools wheel
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install connectors on Debezium
COPY ./connectors/configure_connectors.py configure_connectors.py