
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Cams, Recepients, Events
from . import db
events = Blueprint('events', __name__)


@events.route('/events2')
@login_required
def eventst():
    return 'ok'