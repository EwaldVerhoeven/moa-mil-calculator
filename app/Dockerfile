FROM python:3.10.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install nano

#dependencies for cv2 to run
RUN apt-get install -y\
    ffmpeg \
    libsm6 \
    libxext6 \

RUN mkdir /project
WORKDIR /project

COPY setup.py /project/

RUN python -m pip install --upgrade pip setuptools

COPY . /project/

RUN pip install -e .[dev]

ENV PYTHONPATH "${PYTONPATH}:/project/app"

EXPOSE 8000
