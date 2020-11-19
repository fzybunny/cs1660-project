# Jupyter notebooks in Docker (via Anaconda)

This currently will not run over SSH. Use the following command on the actual
machine instead.
```
docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user 1000:1000 --hostname `hostname` -it jupyter
```
