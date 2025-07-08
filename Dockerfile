# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && \
    apt-get install -y git && \
    mkdir ps && \
    git clone https://github.com/jgomezdans/prosail.git && \
    pip install prosail --target=~/ps 

ENV PYTHONPATH=/usr/lib/python3/dist-packages:~/ps

