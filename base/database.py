import sqlite3

from keyboards.inline import switchs

class Users():
    def __init__(self) -> None:
        self.db = sqlite3.connect('base\database.db')
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id int, lang str, settings str)""")

    def search_user(self, id: int) -> tuple:
        """
        Поиск юзера по базе\n
        id - от телеграмм аккаунта юзера
        """

        self.cursor.execute("""SELECT * FROM users WHERE id = ?""", (id,))
        return self.cursor.fetchone()

    def add_user(self, id: int, lang: str = 'en', settings: str = 'no'):
        """
        Добавить юзера в бд, еслт его нет!\n
        id - от телеграмм аккаунта юзера\n
        lang - дефолт "en"\n
        settings - дефолт "no"
        """

        self.cursor.execute("""INSERT INTO users(id, lang, settings) VALUES(?, ?, ?)""", (id, lang, settings))
        self.db.commit()

    def update_lang(self, id: int, lang: str):
        """
        Обновить данные о языке!\n
        id - от телеграмм аккаунта юзера\n
        lang - выбранный юзером язык
        """

        self.cursor.execute("""UPDATE users SET lang = ? WHERE id = ?""", (lang, id))
        self.db.commit()

    def update_settings(self, id: int, settings: str = 'yes'):
        """
        Обновить данные о языке!\n
        id - от телеграмм аккаунта юзера\n
        settings - изменит значение settings
        """

        self.cursor.execute("""UPDATE users SET settings = ? WHERE id = ?""", (settings, id))
        self.db.commit()

    def check_update_lang(self, id: int, lang: str):
        """
        Проверить изменен язык в бд!\n
        id - от телеграмм аккаунта юзера\n
        lang - выбранный юзером язык
        """

        if self.search_user(id)[1] == lang:
            return 'changed'
        
        return 'eror-lang'
    

class UserSettings():

    def __init__(self) -> None:
        self.db = sqlite3.connect('base\settings_database.db')
        self.cursor = self.db.cursor()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS current(id int, lat_lon str, last_updated str, temp_c str, temp_f str, condition str, humidity str)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS forecast(id int, lat_lon str, sunrise str, sunset str, moonrise tsr, moonset str, max_min_temp_c str, max_min_temp_f str, condition str, humidity str, wind_kph str, wind_mph str)""")

    def add_user_current(self, id: int, lat_lon: str = '✅', last_updated: str = '✅', temp_c: float = '✅', temp_f: float = '✅', condition: str = '✅', humidity: int = '✅'):
        """
        Добавить юзера в бд, еслт его нет!\n
        id - от телеграмм аккаунта юзера\n
        lat_lon - широта и долгота\n
        last_updated - время последнего обновы данных\n
        temp_c | temp_f - тепмература в °C | °F\n
        condition - описание погоды (солнечно, пасмурно ...)\n
        humidity - влажность
        """

        if not self.search_user(id):
            self.cursor.execute("""INSERT INTO current(id, lat_lon, last_updated, temp_c, temp_f, condition, humidity)
                                VALUES(?, ?, ?, ?, ?, ?, ?)""", (id, lat_lon, last_updated, temp_c, temp_f, condition, humidity))
            self.db.commit()

    def add_user_forecast(self, id: int, sunrise: str = '✅', sunset: str = '✅', moonrise: str = '✅', moonset: str = '✅', max_min_temp_c: str = '✅', max_min_temp_f: str = '✅', condition: str = '✅', humidity: str = '✅', wind_kph: str = '✅', wind_mph: str = '✅'):
        """
        Добавить юзера в бд, еслт его нет!\n
        id - от телеграмм аккаунта юзера\n
        sunrise - восход\n
        sunset - закат\n
        moonrise - восход луны\n
        moonset - закат луны\n
        max_min_temp_c|max_min_temp_f - макс, мин температура в °C|°F\n
        condition - описание погоды (солнечно, пасмурно ...)\n
        humidity - влажность
        wind_kph|wind_mph - ветер в км|миль час
        """

        self.cursor.execute("""INSERT INTO forecast(id, sunrise, sunset, moonrise, moonset, max_min_temp_c, max_min_temp_f, condition, humidity, wind_kph, wind_mph)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (id, sunrise, sunset, moonrise, moonset, max_min_temp_c, max_min_temp_f, condition, humidity, wind_kph, wind_mph))
        
        self.db.commit()


    def search_user(self, id: int, table: str = 'current'):
        """
        Поиск юзера по базе\n
        id - от телеграмм аккаунта юзера
        """
        
        self.cursor.execute(f"""SELECT * FROM {table} WHERE id = ?""", (id,))
        return self.cursor.fetchone()
    
    def search_user_param(self, id: int, param: str, table: str = 'current') -> tuple:
        """
        Поиск юзера по базе\n
        id - от телеграмм аккаунта юзера\n
        param - 
        """

        self.cursor.execute(f"""SELECT {param} FROM {table} WHERE id = ?""", (id,))
        return self.cursor.fetchone()
        
    def update_settings(self, id: int, params_name: str, switch: str, table: str = 'current'):
        """
        Обновить данные о настройках юзера!\n
        id - от телеграмм аккаунта юзера
        """

        self.cursor.execute(f"""UPDATE {table} SET {params_name} = ? WHERE id = ?""", (switch, id))
        
        self.db.commit()

    def check_update_lang(self, id: int, param: str, switch: str, table: str = 'current'):
        """
        Проверить изменен язык в бд!\n
        id - от телеграмм аккаунта юзера\n
        param - параметр который нужно проверить\n
        """

        if switch in self.search_user_param(id, param, table):
            return switchs[switch]
        
        return 'eror-lang'


def activate_func():
    """
    Запустит функиции для создание таблиц
    """
    Users().create_table()
    UserSettings().create_tables()