FROM ubuntu:focal

RUN apt update --fix-missing -y
RUN apt install -y git

RUN useradd -ms /bin/bash gituser
USER gituser
WORKDIR /home/gituser/

CMD [ "/bin/bash" ]
