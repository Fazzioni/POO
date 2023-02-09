
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Cams, Recepients, Events
from . import db
from .datas import get_current_timestamp, get_current_time
from . import email
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
    cam = Cams.query.filter_by(code=cam_id, client_code=user_id).first()
    if cam is None or cam.client_code != user_id:
        return redirect(url_for('cams.cams'))
    
    #verifica se a camera tem recipients
    recs = Recepients.query.filter_by(code_cam=cam_id).all()

    # cria a mensagem para enviar

    obj_text =  'Pessoa detectada' if cam.type_event == 'Pessoa'  else 'Carro detectado'

    # formata a data e hora
    
    message = f'[{get_current_time().strftime("%d/%m/%Y %H:%M:%S")}] { obj_text} na camera {cam.label}'
    # percorre os recs
    for rec in recs:
        # cria um novo evento
        enviado = False

        if rec.method == 'email': # envia o email
            if '@' in rec.adress:
                    enviado = email.send(rec.adress, message, '[ POO ] - BIA - Alerta de movimento')

        # cria um novo evento
        event = Events(code_cam=cam_id, 
                           timestamp = get_current_timestamp(True),
                           recepients_method = rec.method,
                           recepients_adress = rec.adress,
                           send = 1 if enviado == True else 0,
                           message = message,
                       )
        # salva no banco de dados
        db.session.add(event)
        db.session.commit()
    return redirect(url_for('cams.cams'))