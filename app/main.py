# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/cams')
@login_required
def cams():
    return render_template('cams.html', name=current_user.name)

@main.route('/events')
@login_required
def events():
    return render_template('events.html', name=current_user.name)

@main.route('/recepients')
@login_required
def recep():
    return render_template('recepients.html', name=current_user.name)