import scrapper
import sqlite3
#create db
database = sqlite3.connect('moradia_custo.db') 
db = database.cursor()

def insert_into_table(preco,endereco,latitude,longitue):
    # Create query
    succ = True
    try:
        for i in range(len(preco)):
            db.execute('''INSERT INTO moradia (preco,endereco,latitude,longitude) VALUES ('{}','{}','{}','{}')'''.format(preco[i],endereco[i],latitude[i],longitude[i]))
    except:
        succ = False 
    print(succ)

    database.commit()

    database.close()

def recreate_table():
    try:
        db.execute('''CREATE TABLE moradia(
                 id moradia PRIMARY KEY ,
                 preco text NOT NULL,
                 endereco text,
                 latitude text,
                 longitude text
         );''')
    except:

        db.execute('''DROP TABLE moradia''')

        db.execute('''CREATE TABLE moradia(
                 id moradia PRIMARY KEY ,
                 preco text NOT NULL,
                 endereco text,
                 latitude text,
                 longitude text
         );''')

        print("table created")

       
    database.commit()

    database.close()

def select_table():
    db.execute("SELECT * FROM moradia")
    results = db.fetchall()

    for i in results:
        print(i)

# Uncomment for testing and running //////////////////////////////////////////

# recreate_table()
# select_table()
