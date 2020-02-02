FROM python:3
RUN pip install click
RUN mkdir -p /opt/latitude
COPY src /opt/latitude/src
COPY test /opt/latitude/test
COPY cli.py /opt/latitude
WORKDIR /opt/latitude