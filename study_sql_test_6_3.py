import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

# 目标：查询成绩大于 90 的学生
sql_select = "SELECT name FROM GRADES WHERE score " # ⑤ 补全查询条件

cur.execute(sql_select)

# 获取所有查询结果
results = cur.fetchall()  # ⑥ 调用获取结果的方法

for row in results:
    print("优秀学生姓名：", row)

cur.close()
conn.close()