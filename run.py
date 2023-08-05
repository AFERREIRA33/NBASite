from flask import Flask, render_template
import sqlite3
import db
app = Flask(__name__)
dBCursor = ""


@app.route('/')
def home():
    global dBCursor
    dBCursor = db.connexionDB
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
