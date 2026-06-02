import sqlite3

while True:
    code = input("1代表插入，2代表查询, 3代表删除, 4代表退出\n请输入操作代号:")

    # [查询功能]
    if code == "2":  # 用户输入2
        print('所有学生姓名如下：')
        conn2 = sqlite3.connect('data.db')
        c2 = conn2.cursor()
        # 查询所有学生姓名
        cursor = c2.execute("SELECT NAME from STUDENT ")
        for row in cursor:
            print(row)
        conn2.close()

        select_name = input("请输入需要查询的姓名：")
        conn3 = sqlite3.connect('data.db')
        c3 = conn3.cursor()
        # 根据姓名查询详细信息
        cursor = c3.execute("SELECT * from STUDENT WHERE NAME =? ", (select_name, ))
        for row in cursor:
            print(*row)
        conn3.close()

    # [删除功能]
    if code == '3':
        delete_name = input("请输入需要删除的姓名：")
        conn4 = sqlite3.connect('data.db')
        c4 = conn4.cursor()
        c4.execute("DELETE from STUDENT WHERE NAME =?", (delete_name,))
        conn4.commit()  # 提交保存更改
        print('delete successful!')
        conn4.close()

    if code == '4':
        break  # 退出循环