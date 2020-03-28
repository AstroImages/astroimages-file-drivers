#!/usr/bin/env bash

clear

# exit when any command fails
set -e

docker build -f ./CICD/Dockerfile.tests -t astroimages-file-drivers:latest .

docker run --rm -ti -p 5000:5000 astroimages-file-drivers

# BASH-OPENING VERSON
# docker run --rm -ti -p 5000:5000 astroimages-file-drivers /bin/bash
