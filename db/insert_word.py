import sqlite3

word = input("word : ")
pronunciation = input("pronunciation : ")
meaning = input("meaning : ")

check = input("is it right? Y/N     : ")
if check == "Y":
    conn = sqlite3.connect("db\\r3call.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO words (word, pronunciation, meaning) VALUES (?, ?, ?)",
        (word, pronunciation, meaning)
    )

    cur.execute(
        "SELECT * FROM words WHERE word = ?",
        (word,)
    )
    print(cur.fetchall())

    conn.commit()
    conn.close()
else:
    pass