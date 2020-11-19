# This is the Anaconda Dockerfile, but we use Ubuntu as a base instead of
# Debian because Ubuntu is easier to run graphical applications.

#FROM debian:buster-slim
FROM ubuntu:focal

# Make tzdata happy.
ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Make keyboard-configuration happy
ENV DEBIAN_FRONTEND=noninteractive

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion && \
    apt-get clean

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

RUN apt-get install -y libgl1 python3-pyqt5.qtwebkit
RUN apt-get install -y firefox

RUN useradd -ms /bin/bash user
USER user

CMD [ "/bin/bash" ]
