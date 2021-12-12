#!/bin/bash

if [  $# -eq 0 ]; then
	DIR=/usr
else
	DIR=$1
fi

find $DIR -size +20M