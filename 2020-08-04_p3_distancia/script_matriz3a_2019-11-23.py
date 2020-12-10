#!/bin/env python3
# Exporta origem e destino por data, distância, modo e commuting (bool.)

from http.client import HTTPSConnection
from base64 import b64encode
import json
import csv
import pandas as pd
projectID = "42"
c = HTTPSConnection("api.odmatrix.app")
userAndPass = b64encode(b"fe6b53f0280443d5bd40d5d30694f356").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }
finall_list = []
for date in ["2019-11-23"]:
    for ftriptype in ["microtrip","bus","private_transport"] :        
        for fdistance in ["0_5","5_10","10_15","15_20","20_40","40_60","60_80","80_100","100_150","150_200"] :
                request = "/generatematrix?format=json&project={}&date={}&ftriptype={}&fdistance={}".format(projectID, date, ftriptype, fdistance)
                print(request)
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
                        full_row['Origin'] = row
                        full_row['Destination'] = column
                        full_row['Modo'] = ftriptype
                        full_row['Distance'] = fdistance
                        full_row['Trips'] = value
                        finall_list.append(full_row)
#print(finall_list)
data = pd.DataFrame(finall_list)
data.to_csv("matriz3a_2019-11-23.csv")
