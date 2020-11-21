FROM ubuntu:focal
WORKDIR /usr/build

RUN apt update
RUN apt install -y gpg wget default-jre-headless

# Download
RUN wget --quiet -O - https://downloads.apache.org/spark/KEYS | gpg --import
RUN wget --quiet https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz.asc
RUN wget --quiet https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz

# Verify
RUN gpg --verify spark-3.0.1-bin-hadoop3.2.tgz.asc

# Install
RUN tar xzf spark-3.0.1-bin-hadoop3.2.tgz
RUN mv spark-3.0.1-bin-hadoop3.2 /usr/local/spark
ENV PATH=$PATH:/usr/local/spark/bin

RUN useradd -ms /bin/bash sparkuser
USER sparkuser
WORKDIR /home/sparkuser

CMD [ "/bin/bash" ]
