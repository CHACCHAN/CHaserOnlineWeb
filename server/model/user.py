import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS "authinfo"
               (
                 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username VARCHAR(64) NOT NULL,
                 password VARCHAR(128) NOT NULL,
                 jti VARCHAR(128),
                 updated_at DATE,
                 created_at DATE
               )''')

conn.commit()
cur.close()
conn.close()