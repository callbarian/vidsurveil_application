#!/bin/bash

echo "Executing a bash statement"
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64
$1 $2 $3 $4 

