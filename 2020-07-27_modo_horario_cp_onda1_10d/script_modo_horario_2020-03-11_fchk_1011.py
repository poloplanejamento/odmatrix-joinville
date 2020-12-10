#!/usr/bin/env python3

# Bibliotecas
from http.client import HTTPSConnection
from base64 import b64encode
import json
import csv
import pandas as pd

# Variáveis
projectID = "40"     # ID do projeto, conforme mostrado no frontend Web
c = HTTPSConnection("api.odmatrix.app")
userAndPass = b64encode(b"fe6b53f0280443d5bd40d5d30694f356").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }
finall_list = []

# Formato da data: AAAA-MM-DD. Até três datas no array e o script parece rodar sem problemas
# Datas desejadas:  12/11, 13/11, 19/11, 20/11, 21/11, 03/03, 04/03, 05/03, 11/03 e 12/03
for date in ["2020-03-11"] :
    for ftriptype in ["microtrip","bus","private_transport"] :
        for ftimeorigin in ["0000_0059","0100_0159","0200_0259","0300_0359","0400_0459","0500_0559","0600_0659","0700_0759","0800_0859","0900_0959","1000_1059","1100_1159","1200_1259","1300_1359","1400_1459","1500_1559","1600_1659","1700_1759","1800_1859","1900_1959","2000_2059","2100_2159","2200_2259","2300_2359"] :
            print(ftimeorigin)
            request = "/generatematrix?format=json&project={}&date={}&ftriptype={}&ftimeorigin={}&fchk_1011=true".format(projectID, date, ftriptype, ftimeorigin)
            c.request('GET', request, headers=headers)
            res = c.getresponse()
            data = res.read()
            matrix = json.loads(data)
            for i, column in enumerate(matrix['ColumnLabels']):
                for j, row in enumerate(matrix['RowLabels']):
                    value = matrix['Data'][j][i]
                    if value == 0:
                        continue
                    full_row = {}
                    full_row['ProjectID'] = projectID
                    full_row['Date'] = date
                    full_row['TimeOrigin'] = ftimeorigin
                    full_row['Origin'] = row
                    full_row['Destination'] = column
                    full_row['Modo'] = ftriptype
                    full_row['Trips'] = value
                    finall_list.append(full_row)
                    print(full_row)
#print(finall_list)
data = pd.DataFrame(finall_list)
final_data =  pd.pivot_table(data, index=['ProjectID', 'Date', 'Origin', 'Destination', 'Modo'], columns='TimeOrigin', values='Trips')
final_data.to_csv("OD_por_modo_horario_fchk_1011_2020-03-11.csv")
