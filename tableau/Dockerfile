FROM ubuntu:focal

RUN apt update
RUN apt install -y firefox

RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user

CMD [ "firefox", "https://sso.online.tableau.com/public/idp/SSO" ]
