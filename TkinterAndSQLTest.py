'''你需要从零开始编写一个程序，实现以下功能：
搭建界面：创建一个窗口，包含一个输入框（Entry）用于输入“学生姓名”，以及一个“录入”按钮
。
数据库操作：点击按钮后，程序需将输入框里的姓名存入名为 school.db 的数据库中（表名为 students，字段只需一个 name）
。
动态交互：存入成功后，使用 StringVar 让窗口中的标签显示“姓名：XXX 录入成功！”
。
安全关闭：点击窗口关闭时，确保数据库连接已正常断开
。'''

import tkinter as tk
import sqlite3 as sq



def save_students():
    name = entry.get()
    if name :
        cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()  # 必须提交才能保存 [3]
        var.set(f"姓名：{name} 录入成功！")

def closing():
    conn.close()
    root.destroy()

conn = sq.connect("school.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT)")
conn.commit()
root = tk.Tk()
root.geometry("300x300")
var = tk.StringVar()
var.set("Hello")
label = tk.Label(root, textvariable= var )
entry = tk.Entry(root)
entry.pack()
btn = tk.Button(root, text="录入",command= save_students)
btn.pack()
label.pack()
root.mainloop()
root.protocol("WM_DELETE_WINDOW", closing) # 窗口关闭时触发
