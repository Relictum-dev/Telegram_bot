import sqlite3

async def db_start():
    global db, cursor
    
    db = sqlite3.connect('profile.db')
    cursor = db.cursor()
    
    if db:
        print('Подключение в базе данных...')
        print('База данных подключена')
    else:
        print('Ошибка подключения')

    cursor.execute("CREATE TABLE IF NOT EXISTS profile (id INTEGER PRIMARY KEY AUTOINCREMENT , user_id TEXT, username TEXT, password TEXT, note TEXT)")
    db.commit()


async def create_profile(user_id):
    user = cursor.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key = user_id)).fetchone()
    if not user:
        cursor.execute("INSERT INTO profile VALUES (?, ?, ?, ?)", (user_id, '', '', '',))
        db.commit()

async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cursor.execute("UPDATE profile SET name = '{}', password = '{}', note = '{}' WHERE user_id == '{}'".format(
             data['name'], data['password'], data['note'], user_id))
        db.commit()