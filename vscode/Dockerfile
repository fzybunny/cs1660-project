FROM jat1902/firefox
WORKDIR /usr/build

USER root

RUN apt update --fix-missing
RUN apt install -y wget

# Download the coder binary, untar it, and allow it to be executed
RUN wget https://github.com/codercom/code-server/releases/download/1.408-vsc1.32.0/code-server1.408-vsc1.32.0-linux-x64.tar.gz
RUN tar xzf code-server1.408-vsc1.32.0-linux-x64.tar.gz 
RUN chmod +x code-server1.408-vsc1.32.0-linux-x64/code-server

COPY entrypoint.sh ./

USER foxuser
WORKDIR /home/foxuser

ENTRYPOINT [ "/bin/bash", "/usr/build/entrypoint.sh" ]
