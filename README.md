# LOVE-simulator instructions

This repository contains tools for simulation of a SAL environment. For development and demonstration purposes

See the documentation here: https://lsst-ts.github.io/LOVE-simulator/html/index.html

## Use as part of the LOVE system
In order to use the LOVE-producer as part of the LOVE system we recommend to use the docker-compose and configuration files provided in the [LOVE-integration-tools](https://github.com/lsst-ts/LOVE-integration-tools) repo. Please follow the instructions there.

## Local load for development
We provide docker images and a docker-compose file in order to load the LOVE-simulator locally for development purposes, i.e. build documentation.

This docker-compose does not copy the code into the image, but instead it mounts the repository inside the image, this way you can edit the code from outside the docker container with no need to rebuild or restart.

### Load and get into the docker image
Follow these instructions to run the application in a docker container and get into it:

1. Launch and get into the container:
```
cd docker/
export dev_cycle=develop #Here you can set a specified version of the lsstts/develop-env image
docker-compose up -d --build
docker-exec simulator bash
```

2. Inside the container:, load the setup and got to love folder
```
source /home/saluser/.setup_dev.sh #Here some configurations will be loaded and you will enter another bash. Press [Ctrl + D] to exit the current console, then the love-producer package will be installed and you can continue with the following step
cd /usr/src/love
```

### Build documentation
Once inside the container and in the `love` folder you can build the documentation as follows:
```
cd docsrc
./create_docs.sh
```

### Linting & Formatting
This code uses pre-commit to maintain `black` formatting, `isort` and `flake8` compliance. To enable this, run the following commands once (the first removes the previous pre-commit hook):

```
git config --unset-all core.hooksPath
generate_pre_commit_conf
```

For more details on how to use `generate_pre_commit_conf` please follow: https://tssw-developer.lsst.io/procedures/pre_commit.html#ts-pre-commit-conf.