# Enter conda env in Dockerfile

```Dockerfile
# Dockerfile

FROM continuumio/miniconda3

RUN conda create -n py36 python=3.6.12 -y

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "py36", "/bin/bash", "-c"]

RUN conda env list

# RUN conda install protobuf -y
# ...

# CMD [ "/bin/bash" ]

```

## Reference

https://pythonspeed.com/articles/activate-conda-dockerfile/

https://stackoverflow.com/questions/55123637/activate-conda-environment-in-docker
