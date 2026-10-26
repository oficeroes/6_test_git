"""Small, repeatable Python practice tasks that keep their data in memory."""

import argparse
import sqlite3
from pathlib import Path


def file_summary(path):
    """Read integer values and return count, minimum, maximum, and mean."""
    values = [int(line.strip()) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
    if not values:
        raise ValueError("数据文件不能为空")
    return len(values), min(values), max(values), sum(values) / len(values)


def database_demo():
    """Practice parameterized SQL without changing the repository databases."""
    with sqlite3.connect(":memory:") as connection:
        connection.execute("CREATE TABLE scores (name TEXT PRIMARY KEY, score INTEGER)")
        connection.executemany(
            "INSERT INTO scores VALUES (?, ?)",
            [("林", 88), ("周", 96), ("陈", 91)],
        )
        connection.execute("UPDATE scores SET score = ? WHERE name = ?", (94, "林"))
        return connection.execute(
            "SELECT name, score FROM scores WHERE score >= ? ORDER BY score DESC", (90,)
        ).fetchall()


def main():
    parser = argparse.ArgumentParser(description="Python 六级常见知识点小练习")
    parser.add_argument("topic", choices=("file", "sqlite"), help="选择文件处理或 SQLite")
    parser.add_argument("--path", default="score.txt", help="file 练习所读取的文本文件")
    args = parser.parse_args()

    if args.topic == "file":
        count, low, high, mean = file_summary(args.path)
        print(f"记录数：{count}  最低：{low}  最高：{high}  平均：{mean:.1f}")
    else:
        print("分数不低于 90 的记录：")
        for name, score in database_demo():
            print(f"{name}: {score}")


if __name__ == "__main__":
    main()
