import sqlite3


def save_user(name, age):
    # create a sqlite connection
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)",
                   (name, age))
    conn.commit()
    conn.close()
