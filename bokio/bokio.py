from flask import Flask, request
from flask import render_template

from bokio.route.editor import editor
from bokio.route.home import home
from bokio.route.index import index
from bokio.route.auth import auth
from bokio.route.profile import profile

#from flask_github import GitHub

from flask_sqlalchemy import SQLAlchemy

from bokio.model.model import db, User


app = Flask(__name__)
app.secret_key = 'thisisthat'  # Change this!

app.register_blueprint(editor.router)
app.register_blueprint(home.router)
app.register_blueprint(index.router)
app.register_blueprint(auth.router)
app.register_blueprint(profile.router)

#app.config['GITHUB_CLIENT_ID'] = 'a36075edd8c1d5e8e6da'
#app.config['GITHUB_CLIENT_SECRET'] = 'c6363b0fcbc4312da657650895ab2d8448614a19'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

#github = GitHub(app)

db.init_app(app)


from flask_login import LoginManager


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
