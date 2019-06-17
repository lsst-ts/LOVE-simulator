FROM lsstts/simulation_tests:latest
WORKDIR /home/saluser/repos/ts_sal
WORKDIR /usr/src/love
COPY requirements.txt .
RUN source /opt/lsst/software/stack/loadLSST.bash && pip install -r requirements.txt
COPY . .
WORKDIR /home/saluser
ENTRYPOINT ["/usr/src/love/start-daemon.sh"]