import requests
import sqlite3
URLUEE = "https://findic.cl/api/uf"

request1 = requests.get(URLUEE)
if request1.status_code == 200:
    data1 = request1.json()
#PLACEHOLDER#
#    print(data1["serie"])
#    print(data1["codigo"]) 
valuelist1 = data1["serie"]


for x in len(valuelist1):
    print(x, valuelist1[x])