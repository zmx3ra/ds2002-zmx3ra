#!/bin/bash

argument1=$1
argument2=$2
argument3=$3


aws s3 cp $argument1 s3://$argument2



aws s3 presign --expires-in $argument3 s3://$argument2/$argument1

