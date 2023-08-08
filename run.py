from flask import Flask, render_template, request
import db
import player
import werkzeug.security

app = Flask(__name__)

db.connexionDB()


@app.route('/')
def home():
    db.connexionDB()
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/tryLog', methods=['POST'])
def tryLog():
    name = request.form['name']
    pwd = request.form['password']
    test = db.verify(name, pwd)
    if (test):
        print("true")
    else:
        print("false")
    return render_template('register.html')


@app.route('/tryReg', methods=['POST'])
def tryReg():
    name = request.form['name']
    pwd = request.form['password']
    hashPassword = werkzeug.security.generate_password_hash(pwd)
    db.addData(name, hashPassword)
    return render_template('login.html')


@app.route('/joueurs')
def allPlayerPage():
    allPlayerList = player.getAllPlayer()
    return render_template('player.html', allPlayer=allPlayerList)


if __name__ == '__main__':
    app.run()
