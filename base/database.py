import sqlite3

class DataBase():

    def __init__(self) -> None:
        self.db = sqlite3.connect('base/database.db')
        self.cursor = self.db.cursor()

    def cretae_table(self) -> None:
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id int, lang str)""")
        self.db.commit()

    def select_user(self, id: int) -> bool:
        self.cursor.execute(f"""SELECT * FROM users WHERE id = {id}""")
        user = self.cursor.fetchone()
        
        return user

    def add_user(self, id: int, lang: str) -> None:
        self.cursor.execute(f"""INSERT INTO users VALUES({id}, "{lang}")""")
        self.db.commit()