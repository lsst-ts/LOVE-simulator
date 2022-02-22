#!/bin/bash
source /home/saluser/.setup_dev.sh
if [[ $LSST_DDS_IP != *"."* ]]; then
  echo "Unset LSST_DDS_IP"
  unset LSST_DDS_IP
fi
cd /home/saluser/
echo "# Starting MTCS Simulator: running run_mtcs_mock.py"
run_mtcs_mock.py
