#!/bin/bash

MAIN_PATH=""
EXPERIMENT_PATH=""

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    --script)
    MAIN_PATH="$2"
    shift # past argument
    shift # past value
    ;;
    --input)
    EXPERIMENT_PATH="$2"
    shift # past argument
    shift # past value
    ;;
esac
done

eval "$(conda shell.bash hook)"
conda activate py2
SCRIPT_PATH=$(dirname $(realpath -s $0))
python ${SCRIPT_PATH}/${MAIN_PATH} ${SCRIPT_PATH}/${EXPERIMENT_PATH}