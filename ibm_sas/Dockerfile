FROM ubuntu:focal

RUN apt update
RUN apt install -y firefox

RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user

CMD [ "firefox", "https://www.pdesas.org/Profile/Account/Login" ]
