import sqlite3

conn = sqlite3.connect('webhw.db')

item_count = conn.execute('select count(*) from item').fetchone()[0]

if item_count==0:
    with conn:
        with open('data.sql', encoding='utf8') as data_sql:
            conn.executescript(data_sql.read())

conn.close()