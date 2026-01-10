import sqlite3

class Access_db:
    
    def __init__(self):
        self.conn = sqlite3.connect("db\\r3call.db")
        self.cur = self.conn.cursor()

    def select_3words(self):
        self.cur.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 3")
        
        return self.cur.fetchall()
    
    def update_or_delete(self,count_list):
        # count_list構造
        # [[word1,count1],[word2,count2],[word3,count3]]
        for word, count in count_list:
            if count < 3:
                self.cur.execute(
                    "UPDATE words SET count = ? WHERE word = ?",
                    (count,word)
                )
            # countが3に達したら、つまり3回passしたら
            else:
                self.cur.execute(
                    "DELETE FROM words WHERE word = ?",
                    (word,)
                )
    
if __name__ == "__main__":
    db = Access_db()
    print(db.select_3words())