import sqlite3
from aiogram import types
def sql_start():

    global conn, cur

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    if conn:
        print('Подключение в базам данных...')
        print('База данных подключена')
    else:
        print('Не удалось подключится к базе данных')

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL
    );
    """)

    conn.commit()

async def add_user_to_db(user_id, login, password):
    insert_query = f"INSERT INTO users (user_id, login, password) VALUES (?, ?, ?)"
    record_to_insert = (user_id, login, password)
    cur.execute(insert_query, record_to_insert)
    conn.commit()

