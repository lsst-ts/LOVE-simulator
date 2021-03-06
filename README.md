# LOVE-simulator instructions

This repository contains tools for simulation of a SAL environment. For development and demonstration purposes

See the documentation here: https://lsst-ts.github.io/LOVE-simulator/html/index.html

## Use as part of the LOVE system
In order to use the LOVE-producer as part of the LOVE system we recommend to use the docker-compose and configuration files provided in the [LOVE-integration-tools](https://github.com/lsst-ts/LOVE-integration-tools) repo. Please follow the instructions there.

## Local load for development
We provide a docker image and a docker-compose file in order to load the LOVE-simulator locally for development purposes, i.e. build documentation.

This docker-compose does not copy the code into the image, but instead it mounts the repository inside the image, this way you can edit the code from outside the docker container with no need to rebuild or restart.

### Load and get into the docker image
Follow these instructions to run the application in a docker container and get into it:

1. Launch and get into the container:
```
docker-compose up -d
docker-exec simulator bash
```

2. Inside the container:, load the setup and got to love folder
```
source .setup.sh
cd /usr/src/love
```

### Build documentation
Once inside the container and in the `love` folder you can build the documentation as follows:
```
cd docsrc
./create_docs.sh
```

### Linting & Formatting
In order to maintaing code linting and formatting we use `pre-commit` that runs **Flake8** (https://flake8.pycqa.org/) and **Black** (https://github.com/psf/black) using Git Hooks. To enable this you have to:

1. Install `pre-commit` in your local development environment:
```
pip install pre-commit
```

2. Set up the git hook scripts running:
```
pre-commit install
```

3. Start developing! Linter and Formatter will be executed on every commit you make