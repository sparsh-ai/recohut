FROM python:3.8
RUN mkdir -p /myapp/app
COPY ./ /myapp/app/
RUN python3.8 -m pip install -r /myapp/app/requirements.txt 
EXPOSE 80 8000
WORKDIR /myapp/app
RUN ["chmod", "+x", "/myapp/app/run.sh"]
CMD /myapp/app/run.sh