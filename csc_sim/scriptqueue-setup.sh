#!/bin/bash
. /home/saluser/.setup_dev.sh

source .setup.sh
if [[ $LSST_DDS_IP != *"."* ]]; then
  echo "Unset LSST_DDS_IP"
  unset LSST_DDS_IP
fi
python -u scriptqueue.py