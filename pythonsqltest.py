import sqlite3
connection = sqlite3.connect("db.sqlite3", isolation_level=None)
cursor = connection.cursor()
rows = cursor.execute("Select Max(cod_prod) from Productos").fetchall()
print(rows[0][0])
nombre = 'my melody'
precio = 50000
imagen = 'C:\\Users\\cuent\\Desktop\\nueva clona\\Nooketplace\\media\\mm.jpg'
codigo = rows[0][0]+1
cursor.execute("INSERT INTO Productos (cod_prod, nom_prod, precio, imagen) VALUES (?,?,?,?)", (codigo,nombre,precio,imagen))
connection.commit