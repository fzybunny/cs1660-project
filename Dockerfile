FROM python:3.9.0
WORKDIR /usr/src

RUN apt update --fix-missing
RUN apt install -y docker.io

COPY . /usr/src/

CMD [ "python3", "main.py" ]
