# Tensorflow with Jupyter notebook

Like the Jupyter container, which also uses Firefox, this will not run over
SSH. The following command can be used instead on the actual machine instead.
```
docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --rm -it mytf
```

The Dockerfile used here is taken from [Tensorflow's Github
repository](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/dockerfiles)
and modified. The `bashrc` and `readme-for-jupyter.md` files come from the same
place.
