FROM python:3.6
MAINTAINER Vineeth George
RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD python3 app.py
