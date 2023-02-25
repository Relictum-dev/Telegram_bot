import sqlite3
from handlers import general

def connected_db():


    conn = sqlite3.connect('database/users_info.db')
    c = conn.cursor()
    if conn:
        print(str('#') * 40, '\n' '\n'
        'Database connected...' '\n' '\n',
        str('#') * 40)
    else:
        print(str('#') * 20, '\n' '\n'
        'Something wrong', '\n' '\n',
        str('#') * 40)


    c.execute("""CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
                )""")


    c.execute("INSERT INTO contacts VALUES(?, ?, ?, ?)")
    




    conn.commit()
    conn.close()

connected_db()