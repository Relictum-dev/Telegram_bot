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

async def user_exists(user_id):
    result = conn.execute(f'SELECT * FROM users WHERE user_id = {user_id}').fetchall()
    return bool(len(result))

async def user_check_login(user_id, login):
    cur.execute(
    f"SELECT * FROM users WHERE user_id = {user_id}")
    info = cur.fetchone()
    return login

async def user_check_password(user_id, password):
    cur.execute(
    f"SELECT * FROM users WHERE user_id = {user_id}")
    info = cur.fetchone()
    return password
