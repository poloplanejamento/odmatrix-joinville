#!/bin/env python3
# Exporta origem e destino por data e modo

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
for date in ["2019-11-26","2019-11-27","2019-11-28"] :
    for ftriptype in ["microtrip","bus","private_transport"] :
            request = "/generatematrix?format=json&project={}&date={}&ftriptype={}".format(projectID, date, ftriptype)
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
                    full_row['Trips'] = value
                    finall_list.append(full_row)
#print(finall_list)
data = pd.DataFrame(finall_list)
data.to_csv("matriz1a.csv")