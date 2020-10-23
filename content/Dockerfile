FROM python:3.9.0-alpine as builder
LABEL maintainer="Kemp Po kempspo@gmail.com"

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python:3.9.0-alpine
RUN mkdir src
COPY . src/

CMD ['pelican', 'src/publishconf.py']