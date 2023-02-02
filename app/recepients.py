# ESSE ARQUIVO CUIDA DOS REQUESTS DOS recipients

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Cams, Recepients, Events
from . import db
recepients_bp = Blueprint('recipients', __name__)


@recepients_bp.route('/recepients')
@login_required
def recepients():
    return render_template('recepients.html', name=current_user.name)


@recepients_bp.route('/recepients_cam')
@login_required
def recepients_cam():
    # lista os recipients dessa camera
    cam_id = request.args.get('id')
    if cam_id is None:
        return redirect(url_for('cams.cams'))

    cam = Cams.query.filter_by(code=cam_id).first()
    if cam.client_code != current_user.id:
        return redirect(url_for('cams.cams'))

    rec = Recepients.query.filter_by(code_cam=cam.code).all()
     

    print(rec)

    return render_template('recepients/home.html', name=current_user.name)

@recepients_bp.route('/recepients_new')
@login_required
def recepients_new():
    return 'new'