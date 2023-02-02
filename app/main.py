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



