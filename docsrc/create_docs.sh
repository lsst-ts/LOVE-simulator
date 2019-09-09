#!/bin/bash
rm -rf source/apidoc
sphinx-apidoc -o source/apidoc/csc-sim ../csc-sim
sphinx-apidoc -o source/apidoc/simulator ../simulator
# python edit_apidoc_modules.py
rm -rf ../docs/doctrees
rm -rf ../docs/html
make html
