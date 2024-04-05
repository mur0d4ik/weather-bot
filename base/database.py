import sqlite3

class DataBase():

    def __init__(self) -> None:
        self.db = sqlite3.connect('base/base.db')
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user(id int, lang str)''')

    def add_user(self, id: int, language: str):

        if DataBase().select_user(id) is None:
            self.cursor.execute(f'''INSERT INTO user VALUES({id}, '{language}')''')

        else:
            self.cursor.execute(f'''UPDATE user SET lang = '{language}' WHERE id = {id}''')

        self.db.commit()

    def select_user(self, id: int):
        self.cursor.execute(f'''SELECT * FROM user WHERE id = {id}''')
        return self.cursor.fetchone()
    

class WeatherBase():

    def __init__(self) -> None:
        self.db = sqlite3.connect('base/weather-base.db')
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user(id int, options str)''')