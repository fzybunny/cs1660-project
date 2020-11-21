FROM ubuntu:focal

## Make tzdata happy.
ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set up dependencies
RUN apt update --fix-missing
RUN apt install -y gpg ssh pdsh openjdk-11-jre-headless
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/

# User
RUN useradd -ms /bin/bash user
WORKDIR /home/user
USER user

# Get Hadoop
RUN wget --quiet https://mirrors.ocf.berkeley.edu/apache/hadoop/common/hadoop-3.3.0/hadoop-3.3.0-aarch64.tar.gz
RUN wget --quiet https://downloads.apache.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0-aarch64.tar.gz.asc

# Verify signatures
RUN wget --quiet -O - https://downloads.apache.org/hadoop/common/KEYS | gpg --import
RUN gpg --verify hadoop-3.3.0-aarch64.tar.gz.asc hadoop-3.3.0-aarch64.tar.gz

# Extract
RUN tar xzf hadoop-3.3.0-aarch64.tar.gz

# Add to path
ENV PATH=$PATH:/home/user/hadoop-3.3.0/bin

CMD [ "/bin/bash" ]
