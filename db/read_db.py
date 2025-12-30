import sqlite3

conn = sqlite3.connect("db\\r3call.db")
cur = conn.cursor()

cur.execute("SELECT * FROM words")

rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()