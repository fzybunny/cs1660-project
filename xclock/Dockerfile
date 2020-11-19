FROM ubuntu:focal

#RUN useradd -ms /bin/bash xuser

RUN apt update -y
RUN apt install -y x11-apps

USER xuser

CMD ["xclock"]
