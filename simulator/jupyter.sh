#!/bin/bash
. /home/saluser/.setup_dev.sh
/home/saluser/repos/ts_sal/bin/make_idl_files.py LOVE
pip install jupyterlab
jupyter lab --no-browser --port=1234 --ip=0.0.0.0 --allow-root --NotebookApp.token=$JUPYTER_PASS
