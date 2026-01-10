import sqlite3

conn = sqlite3.connect("db\\r3call.db")
cur = conn.cursor()

with open("db\schema.sql","r",encoding="utf-8") as f:
    cur.execute(f.read())

with open("data\sample.txt","r",encoding="utf-8") as f:
    for line in f:
        word, pronunciation, meaning = line.strip().split(",")
        cur.execute(
            "INSERT INTO words (word, pronunciation, meaning) VALUES (?, ?, ?)",
            (word, pronunciation, meaning)
        )

conn.commit()
conn.close()