# ESSE ARQUIVO CUIDA DOS REQUESTS DAS CAMERAS

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Cams, Recepients, Events
from . import db
cams_bp = Blueprint('cams', __name__)

@cams_bp.route('/cams')
@login_required
def cams():
    cams = Cams.query.filter_by(client_code=current_user.id).all()
    for i in cams:
        print(i.code, i.client_code, i.backup_image, i.backup_img_days, i.type_event, i.label)

    return render_template('cams.html', name=current_user.name,cams=cams)

@cams_bp.route('/cams_new')
@login_required
def cams_new():
    return render_template('cams_new.html', name=current_user.name)

@cams_bp.route('/cams', methods=['POST'])
def cams_post():
    user_id = current_user.id

    backup_image = request.form.get('backup_image')
    backup_img_days = request.form.get('backup_img_days')
    type_event = request.form.get('type_event')
    label = request.form.get('label')

    new_cam = Cams(client_code=user_id, backup_image=backup_image, backup_img_days=backup_img_days, type_event=type_event, label=label)
    db.session.add(new_cam)
    db.session.commit()
    
    return redirect(url_for('cams.cams'))

@cams_bp.route('/cams_edit')
@login_required
def cams_edit():
    cam_id = request.args.get('id')
    cam = Cams.query.filter_by(code=cam_id, client_code=current_user.id).first()
    return render_template('cams_new.html', name=current_user.name, cam=cam)

@cams_bp.route('/cams_delete', methods=['POST'])
@login_required
def cams_delete():    
    Cams.query.filter_by(code=request.form.get('code'), client_code=current_user.id).delete()
    db.session.commit()
    return redirect(url_for('cams.cams'))


@cams_bp.route('/cams_edit', methods=['POST'])
def cams_edit_post():
    """"
        Método de Edição de cameras
    """
    user_id = current_user.id
    cam_code = request.form.get('cam_code')

    # verificar se essa camera é desse cliente
    camera  = Cams.query.filter_by(code=cam_code, client_code=user_id).first()
    print(camera)

    if camera is None:
        return redirect(url_for('cams.cams'))

    camera.backup_image = request.form.get('backup_image')
    camera.backup_img_days = request.form.get('backup_img_days')
    camera.type_event = request.form.get('type_event')
    camera.label = request.form.get('label')
    db.session.commit()
    
    return redirect(url_for('cams.cams'))