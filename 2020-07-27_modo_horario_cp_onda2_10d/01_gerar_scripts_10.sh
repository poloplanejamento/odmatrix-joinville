#!/bin/bash
export LC_ALL=en_US.UTF-8
chkpt=( 1045 1046 1047 1048 1049 1050 1051 1052 1053 1054 1055 1056 1057 1058 1059 1060 1061 1062 1063 )

for f in script_modo_horario_20??-??-??.py
do
	for i in "${chkpt[@]}"
	do
		sed s/fchk_XXX/fchk_"${i}"/g $f > "${f%.py}_fchk_$i.py"
	done
done
