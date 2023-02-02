# ESSE ARQUIVO CUIDA DOS REQUESTS DOS recipients

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Cams, Recepientes, Events
from . import db
recepients_bp = Blueprint('recipients', __name__)


@recepients_bp.route('/recepients')
@login_required
def recepients():
    return render_template('recepients.html', name=current_user.name)