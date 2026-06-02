import sqlite3
import tkinter as tk
glob(i)= 0
def add_books_python():
    cur.execute("INSERT INTO books VALUES ('Python','小明')")
    conn.commit()
    print("--- 录入成功，当前数据： ---")
    check()

def check():
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()
    if data:
        print(globals(i))
    else:
        print('数据库内容是空的')
    i += 1

root = tk.Tk()
root.geometry("300x500")
btn = tk.Button(root, text="加入python",command=add_books_python)

conn = sqlite3.connect('my_library.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS books (name TEXT , author TEXT)")
conn.commit()
print("数据库和表已准备就绪！",end="\n")
btn.pack(pady=20)
check()
root.mainloop()