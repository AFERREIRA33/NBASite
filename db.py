import sqlite3
import werkzeug.security


def connexionDB():
    conn = sqlite3.connect('NBADB')
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS Account([id] INTEGER PRIMARY KEY, [name] TEXT, [password] TEXT)''')
    c.close()


def addData(name, password):
    conn = sqlite3.connect('NBADB')
    c = conn.cursor()
    result = c.execute('''Select name FROM Account WHERE name = ?''', [name])
    if (not result.fetchall()):
        c.execute(
            "INSERT INTO Account (name, password) VALUES (?, ?)", (name, password))
        conn.commit()
        c.close()


def verify(name, password):
    conn = sqlite3.connect('NBADB')
    c = conn.cursor()
    result = c.execute(
        '''Select name, password FROM Account WHERE name = ?''', [name])
    result = result.fetchall()
    c.close()
    if (len(result) > 0):
        return werkzeug.security.check_password_hash(result[0][1], password)
    return False
