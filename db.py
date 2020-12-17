import main
import sqlite3
#create db
def query():
    database = sqlite3.connect('moradia_custo.db') 
    db = database.cursor()
    #db.execute('drop table moradia')

    """
    db.execute('''CREATE TABLE IF NOT EXISTS moradia(
            id moradia PRIMARY KEY AUTO_INCREMENT,
            preco text NOT NULL,
            moradia text
    );''')
    """

    #for a in db.execute('SELECT * FROM moradia'):
        #print(a)

    result = list(main.Scrapper())
    endereco = []
    preco= []
    for i in range(19):
        preco.append(result[0][i])
        print(preco[i])
    for i in range(19):
        endereco.append(result[1][i])
        print(endereco[i])

    #for a in range(len(result)):
        #print(result[a])
        #db.execute('INSERT INTO moradia (preco,moradia) VALUES (%s,%s)', %(preco,moradia)

query()
