#!/bin/bash

echo $(date) >> /tmp/run.log
echo "Hello world!" 
echo $(cat /tmp/run.log | wc -l) >&2
