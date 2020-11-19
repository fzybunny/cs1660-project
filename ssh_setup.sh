# /usr/bin/env bash

# Set up the environment to run GUI applications inside Docker over SSH.
#
# The Docker container will need to be run with the following arguments:
#  * -e DISPLAY=${DISPLAY}
#  * -v /tmp/.X11-unix:/tmp/.X11-unix
#  * -v ${HOME}/.Xauthority:/home/xuser/.Xauthority (See below)
#  * --user $(id --user):$(id --group)
#  * --hostname $(hostname)
#
# -v ${HOME}/.Xauthority:/home/xuser/.Xauthority
#  The `/home/xuser/` part of this command refers to the user's home directory
#  inside the container.

# The socat command needs to be run each time before starting a container.

DISPLAY_NUMBER=$(echo $DISPLAY | cut -d. -f1 | cut -d: -f2)
socat TCP4:localhost:60${DISPLAY_NUMBER} UNIX-LISTEN:/tmp/.X11-unix/X${DISPLAY_NUMBER} &
export DISPLAY=:$(echo $DISPLAY | cut -d. -f1 | cut -d: -f2)
