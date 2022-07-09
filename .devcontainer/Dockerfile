FROM ubuntu:20.04

RUN apt update && apt install -y python3-pip && apt install -y git && apt -y install nano

# Install pip requirements
COPY ../requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

# Configure non-root user
ARG name=dev
RUN useradd -ms /bin/bash ${name}
USER ${name}
