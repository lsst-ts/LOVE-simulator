#!/usr/bin/env bash

# This file is part of LOVE-simulator.
#
# Copyright (c) 2023 Inria Chile.
#
# Developed by Inria Chile.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or at
# your option any later version.
#
# This program is distributed in the hope that it will be useful,but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


# Source this file when starting the container to set it up
source /home/saluser/.setup_dev.sh
if [[ $LSST_DDS_IP != *"."* ]]; then
  echo "Unset LSST_DDS_IP"
  unset LSST_DDS_IP
fi

#WRITE CONFIG
cd /home/saluser/repos/ts_config_ocs/Watcher/
version=$(ls | sort -V | tail -n 1)
echo "rules:
- classname: Enabled
  configs:
  - name: ATDome
  - name: ATDomeTrajectory
  - name: ATHexapod
  - name: ATMCS
  - name: ATPneumatics
  - name: ATPtg
  - name: WeatherStation
  - name: ATAOS
  - name: GenericCamera
  - name: ScriptQueue:1
- classname: Heartbeat
  configs:
  - name: ATDome
  - name: WeatherStation
  - name: GenericCamera
  - name: ScriptQueue:1" > ./$version/default.yml

#RUN WATCHER
cd /home/saluser/repos/ts_watcher
setup -r .
scons install declare
python /home/saluser/repos/ts_watcher/bin/run_watcher