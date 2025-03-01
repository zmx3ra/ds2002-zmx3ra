#!/bin/bash

argument1=$1
argument2=$2
argument3=$3
# adding the positional arguments

aws s3 cp $argument1 s3://$argument2
# this will move the file into the designated bucket


aws s3 presign --expires-in $argument3 s3://$argument2/$argument1

# this will make the link 
