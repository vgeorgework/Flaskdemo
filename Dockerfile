FROM python:3.6
MAINTAINER Vineeth George
RUN mkdir -p /app
RUN ls /app
COPY . /app
RUN ls /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
CMD python3 app.py

