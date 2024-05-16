import sqlite3

conn = sqlite3.connect('users.db')

cur = conn.cursor()

cur.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')

conn.commit()

cur.close()
conn.close()