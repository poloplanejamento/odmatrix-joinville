#!/bin/env python3
# Exporta origem e destino por data e modo (pivotada)

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
for fcommuting in ["true","false"] :
    for date in ["2020-03-05"] :
        for ftriptype in ["microtrip","bus","private_transport"] :       
            request = "/generatematrix?format=json&project={}&date={}&ftriptype={}&fcommuting={}".format(projectID, date, ftriptype, fcommuting)
            c.request('GET', request, headers=headers)
            res = c.getresponse()
            data = res.read()
            matrix = json.loads(data)
            print(request)
            for i, column in enumerate(matrix['ColumnLabels']):
                for j, row in enumerate(matrix['RowLabels']):
                    value = matrix['Data'][j][i]
                    if value == 0:
                        continue
                    full_row = {}
                    full_row['ProjectID'] = projectID
                    full_row['Date'] = date
                    full_row['Origin'] = row
                    full_row['Commuting'] = fcommuting
                    full_row['Destination'] = column
                    full_row['Modo'] = ftriptype
                    full_row['Trips'] = value
                    finall_list.append(full_row)
#print(finall_list)
data = pd.DataFrame(finall_list)
final_data =  pd.pivot_table(data, index=['ProjectID', 'Date', 'Origin', 'Destination', 'Modo'], columns='Commuting', values='Trips')
final_data.to_csv("matriz1b_commuting_2020-03-05.csv")
