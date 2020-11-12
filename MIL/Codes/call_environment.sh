#!/bin/bash

echo "Executing a bash statement"
#export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64
$1 $2 --env_path=$1 --script_path=$2 --input=$3 --target=$4

