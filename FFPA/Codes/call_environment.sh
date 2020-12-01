#!/bin/bash

echo "Executing a bash statement"
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64
$1 $2 $3 $4 $5 --env_path=$1 --script_path=$2 --dataset=$3 --test_folder=$4 --gpu=$5

