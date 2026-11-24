import requests
import sqlite3
URLUEE = "https://findic.cl/api/uf"

request1 = requests.get(URLUEE)
if request1.status_code == 200:
    data1 = request1.json()
    print(data1["codigo"])
