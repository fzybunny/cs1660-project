#! /usr/bin/env bash

#docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix $@

# Run the gui or something.
docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user="$(id --user):$(id --group)" who70
