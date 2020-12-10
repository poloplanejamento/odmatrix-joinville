#!/bin/sh
HEADER="head -n+1"
BODY="tail -n+2"

$HEADER OD_por_modo_horario_2019-11-12.csv > OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2019-11-12.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2019-11-13.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2019-11-19.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2019-11-20.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2019-11-21.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2020-03-03.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2020-03-04.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2020-03-05.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2020-03-11.csv >> OD_por_modo_horario.csv
$BODY OD_por_modo_horario_2020-03-12.csv >> OD_por_modo_horario.csv
