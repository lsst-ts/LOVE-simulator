#!/bin/bash
source /home/saluser/setup.sh
cd /home/saluser/
echo "# Starting WeatherStation Simulator CSCs for every salindex with a 'command_sim' source in the config file"
python -u weatherstation.py
