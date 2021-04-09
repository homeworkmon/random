#Excel spreadsheet comparison script cribbed from https://towardsdatascience.com/comparing-and-matching-column-values-in-different-excel-files-using-pandas-a25172f0ff4d 
# -*- coding: utf-8 -*-

import pandas as pd
import itertools

A = pd.read_csv('etbd.csv')
B = pd.read_csv('eid.csv')

print(A.columns)
print(B.columns)

tbd_name = A['NAME'].tolist()
tbd_created = A['CREATEDDATE'].tolist()
id_name = B['NAME'].tolist()
id_id = B['ID'].tolist()

id_dict = dict(zip(id_name, id_id))
tbd_dict = dict(zip(tbd_name, tbd_created))

k = 3

#print slice 
print list(itertools.islice(tbd_dict.items(), k))
print list(itertools.islice(id_dict.items(), k))

filename = 'template_del.csv'
f = open(filename, 'w')


headers = 'TBD_NAME, CREATEDDATE, ID_NAME, ID\n'
f.write(headers)

for tbd_name, tbd_created in tbd_dict.items():
    for id_name, id_id in id_dict.items():
        if tbd_name == id_name:
            f.write(tbd_name + ',' + tbd_created + ',' + id_name + ',' + str(id_id) + '\n')

f.close()



















