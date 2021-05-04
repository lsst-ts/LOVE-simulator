#!/bin/bash
. /home/saluser/.setup_dev.sh

if [[ $LSST_DDS_IP != *"."* ]]; then
  echo "Unset LSST_DDS_IP"
  unset LSST_DDS_IP
fi

echo "# Starting ScriptQueue Simulator CSCs for every salindex with a 'command_sim' source in the config file"
python -u scriptqueue.py