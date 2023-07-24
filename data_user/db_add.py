

import sqlite3 as sq

def send_data_register(login,password,f,m,agree):
    print('ok db')

    with sq.connect('data_user/users.db') as conn:
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id  INTEGER PRIMARY KEY,
        login TEXT,
        password TEXT,
        m INTEGER ,
        f INTEGER,
        agree INTEGER 
         )""")



    with sq.connect('data_user/users.db') as conn:
        c = conn.cursor()
        c.execute(f"INSERT INTO users VALUES (NULL,?,?,?,?,?)", (login, password, f, m, agree))



