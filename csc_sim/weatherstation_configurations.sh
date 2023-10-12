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


#!/bin/bash
echo "# Running develop-env/setup.sh"
# from ts_sal setup.env
#export LSST_DDS_QOS=file:///home/saluser/tsrepos/ts_sal/test/python/DDS_DefaultQoS_All.xml
#export SAL_IDL_DIR=/home/saluser/tsrepos/ts_sal/test/idl-templates/validated/sal

#to use licensed version this may help:
#export OSPL_HOME=/home/saluser/tsrepos/OpenSpliceDDS/Vortex_v2/Device/VortexOpenSplice/6.10.2/HDE/x86_64.linux
#export OSPL_TMPL_PATH=$OSPL_HOME/etc/idlpp
#export OSPL_URI=file:///home/saluser/tsrepos/OpenSpliceDDS/Vortex_v2/Device/VortexOpenSplice/6.10.2/HDE/x86_64.linux/etc/config/ospl.xml
echo "OSPL_HOME=${OSPL_HOME}"

# ***** SET THIS PATH *****
export TSREPOS="/home/saluser/repos"

# ***** CHOOSE THE CORRECT ts_sal *****
# * If using the ts_sal included in the Docker image:
#   export TS_SAL_DIR=${HOME}/repos/ts_sal
# * If using your own ts_sal:
#   export TS_SAL_DIR=${TSREPOS}/ts_sal
export TS_SAL_DIR=${HOME}/repos/ts_sal

export LSST_SDK_INSTALL=${TS_SAL_DIR}

# Put the correct ts_sal's lsstsal/bin and lsstsal/scripts directories on PATH,
# to override the default, which is the built-in ts_sal.
export PATH=${TS_SAL_DIR}/lsstsal/bin:${TS_SAL_DIR}/lsstsal/scripts:${PATH}

# Eliminate duplicates from bash history
export HISTCONTROL="ignoreboth"

# Load the LSST stack before configuring the SAL environment
# because SAL's setup.env must find the correct python.
echo "# Load the LSST Stack"
. /opt/lsst/software/stack/loadLSST.bash

echo "# Configure ts_sal in ${TS_SAL_DIR}"
# source /home/saluser/tsrepos/docker/develop-env/setup.env
source ${TS_SAL_DIR}/setup.env

eups_declare() {
    eups declare -r "${TSREPOS}/$1" "$1" git -t current
}

declare_and_setup() {
    eups_declare "$1"
    setup -k "$1"
}

# ***** SETUP YOUR PACKAGES *****
# Declare and setup packages from your disk;
# omit any packages you want to use from the Docker image.
# Be sure to declare packages *before* you setup packages that depend on them.
echo "# Declare and setup my packages; please ignore \"Warning: path...\" messages"
setup sconsUtils
setup -k verify
eups_declare ts_weatherstation
declare_and_setup ts_weatherstation

/bin/bash
