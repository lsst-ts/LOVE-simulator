#!/bin/bash

source ~/miniconda3/bin/activate
source $OSPL_HOME/release.com
pip install matplotlib

while :
    do
        run_genericcamera.py -i $INDEX
        echo "# CSC exited, restarting..."
done