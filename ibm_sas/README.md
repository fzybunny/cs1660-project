# IBM SAS

This opens a website in Firefox.

Like the other containers that use Firefox, it has issues running over SSH. It
can be run on the actual machine with this command.
```
docker run -e DISPLAY=${DISPLAY} -v /tmp/.X11-unix --user `id -g`:`id -u` -ti sasfox
```
