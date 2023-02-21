import sqlite3


async def start_db():
    global db, cursor
    db = sqlite3.connect('database/verified.db')
    cursor = db.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, phone_number TEXT, age TEXT, email TEXT)')


    db.commit()


async def create_profile(user_id):
    user = cursor.execute('SELECT 1 FROM profile WHERE user_id == "{key}"' .format(key = user_id)) .fetchone
    if not user:
        cursor.execute('INSERT INTO profile VALUES (?, ?, ?, ?)', (user_id, '', '', ''))
        db.commit()

async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cursor.execute('UPDATE profile WHERE user_id == "{}" SET phone_number = "{}", age = "{}", email = "{}"'
        .format(user_id, data ['phone_number'],
        data ['age'], data ['email']))

        db.commit()