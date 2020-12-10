#!/bin/sh
tail -n+1 OD_por_modo_media_naocommuting_horario_17-18-19.csv > OD_por_modo_media_naocommuting_horario.csv
tail -n+2 OD_por_modo_media_naocommuting_horario_20-21-22.csv >> OD_por_modo_media_naocommuting_horario.csv
tail -n+2 OD_por_modo_media_naocommuting_horario_23-24.csv >> OD_por_modo_media_naocommuting_horario.csv

tail -n+1 OD_por_modo_naocommuting_horario_17-18-19.csv > OD_por_modo_naocommuting_horario.csv
tail -n+2 OD_por_modo_naocommuting_horario_20-21-22.csv >> OD_por_modo_naocommuting_horario.csv
tail -n+2 OD_por_modo_naocommuting_horario_23-24.csv >> OD_por_modo_naocommuting_horario.csv
