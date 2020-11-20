FROM ubuntu:focal

# Make tzdata happy.
ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update --fix-missing -y
RUN apt install -y git-gui

RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user/

CMD [ "git", "gui" ]
