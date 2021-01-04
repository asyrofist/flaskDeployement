from flask import Flask #import library flask
from flask_sqlalchemy import SQLAlchemy # import library sqlalchemy sebagai database
from flask_bcrypt import Bcrypt # import library bcrypt sebagai enkripsi
from flask_login import LoginManager # import library login manager 
from flask_mail import Mail # import library mail sebagai mail function
from flaskblog.config import Config # library config sebagai konfigurasi


db = SQLAlchemy() # membuat variable database sqlalchemy
bcrypt = Bcrypt() # membuat variable database bcrypt
login_manager = LoginManager() # membuat variable loginmanager
login_manager.login_view = 'users.login' # membuat variablle login view
login_manager.login_message_category = 'info' # membuat variable info 
mail = Mail() # membuat variable mail


def create_app(config_class=Config): # membuat fungsi create app, berdasarkan konfigurasi
    app = Flask(__name__) # menginisalisasi flask dengan nama  app
    app.config.from_object(Config) # menginisialisasi konfigurasi app

    db.init_app(app) # menginsialisa app berdasarkan db
    bcrypt.init_app(app) # menginisalisasi app berdasarkan bcrypt
    login_manager.init_app(app) # menginisialisasi app berdasarkan login manager
    mail.init_app(app) # menginisialisasi app berdasarkan mail.

    from flaskblog.users.routes import users # import library user
    from flaskblog.posts.routes import posts # import library posts
    from flaskblog.main.routes import main # import library main 
    from flaskblog.errors.handlers import errors # import library erros
    app.register_blueprint(users) # masukkan nilai users tersbut ke blueprint 
    app.register_blueprint(posts) # masukkan nilai posts tersebut ke blueprint
    app.register_blueprint(main) # masukkan nilai main tersebut ke blueprint
    app.register_blueprint(errors) # masukkan nilai erros tersebut ke blueprint

    return app # mengembalikan value ke app
