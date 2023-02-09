# models.py

from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Events(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    code_cam = db.Column(db.Integer)
    timestamp = db.Column(db.String(30))
    recepients_method = db.Column(db.String(100))
    recepients_adress = db.Column(db.String(100))
    send = db.Column(db.Integer)
    message = db.Column(db.String(1000))

    def formatadata(self):
        # transforma o timestamp em data
        data = ''
        try:
            data = datetime.fromtimestamp(int(self.timestamp)).strftime('%d/%m/%Y %H:%M:%S')
        except:
            pass
        return data

class Cams(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    client_code = db.Column(db.Integer)
    backup_image = db.Column(db.Integer)
    backup_img_days = db.Column(db.Integer)
    type_event = db.Column(db.String(2))
    label = db.Column(db.String(100))



class Recepients(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    code_cam = db.Column(db.Integer)
    method = db.Column(db.String(100))
    adress = db.Column(db.String(100))