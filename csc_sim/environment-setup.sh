#!/bin/bash
source /home/saluser/setup.sh
cd /home/saluser/
echo "# Starting Environment Simulator CSCs for every salindex with a 'command_sim' source in the config file"
python -u environment.py
