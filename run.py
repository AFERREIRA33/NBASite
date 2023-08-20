from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy
import player
import team
import match
from werkzeug.security import generate_password_hash, check_password_hash
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'toto'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


app = create_app()


@app.route('/')
def home():
    return render_template('login.html', user=current_user)


@app.route('/login')
def login():
    return render_template('login.html', user=current_user)


@app.route('/register')
def register():
    return render_template('register.html', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/tryLog', methods=['POST'])
def tryLog():
    name = request.form['name']
    pwd = request.form['password']
    from models import User

    user = User.query.filter_by(username=name).first()
    if user is not None:
        if check_password_hash(user.password, pwd):
            flash('logged in succesfully.', category='succes')
            login_user(user, remember=True)
            return redirect(url_for('allPlayerPage', pageNum="1", user=current_user))
    return render_template('login.html', user=current_user)


@app.route('/tryReg', methods=['POST'])
def tryReg():
    name = request.form['name']
    pwd = request.form['password']

    from models import User

    user = User.query.filter_by(username=name).first()
    if user is not None:
        flash('Email already exist', category='error')
    else:

        new_user = User(
            username=name, password=generate_password_hash(pwd, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(user, remember=True)
        flash('Account created.', category='succes')
        return redirect(url_for('joueurs', user=current_user))
    return render_template('register.html', user=current_user)


@app.route('/joueurs', methods=['GET'])
@login_required
def allPlayerPage():
    page = request.args.get('pageNum')
    allPlayerList = player.getAllPlayer(page)
    return render_template('player.html', allPlayer=allPlayerList, actualPage=int(page), user=current_user)


@app.route('/joueur', methods=['POST'])
@login_required
def playerPage():
    idPlayer = request.form['id']
    playerInfo = player.getAPlayer(idPlayer)
    return render_template('aPlayer.html', playerInfo=playerInfo, user=current_user)


@app.route('/equipes', methods=['GET'])
@login_required
def allTeamPage():
    page = request.args.get('pageNum')
    allTeamList = team.getAllTeam(page)
    return render_template('team.html', allTeam=allTeamList, actualPage=int(page), user=current_user)


@app.route('/equipe', methods=['POST'])
@login_required
def equipePage():
    idTeam = request.form['id']
    page = request.form['page']
    teamFirst = request.form['teamFirst']
    teamLast = request.form['teamLast']
    teamInfo, allPlayer, teamFirst, teamLast = team.getATeam(
        idTeam, teamFirst, teamLast, page)
    return render_template('aTeam.html', teamInfo=teamInfo, allPlayer=allPlayer, teamFirst=teamFirst, teamLast=teamLast, user=current_user)


@app.route('/matchs', methods=['GET'])
@login_required
def allMatchPage():
    page = request.args.get('pageNum')
    allMatch, totalPage = match.getAllMatch(page)
    return render_template('match.html', allMatch=allMatch, totalPage=totalPage, actualPage=int(page), user=current_user)


@app.route('/match', methods=['POST'])
@login_required
def aMatch():
    idMatch = request.form['id']
    matchInfo = match.getAMatch(idMatch)
    return render_template('aMatch.html', matchInfo=matchInfo, user=current_user)


if __name__ == '__main__':
    app.run()
