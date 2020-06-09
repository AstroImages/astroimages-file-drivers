#!/usr/bin/env bash


clear
# exit when any command fails
set -e

export PYTHONPATH=$PYTHONPATH:../astroimages-file-drivers/

echo "----------------------------------------------------------------------"
echo "UNIT TESTS"
echo "----------------------------------------------------------------------"
python -m unittest discover ./test/unit -v


echo "----------------------------------------------------------------------"
echo "COMPONENT TESTS"
echo "----------------------------------------------------------------------"
python -m unittest discover ./test/component -v


