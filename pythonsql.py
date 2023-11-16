import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
rows = cursor.execute("Select Max(cod_prod) from Productos").fetchall()
print(rows)