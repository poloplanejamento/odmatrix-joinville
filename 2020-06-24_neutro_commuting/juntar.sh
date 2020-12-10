#!/bin/sh
tail -n+1 OD_por_modo_commuting_horario_17-18-19.csv > OD_por_modo_commuting_horario.csv
tail -n+2 OD_por_modo_commuting_horario_20-21-22.csv >> OD_por_modo_commuting_horario.csv
tail -n+2 OD_por_modo_commuting_horario_23-24.csv >> OD_por_modo_commuting_horario.csv

tail -n+1 OD_por_modo_horario_17-18-19.csv > OD_por_modo_horario.csv
tail -n+2 OD_por_modo_horario_20-21-22.csv >> OD_por_modo_horario.csv
tail -n+2 OD_por_modo_horario_23-24.csv >> OD_por_modo_horario.csv

tail -n+1 OD_por_modo_media_commuting_horario_17-18-19.csv > OD_por_modo_media_commuting_horario.csv
tail -n+2 OD_por_modo_media_commuting_horario_20-21-22.csv >> OD_por_modo_media_commuting_horario.csv
tail -n+2 OD_por_modo_media_commuting_horario_23-24.csv >> OD_por_modo_media_commuting_horario.csv

tail -n+1 OD_por_modo_media_horario_17-18-19.csv > OD_por_modo_media_horario.csv
tail -n+2 OD_por_modo_media_horario_20-21-22.csv >> OD_por_modo_media_horario.csv
tail -n+2 OD_por_modo_media_horario_23-24.csv >> OD_por_modo_media_horario.csv
