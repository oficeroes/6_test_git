import sqlite3
conn = sqlite3.connect('my_library.db')
cur = conn.cursor()
cur.execute("CREATE TABLE If NOT EXISTS books(name TEXT , author TEXT)")
conn.commit()
cur.execute("SELECT * FROM books WHERE author = '小明'")
results = cur.fetchall()
for i in results :
    print(i)
conn.commit()
