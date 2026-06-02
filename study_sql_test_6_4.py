import sqlite3

# 1. 打开数据库连接
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# 2. 清除已存在的表 - students
# 注意：这里直接执行 SQL 语句来删除表
conn.execute('''DROP TABLE IF EXISTS students''')
conn.commit() # 执行提交，确保删除生效

# 3. 创建一个表 students
conn.execute('''④ students
(ID INT PRIMARY KEY NOT NULL,
 NAME TEXT NOT NULL,
 AGE INT NOT NULL);''')
print("Table created successfully")
conn.commit()

# 4. 插入数据
conn.execute("INSERT INTO students(ID,NAME,AGE) VALUES(1,'Allen',25)")
conn.execute("INSERT INTO students(ID,NAME,AGE) VALUES(2,'Maxsu',20)")
conn.execute("INSERT INTO students(ID,NAME,AGE) VALUES(3,'Teddy',24)")
conn.commit()
print("Records Insert successfully")

# 5. 读取表 students 中的数据
# 注意：这里需要一个变量来接收查询结果
cursor = conn.execute("SELECT * from students")

print("ID NAME AGE")
for it in cursor:
    for i in range(len(it)):
        print(it[i], end=" ")
    print('\n')

conn.close()
