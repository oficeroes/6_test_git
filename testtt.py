import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.cursor()

cursor.execute('''

   CREATE TABLE IF NOT EXISTS employees (

       id id INTEGER PRIMARY KEY,                    

       name TEXT NOT NULL,

       salary REAL

   )

''')

cursor.execute("CREATE TABLE IF NOT EXISTS employees('name TEXT,salary TEXT')")

cursor.executemany('INSERT INTO employees VALUES(?,?,?)')

conn.commit()

print("薪资大于5000的员工：")

cursor.execute('SELECT * FROM employees WHERE > 5000')

for row in cursor:

   print(row)

cursor.execute('  UPDATE employees SET salary = 5500 WHERE id = 1')

conn.commit()

cursor.execute('DELETE FROM employees WHERE id = 2')

conn.commit()

conn.close()