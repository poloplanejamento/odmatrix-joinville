#!/bin/bash
export LC_ALL=en_US.UTF-8
data=( "2019-11-12" "2019-11-13" "2019-11-19" "2019-11-20" "2019-11-21" "2020-03-03" "2020-03-04" "2020-03-05" "2020-03-11" "2020-03-12" )

for f in *.py
do
	for i in "${data[@]}"
	do
		sed s/XXXXX/"${i}"/g $f > "${f%.py}_$i.py"
	done
done
