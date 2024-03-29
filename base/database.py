import sqlite3

class DataBase():

    def __init__(self) -> None:
        self.db = sqlite3.connect('base/database.db')
        self.cursor = self.db.cursor()

    def cretae_table(self) -> None:
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id int, lang str)""")
        self.db.commit()

    def select_user(self, id: int):
        self.cursor.execute(f"""SELECT * FROM users WHERE id = {id}""")
        user = self.cursor.fetchone()
        
        return user

    def add_user(self, id: int, lang: str) -> None:
        
        user = self.select_user(id)
        
        if user is None:
            self.cursor.execute(f"""INSERT INTO users VALUES({id}, "{lang}")""")
            self.db.commit()
        
    def update_lang(self, id: int, lang: str) -> bool:
        self.cursor.execute("""UPDATE users SET lang = '{}' WHERE id = {}""".format(lang, id))
        self.db.commit()
        
        status = self.select_user(id)
        
        if status[-1] == lang:
            return True
        
        return False