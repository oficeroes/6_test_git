"""SQLite employee-table exercise using temporary, predictable sample data."""

import sqlite3


def main():
    with sqlite3.connect(":memory:") as connection:
        connection.execute(
            "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL, salary REAL NOT NULL)"
        )
        connection.executemany(
            "INSERT INTO employees (name, salary) VALUES (?, ?)",
            [("Lin", 4800), ("Zhou", 6200), ("Chen", 7500)],
        )
        connection.execute("UPDATE employees SET salary = ? WHERE id = ?", (5500, 1))

        print("薪资大于 5000 的员工：")
        for employee in connection.execute(
            "SELECT id, name, salary FROM employees WHERE salary > ? ORDER BY salary DESC",
            (5000,),
        ):
            print(employee)

        connection.execute("DELETE FROM employees WHERE id = ?", (2,))
        print("删除 id=2 后的员工数量：", connection.execute("SELECT COUNT(*) FROM employees").fetchone()[0])


if __name__ == "__main__":
    main()
