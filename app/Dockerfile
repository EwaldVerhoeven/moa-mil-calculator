FROM python:3.10.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install nano


RUN mkdir /project
WORKDIR /project

COPY setup.py /project/

RUN python -m pip install --upgrade pip setuptools 
RUN pip install -e .[dev]

COPY . /project/

ENV PYTHONPATH "${PYTONPATH}:/project/app"

EXPOSE 8000