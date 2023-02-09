
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Cams, Recepients, Events
from . import db
events = Blueprint('events', __name__)


@events.route('/events2')
@login_required
def eventst():
    return 'ok'


@events.route('/simulate', methods=['GET'])
@login_required
def simulate():
    user_id = current_user.id
    cam_id = request.args.get('id')
    
    #verifica se a camera pertence ao usuario
    cam = Cams.query.filter_by(id=cam_id, user_id=user_id).first()
    if cam is None or cam.user_id != user_id:
        return redirect(url_for('cams.cams'))
    
    #verifica se a camera tem recipients
    recs = Recepients.query.filter_by(cam_id=cam_id).all()

    # percorre os recs
    for rec in recs:
        # cria um novo evento
        event = Events(cam_id=cam_id, rec_id=rec.id, status=1)
        db.session.add(event)
        db.session.commit()
        
    
    return redirect(url_for('cams.cams'))