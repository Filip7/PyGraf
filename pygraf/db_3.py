import os
import sqlite3


class Db:
    con: sqlite3.Connection
    cur: sqlite3.Cursor

    def __init__(self) -> None:
        db_name = "pygraf.db"
        if os.path.isfile(db_name):
            print("Existing db")
            self.con = sqlite3.connect(f"file:{db_name}?mode=rw", uri=True)
        else:
            print("New db")
            self.con = sqlite3.connect(db_name)
            self.con.execute(
                "CREATE TABLE IF NOT EXISTS color(id INTEGER PRIMARY KEY, hex TEXT UNIQUE, last_access TEXT)"
            )

        self.cur = self.con.cursor()

    def insert_color(self, color) -> int | None:
        insert_cur = self.cur.execute(
            "INSERT INTO color(hex, last_access) VALUES(?, CURRENT_TIMESTAMP) ON CONFLICT(hex) DO NOTHING",
            (color,),
        )

        self.con.commit()

        return insert_cur.lastrowid

    def get_all_colors(self) -> list:
        color_list = self.cur.execute(
            "SELECT * FROM color ORDER BY last_access DESC LIMIT 16"
        ).fetchall()

        return color_list
