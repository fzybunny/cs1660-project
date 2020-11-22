FROM ubuntu:focal
WORKDIR /usr/build

# Make tzdata happy.
ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Something about keyboard-configuration
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update --fix-missing
RUN apt install -y retext

RUN useradd -ms /bin/bash mduser
WORKDIR /home/mduser
USER mduser

CMD [ "retext" ]
