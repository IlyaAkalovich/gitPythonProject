import sqlite3
import random

conn = sqlite3.connect('random.db')
cursor = conn.cursor()


def changetab(*args):
    if len(args) == 1:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (3,))
    elif len(args) == 2 and isinstance(args[1], int):
        cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
    elif len(args) == 3 and not isinstance(args[0], int) and not isinstance(args[1], int) and isinstance(args[2], int):
        cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')
    conn.commit()


cursor.execute('''DROP TABLE tab_1''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')
for i in range(3):
    x = random.randint(1, 9)
    cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (x,))
conn.commit()
cursor.execute(''' SELECT * FROM tab_1''')
oo = cursor.fetchall()
print('before changes')
print(oo)
changetab(42, 54)
changetab('1', '2', 8)
changetab(15)
cursor.execute(''' SELECT * FROM tab_1''')
oo = cursor.fetchall()
print('after changes')
print(oo)
