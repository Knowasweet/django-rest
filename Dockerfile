FROM python:3.10

# set environment variables
ENV PYTHONUNBUFFERED=1

RUN mkdir /app

# change workdir
WORKDIR /app

# install dependencies
COPY . /app/
RUN pip install -r requirements.txt