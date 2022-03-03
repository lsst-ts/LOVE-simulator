ARG dev_cycle=develop
FROM lsstts/develop-env:${dev_cycle}

WORKDIR /usr/src/love
COPY simulator/requirements.txt .
RUN source /opt/lsst/software/stack/loadLSST.bash && pip install -r requirements.txt

COPY . .
WORKDIR /home/saluser
    
ENTRYPOINT ["/usr/src/love/docker/start-daemon-dev.sh"]
