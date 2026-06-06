import sqlite3
conn = sqlite3.connect('school.db')
cur = conn.cursor()

cur.execute('create table if not exists scores(name TEXT , score int)')
conn.commit()

a = "update scores set score = ? where name = ?"
cur.execute(a,(95,'moke'))
conn.commit()
cur.close()
print(cur.fetchone())
conn.close()
