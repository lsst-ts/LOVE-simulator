FROM lsstts/develop-env:sal_v4.0.0_salobj_v5.0.0

WORKDIR /usr/src/love
COPY simulator/requirements.txt .
RUN source /opt/lsst/software/stack/loadLSST.bash && pip install -r requirements.txt
RUN source /opt/lsst/software/stack/loadLSST.bash \
    && source /home/saluser/repos/ts_sal/setup.env \
    && setup ts_sal -t current \
    && /home/saluser/repos/ts_sal/bin/make_idl_files.py Watcher
COPY simulator ./simulator

WORKDIR /home/saluser
ENTRYPOINT ["/usr/src/love/simulator/start-daemon.sh"]
