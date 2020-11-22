FROM ubuntu:focal

# Make tzdata happy.
ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update -y
RUN apt install -y r-base
#
#CMD ["R", "--vanilla"]

#FROM r-base:latest
WORKDIR /usr/build

RUN apt update --fix-missing
RUN apt install -y --fix-broken \
# Dependencies for RStudio deb
	libedit2 \
	libclang-dev \
	libxkbcommon-x11-0 \
# Dynamic linked libraries
	qtbase5-dev \
# Something something OpenGL
	ffmpeg \
	libsm6 \
	libxext6 \
	libnss3 \
# Run-time dependencies?
	libxcomposite1 \
	libxtst6

RUN apt install -y wget

# RStudio
RUN wget --quiet "https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.3.1093-amd64.deb"
RUN dpkg -i rstudio-1.3.1093-amd64.deb

#CMD ["R", "--vanilla"]
CMD ["rstudio"]
