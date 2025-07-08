# Use an official Python runtime as a parent image
FROM python:3.8

RUN apt-get update && \
    apt-get install -y git && \
    mkdir ps && \
    git clone https://github.com/jgomezdans/prosail.git && \
    pip install prosail --target=~/ps 

ENV PYTHONPATH=/usr/lib/python3/dist-packages:~/ps

