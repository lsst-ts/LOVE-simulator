FROM lsstts/develop-env:20190610_sal3.10.0_salobj4


WORKDIR /usr/src/love
COPY requirements.txt .
RUN source /opt/lsst/software/stack/loadLSST.bash && pip install -r requirements.txt
COPY . .
WORKDIR /home/saluser
ENTRYPOINT ["/usr/src/love/start-daemon.sh"]