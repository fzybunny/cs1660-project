# Visual Studio Code in the browser

This container runs vscode as a webserver, and opens a connection to that
server within the browser, all running inside a Docker container.

The [code-server project](https://github.com/cdr/code-server) is used to do
this.

Like the other containers that use Firefox, there are some difficulties running
over SSH.

Command:
```
docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --rm -it vsb
```
