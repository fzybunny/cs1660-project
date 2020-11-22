# Data Science Toolbox
Project 1 for CS 1660, Fall 2020

This project contains various data science tools, each running as their own
microservice through Docker.

## Progress
- [x] Containers for all applications
- [x] All containers runnable from GUI
- [x] Top-level GUI inside Docker

Although the interface is still very clunky, we expect that all of the
applications for this project are properly functioning.

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

This should display a GUI from which each program can be run. Applications can
be run by clicking on their respective buttons. (Note that the text boxes are
only used when running SonarQube, see below). Each application runs in its own
isolated container, which is created the first time the application is run.
Depending on the speed of your network connection and the speed of your
storage, **this process can take a significant amount of time**, as some of the
images are quite large, or require installing many packages.

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
This launches a Jupyter Notebook server running inside the container. Firefox,
also running inside the container, is launched and directed to the Notebook
server. To close the application, it is necessary to both close Firefox, and to
terminate the server (by pressing ^C in the terminal).

### ReText Markdown Editor (`markdown`)
This opens ReText Markdown Editor, running within the container.

### Orange (`orange`)
This will open Orange in a new window, running within the container.

### RStudio (`rstudio`)
This will open RStudio in a new window, running inside the container.

### Apache Spark (`spark`)
This will drop the user in a shell within the container, from which
`spark-shell` can be run.

### Spyder (`spyder`)
This will open the editor in a new window, running within the container. At
first, the window may not properly update, but this can usually be resolved by
resizing it.

### Tableau (`tableau`)
Like IBM SAS, this will open Firefox (running inside the container) to the
login portal for the web application. Users with accounts can log in and use
the software from here.

### Tensorflow (`tensorflow`)
This container contains TensorFlow, with access via Jupyter Notebook. On
starting the container, a Notebook server will also be started, and Firefox
(running within the container) will be opened to connect. The Notebook contains
various sample projects for Tensorflow, which can be viewed and executed.

Like Jupyter Notebook running on its own, it is necessary to close both Firefox
and the server when exiting the container.

### Visual Studio Code IDE (`vscode`)
This container runs Visual Studio Code as a webserver, then connects to that
server through the browser to provide editing functionality. This is
accomplished by using the [code-server
project](https://github.com/cdr/code-server). Both the server and Firefox are
running inside the container.

Unlike the other containers that run both a browser and server, here, it should
only be necessary to close the browser--the server should close automatically
once all connections are terminated.

### `xclock`
This is a test application. Normally, I would go with `xeyes` instead, but it
seems to have issues when running in a tiling window manager.

### SonarQube & SonarScanner (`sonarqube`)
This container runs a SonarQube server. Unlike the other servers, this is
accessed from the host's web browser. The container exposes a port to the host,
and the server can be accessed from `localhost:9000` on the host. The login
credentials are `admin` for both the username and password

#### First run
On the first run, make sure to clear the text boxes on the main GUI application
window.

When creating a project within SonarQube, make note of the project key--this
will be used to connect to the Scanner.

#### Subsequent runs
In the main GUI, enter the path to a source code directory (on the host) to
analyse, along with the project key, and launch the application again. This
will start SonarScanner, which will analyse the code in the given directory.
After some time, if the scanner was able to properly connect to SonarQube, the
results will be displayed in the browser.

## Notes
The following resources may be helpful for development.
 * [Running GUI Apps in Docker](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)
 * [GUI in Docker over SSH](https://blog.yadutaf.fr/2017/09/10/running-a-graphical-app-in-a-docker-container-on-a-remote-server/)
 * [Ubuntu Package Search](https://packages.ubuntu.com/search)
