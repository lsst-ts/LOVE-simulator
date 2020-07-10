#!/usr/bin/env bash

# Source this file when starting the container to set it up

. /home/saluser/.setup_dev.sh

if [[ $LSST_DDS_IP != *"."* ]]; then
  echo "Unset LSST_DDS_IP"
  unset LSST_DDS_IP
fi

#WRITE CONFIG
cd /home/saluser/repos/ts_config_ocs/Watcher/v1
echo "rules:
- classname: Enabled
  configs:
  - name: ATDome
  - name: ATDomeTrajectory
  - name: ATHexapod
  - name: ATMCS
  - name: ATPneumatics
  - name: ATPtg
  - name: Environment
  - name: ATAOS
  - name: GenericCamera
  - name: ScriptQueue:1
- classname: Heartbeat
  configs:
  - name: ATDome
  - name: ATDomeTrajectory
  - name: ATHexapod
  - name: Environment
  - name: ATAOS
  - name: GenericCamera
  - name: ScriptQueue:1" > default.yaml

#RUN WATCHER
cd /home/saluser/repos/ts_watcher
setup -r .
scons install declare
python /home/saluser/repos/ts_watcher/bin/run_watcher.py