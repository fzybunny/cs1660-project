FROM python:3.9.0
WORKDIR /usr/src

RUN pip install docker

COPY . /usr/src/
#ADD ../xclock /home/user/xclock

CMD [ "python3", "main.py" ]
