#!/bin/bash
export LC_ALL=en_US.UTF-8

cd bkp

data=( "2019-11-11" )

for f in *.py
do
	for i in "${data[@]}"
	do
		sed s/XXXXX/"${i}"/g $f > "${f%.py}_$i.py"
	done
done

mv script_matriz4a_*.py ..