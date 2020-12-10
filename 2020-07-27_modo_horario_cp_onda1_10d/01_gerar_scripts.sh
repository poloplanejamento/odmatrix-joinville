#!/bin/bash
export LC_ALL=en_US.UTF-8
chkpt=(101 102 103 104 105 106 107 108 109 1010 1011 1012 1013 1014 1015 1016 1017 1018 1019 1020 1021 1022 1023 1024 1025 1026 1027 1028 1029 1030 1031 1032 1033 1034 1035 1036 1037 1038 1039 1040 1041 1042 1043 1044)

for f in script_modo_horario_20??-??-??.py
do
	for i in "${chkpt[@]}"
	do
		sed s/fchk_XXX/fchk_"${i}"/g $f > "${f%.py}_fchk_$i.py"
	done
done
