FROM prefecthq/prefect:2-python3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY realtime-poc/ .
CMD ["python", "real_time_flow.py"]
