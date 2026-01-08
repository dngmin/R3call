import sqlite3

class Access_db:
    
    def __init__(self):
        self.conn = sqlite3.connect("db\\r3call.db")
        self.cur = self.conn.cursor()

    def select_3words(self):
        self.cur.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 3")
        
        return self.cur.fetchall()
    
if __name__ == "__main__":
    db = Access_db()
    print(db.select_3words())