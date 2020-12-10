#!/bin/bash
export LC_ALL=en_US.UTF-8
chkpt=( 1065 1066 1069 1071 1073 1074 1076 1077 1078 1079 1080 1081 1082 1083 1084 1088 1090 1075 )

for f in script_modo_horario_20??-??-??.py
do
	for i in "${chkpt[@]}"
	do
		sed s/fchk_XXX/fchk_"${i}"/g $f > "${f%.py}_fchk_$i.py"
	done
done
