# main.py

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/events')
@login_required
def events():
    return render_template('events.html', name=current_user.name)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/profile_edit')
@login_required
def profile_edit():
    return render_template('profile_edit.html', user=current_user)

@main.route('/profile_edit', methods=['POST'])
@login_required
def profile_edit_post():
    user = current_user

    name = request.form.get('name')
    cpfj = request.form.get('cpfj')
    telefone = request.form.get('telefone')

    password = request.form.get('password')
    if  password is None or  len(password) == 0:
        return render_template('profile_edit.html', user=current_user, error='Senha não pode ser vazia ou inválida')
    
    user.name = name
    user.cpfj = cpfj
    user.telefone = telefone
    user.password = generate_password_hash(password, method='sha256')
    db.session.commit()

    return redirect(url_for('cams.cams'))
