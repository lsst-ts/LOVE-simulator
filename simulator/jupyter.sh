#!/bin/bash
. /home/saluser/.setup_dev.sh

jupyter lab --no-browser --port=1234 --ip=0.0.0.0 --allow-root --NotebookApp.token=$JUPYTER_PASS
