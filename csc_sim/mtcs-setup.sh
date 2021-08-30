#!/bin/bash
. /home/saluser/.setup_dev.sh

if [[ $LSST_DDS_IP != *"."* ]]; then
  echo "Unset LSST_DDS_IP"
  unset LSST_DDS_IP
fi

cd /home/saluser/
echo "# Starting MTCS Simulator CSCs for every salindex with a 'command_sim' source in the config file"
run_mtcs_mock.py
