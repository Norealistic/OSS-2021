#!/bin/bash

echo "Good Morning!"
cal

if [ -f ~/TODO ]; then
	cat ~/TODO
else
	echo "No file expected"
fi