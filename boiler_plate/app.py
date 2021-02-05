from flask import Flask, jsonify
import numpy as np

# from flaskext.mysql import MySQL
import pymysql

db=pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '1234',
            db = 'modulo_4_sql'
)
app = Flask(__name__)
print(db)
# api = MySQL(app)


@app.route('/api/nombre')
def nombre():
    random = np.random.uniform(-1, 1, size=10)
    print(random)
    return jsonify({"data": "dani"})

@app.route('/api/nota')
def nota():
    mycursor = db.cursor()
    mycursor.execute("SELECT notas FROM table1")
    myresult = mycursor.fetchall()
    return jsonify({"data": myresult})


"""
POST --> Send request from client at endpoint /api/titulacion
From server --> Recieve data and push to db
 server returns 200 if okk otherwise returns 400 (Error)
"""
@app.route('/api/titulacion') #endpoint
def titulacion():
    mycursor = db.cursor()

    sql = "INSERT INTO table1 (idtable1,nombre, notas) VALUES (%s, %s, %s)"
    val = [
        (4,'Maria', 3),
        (5,'Amy', 652)
    ]
    mycursor.executemany(sql, val)
    db.commit()
    return jsonify({"status":200})



##### --> HTTP/HTTPS
##### --> GET: Todo el dataset, Todas las notas, Todos los nombres
##### --> POST: Meter cosas en la db


