# ESSE ARQUIVO CUIDA DOS REQUESTS DOS recipients

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Cams, Recepients, Events
from . import db
recepients_bp = Blueprint('recipients', __name__)


@recepients_bp.route('/recepients', methods=['GET'])
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

    recs = Recepients.query.filter_by(code_cam=cam.code).all()

    return render_template('recepients/home.html', cam=cam, recs=recs)

@recepients_bp.route('/recepients_new')
@login_required
def recepients_new():
    cam_id = request.args.get('id')
    if cam_id is None:
        return redirect(url_for('cams.cams'))

    cam = Cams.query.filter_by(code=cam_id).first()
    #if cam.client_code != current_user.id:
    #    return redirect(url_for('cams.cams'))

    return render_template('recepients/new.html', cam=cam)


@recepients_bp.route('/recipients', methods=['POST'])
@login_required
def recepients_post():
    user_id = current_user.id
    cam_id = request.form.get('cam_code')
    modo = request.form.get('modo')
    adress = request.form.get('adress')
    rec_code = request.form.get('rec_code')

    # verificar se essa camera pertence ao usuario
    cam = Cams.query.filter_by(code=cam_id).first()
    if cam.client_code != user_id:
        return redirect(url_for('cams.cams'))

    if rec_code is not None:
        # atualiza o recipient
        rec = Recepients.query.filter_by(code=rec_code).first()
        rec.method = modo
        rec.adress = adress
        db.session.commit()
    else: # cria um novo recipient        
        # adiciona um recepient
        new_recipient = Recepients(code_cam=cam_id, method=modo, adress=adress)
        db.session.add(new_recipient)
        db.session.commit()

    return redirect(url_for('recipients.recepients_cam', id=cam_id))


@recepients_bp.route('/recepients_delete')
@login_required
def recepients_delete():
    user_id = current_user.id
    rec_id = request.args.get('rec_id')

    # pega a camera com o id do recipient
    rec = Recepients.query.filter_by(code=rec_id).first()
    # verifica se achou o recipient
    if rec is None:
        return redirect(url_for('cams.cams'))
    cam_id = rec.code_cam


    cam = Cams.query.filter_by(code=cam_id).first()
    # verifica se achou a camera
    if cam is None:
        return redirect(url_for('cams.cams'))
    
    # verifica se a camera pertence ao usuario
    if cam.client_code != user_id:
        return redirect(url_for('cams.cams'))

    # remove o recipient
    db.session.delete(rec)
    db.session.commit()

    return redirect(url_for('recipients.recepients_cam', id=cam_id))

@recepients_bp.route('/recepients_edit')
@login_required
def recepients_edit():
    user_id = current_user.id
    rec_id = request.args.get('id')

    # pega a camera com o id do recipient
    rec = Recepients.query.filter_by(code=rec_id).first()
    # verifica se achou o recipient
    if rec is None:
        return redirect(url_for('cams.cams'))
    cam_id = rec.code_cam


    cam = Cams.query.filter_by(code=cam_id).first()
    # verifica se achou a camera
    if cam is None:
        return redirect(url_for('cams.cams'))
    
    # verifica se a camera pertence ao usuario
    if cam.client_code != user_id:
        return redirect(url_for('cams.cams'))
    
    return render_template('recepients/new.html', cam=cam, rec=rec)