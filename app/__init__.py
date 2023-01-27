from flask import Flask
from flask_login import LoginManager
##app = Flask(__name__, template_folder='view') 
#por default use o nome da pasta templates 
from Dados import Database 

db = Database()

def create_app():
    app = Flask(__name__, template_folder='view') 
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    #app.config['SECRET_KEY'] = 'secret-key-goes-here'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return db.getUser(id=user_id)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app()

#from app import admin
#from app import cliente

