#!/bin/bash
rm -rf source/apidoc
sphinx-apidoc -o source/apidoc/simulator ../simulator
sphinx-apidoc -o source/apidoc/csc_sim ../csc_sim
