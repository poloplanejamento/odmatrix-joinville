#!/bin/env python3
# Exporta origem e destino por data, velocidade, modo e commuting (bool.)

from http.client import HTTPSConnection
from base64 import b64encode
import json
import csv
import pandas as pd
projectID = "X"
c = HTTPSConnection("api.odmatrix.app")
userAndPass = b64encode(b"X:").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }
finall_list = []
for date in ["2019-11-17","2019-11-18","2019-11-19"] :
    for ftriptype in ["microtrip","bus","private_transport"] :        
        for fspeed in ["0_10","10_20","20_30","30_40","40_100"] :
                request = "/generatematrix?format=json&project={}&date={}&ftriptype={}&fspeed={}".format(projectID, date, ftriptype, fspeed)
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
                        full_row['Speed'] = fspeed
                        full_row['Trips'] = value
                        finall_list.append(full_row)
#print(finall_list)
data = pd.DataFrame(finall_list)
data.to_csv("matriz4a.csv")