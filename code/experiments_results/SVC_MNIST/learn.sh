#!/bin/bash

C=""
GAMMA=""

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    --gamma)
    GAMMA="$2"
    shift # past argument
    shift # past value
    ;;
    --C)
    C="$2"
    shift # past argument
    shift # past value
    ;;
esac
done

eval "$(conda shell.bash hook)"
conda activate torch
SCRIPT_PATH=$(dirname $(realpath -s $0))
python ${SCRIPT_PATH}/learner.py --gamma ${GAMMA} --C ${C}