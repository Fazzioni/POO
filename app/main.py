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


@main.route('/cams')
@login_required
def cams():
    cams = Cams.query.filter_by(client_code=current_user.id).all()
    for i in cams:
        print(i.code, i.client_code, i.backup_image, i.backup_img_days, i.type_event, i.label)

    return render_template('cams.html', name=current_user.name,cams=cams)

@main.route('/cams_new')
@login_required
def cams_new():
    return render_template('cams_new.html', name=current_user.name)


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

@main.route('/cams', methods=['POST'])
def cams_post():
    user_id = current_user.id

    backup_image = request.form.get('backup_image')
    backup_img_days = request.form.get('backup_img_days')
    type_event = request.form.get('type_event')
    label = request.form.get('label')

    new_cam = Cams(client_code=user_id, backup_image=backup_image, backup_img_days=backup_img_days, type_event=type_event, label=label)
    db.session.add(new_cam)
    db.session.commit()
    
    return redirect(url_for('main.profile'))

@main.route('/cams_edit')
@login_required
def cams_edit():
    return 'main.cams_edit'


@main.route('/cams_delete', methods=['POST'])
@login_required
def cams_delete():    
    Cams.query.filter_by(code=request.form.get('code'), client_code=current_user.id).delete()
    db.session.commit()
    return redirect(url_for('main.cams'))


