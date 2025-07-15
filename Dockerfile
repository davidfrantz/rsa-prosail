# Use an official Python runtime as a parent image
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y procps && \
    rm -rf /var/lib/apt/lists/*

# Create a dedicated 'docker' group and user
RUN groupadd docker && \
  useradd -m docker -g docker -p docker && \
  chmod 0777 /home/docker && \
  chgrp docker /usr/local/bin && \
  mkdir -p /home/docker/bin && chown docker /home/docker/bin
# Use this user by default
USER docker

ENV HOME=/home/docker
ENV INSTALL_DIR=$HOME/bin
ENV PATH="$PATH:$INSTALL_DIR"

RUN pip install prosail

COPY --chown=docker:docker *.py $INSTALL_DIR

RUN mkdir -p /home/docker/.local && chmod -R 777 /home/docker/.local

WORKDIR /home/docker
