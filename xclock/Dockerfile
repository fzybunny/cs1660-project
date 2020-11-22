FROM ubuntu:focal

RUN apt update -y
RUN apt install -y x11-apps

RUN useradd -ms /bin/bash xuser
USER xuser

CMD ["xclock"]
