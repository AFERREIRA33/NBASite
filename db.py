import sqlite3


def connexionDB():
    conn = sqlite3.connect('NBADB')
    c = conn.cursor()
    c.execute('''
          CREATE TABLE IF NOT EXISTS Account
          ([id] INTEGER PRIMARY KEY, [name] TEXT, [password] TEXT)
          ''')
    return c
