# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Create a dedicated 'docker' group and user
#RUN groupadd docker && \
#  useradd -m docker -g docker -p docker && \
#  chmod 0777 /home/docker && \
#  chgrp docker /usr/local/bin && \
#  mkdir -p /home/docker/bin && chown docker /home/docker/bin
# Use this user by default
#USER docker

#ENV HOME=/home/docker
#ENV INSTALL_DIR=$HOME/bin
#ENV PATH="$PATH:$INSTALL_DIR"

RUN pip install prosail

COPY --chown=docker:docker *.py /usr/local/bin


#WORKDIR /home/docker
