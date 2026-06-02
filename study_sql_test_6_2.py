import sqlite3

# 1. 建立数据库连接
conn = sqlite3.connect("warehouse.db")
cur = conn.cursor()  # ① 创建游标

# 2. 创建表：如果不存在则建立 STOCKS 表
sql_create = "CREATE TABLE IF NOT EXISTS STOCKS (item TEXT, count INT)"
cur.execute(sql_create) # ② 执行建表指令

# 3. 插入数据：存入 'Apple', 数量 50
sql_insert = "INSERT INTO STOCKS VALUES ('Apple', 50)"
cur.execute(sql_insert) # ③ 填入 SQL 语句

# 4. 提交并关闭
conn.commit() # ④ 提交保存更改
cur.close()
conn.close()
















