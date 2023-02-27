import sqlite3

class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()


    def create_db(self):
        pass


    def add_users(self):
        pass