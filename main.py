import sqlite3
import scrapper
import db


preco = []
endereco = []
latitude = []
longitude = []

data = scrapper.Scrapper()

for i in range(20): 
    try:
        preco.append(data[0][i])
        endereco.append(data[1][i])
        latitude.append(data[2][i].latitude)
        longitude.append(data[2][i].longitude)
    except:
        pass

# db.insert_into_table(preco,endereco,latitude,longitude)
print(preco)
print(endereco)
print(latitude)
print(longitude)
