# Data Science Toolbox
Project 1 for CS 1660, Fall 2020

This project contains various data science tools, each running as their own
microservice through Docker.

## Progress
- [x] Containers for all applications
- [x] All containers runnable from GUI
- [x] Top-level GUI inside Docker

## Running
### Prerequisites
It is assumed that Docker and a web browser are installed for running this
container.

All of the programs can be run from the main GUI program, which also runs
inside a Docker container.

In the root directory of this repository, the main program container can be
built with:
```
$ docker build -t 1660-project-gui
```

And it can be run with
```
$ docker run \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v ${HOST_REPO_DIR}:/home/1660 \
	-v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY \
	-it 1660-project-gui
```
where `${HOST_REPO_DIR}` is the root directory of this repository on the host
machine.

This should display a GUI from which each program can be run. Each application
runs in its own isolated container, which is created the first time the
application is run. Depending on the speed of your network connection and the
speed of your storage, **this process can take a significant amount of time**,
as some of the images are quite large, or require installing many packages.

Brief descirptions of the usage of each program follow.

### Git (`git`)
Running Git will open a shell inside a container with git installed.
Typical Git tasks can be performed in this environment.

### Apache Hadoop (`hadoop`)
This will open a shell in a container where Apache Hadoop is installed and able
to be used. Hadoop and HDFS commands can be issued. The container is intended
to be used for for [Standalone
Operation](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Standalone_Operation).

### IBM SAS (`ibm sas`)
This will open Firefox (running inside the container) to the login portal for
the application. Users with accounts can log in from here.

### Jupyter Notebook (`jupyter`)

### ReText Markdown Viewer (`markdown`)

### Orange (`orange`)

### RStudio (`rstudio`)

### Apache Spark (`spark`)

### Spyder (`spyder`)

### Tableau (`tableau`)
Like IBM SAS, this will open Firefox (running inside the container) to the
login portal for the web application. Users with accounts can log in and use
the software from here.

### Tensorflow (`tensorflow`)

### Visual Studio Code IDE (`vscode`)

### XClock (`xclock`)

### SonarQube & SonarScanner (`sonarqube`)


## Notes
The following resources may be helpful for development.
 * [Running GUI Apps in Docker](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)
 * [GUI in Docker over SSH](https://blog.yadutaf.fr/2017/09/10/running-a-graphical-app-in-a-docker-container-on-a-remote-server/)
 * [Ubuntu Package Search](https://packages.ubuntu.com/search)
