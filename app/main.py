# main.py

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Cams, Recepientes, Events
from . import db
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/events')
@login_required
def events():
    return render_template('events.html', name=current_user.name)

@main.route('/recepients')
@login_required
def recepients():
    return render_template('recepients.html', name=current_user.name)

@main.route('/recepients', methods=['POST'])
def recepients_post():
    user = current_user.name
    print('user = ', user.name)

    #email = request.form.get('email')
    #password = request.form.get('password')
    #remember = True if request.form.get('remember') else False
    #
    #user = User.query.filter_by(email=email).first()
    #
    ## check if user actually exists
    ## take the user supplied password, hash it, and compare it to the hashed password in database
    #if not user or not check_password_hash(user.password, password): 
    #    flash('Please check your login details and try again.')
    #    return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page
    #
    ## if the above check passes, then we know the user has the right credentials
    #login_user(user, remember=remember)
    #return redirect(url_for('main.profile'))
