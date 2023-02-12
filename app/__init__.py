# init.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from .e_mail import Email
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

email = Email()

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    #print(os.path.join(basedir, 'static')+os.sep )
    app = Flask(__name__,  static_folder=os.path.join(basedir, 'static')+os.sep, )
  
    app.config['SECRET_KEY'] = 'ProgramacaoOrientadaObjetos'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

    db.init_app(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .events import events as events_blueprint
    app.register_blueprint(events_blueprint)

    from .cams import cams_bp as cams_blueprint
    app.register_blueprint(cams_blueprint)

    from .recepients import recepients_bp as recepients_blueprint
    app.register_blueprint(recepients_blueprint)
    
    return app

app = create_app()