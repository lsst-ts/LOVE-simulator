ARG dev_cycle=develop
FROM lsstts/develop-env:${dev_cycle}

WORKDIR /usr/src/love
RUN source /home/saluser/.setup_dev.sh && \
  pip install gevent greenlet six websocket-client websockets eventlet

COPY . .
WORKDIR /home/saluser
    
ENTRYPOINT ["/usr/src/love/docker/start-daemon-dev.sh"]
