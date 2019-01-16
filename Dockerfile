FROM python:3.6

ADD . /code

RUN pip install pip --upgrade
RUN pip install setuptools

WORKDIR /code

RUN pip install -r reqs.txt


CMD  locust --host=http://example.com
