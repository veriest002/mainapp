FROM python:3.6

RUN mkdir /web_container
WORKDIR /web_container
ADD ./requirements.txt /web_container/requirements.txt
RUN pip install -r requirements.txt
ADD ./web_container
