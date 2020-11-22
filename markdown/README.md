# Retext Markdown Editor
This opens `retext` in a Docker container.

Command:
```
docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v ${HOME}/.Xauthority:/home/user/.Xauthority --user `id -u`:`id -g` --hostname `hostname` -ti --rm md
```
