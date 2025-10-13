"""sqlite3 sample."""

import sqlite3


if __name__ == "__main__":
    # 创建内存数据库
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # 创建表
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    # 插入数据
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
    # 查询数据
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # 关闭连接
    conn.close()
