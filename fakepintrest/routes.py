from flask import render_template, url_for, redirect
from fakepintrest import app, data_base, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepintrest.forms import FormLogin, FormCreateAccount, FormPhoto
from fakepintrest.models import User, Photo
import os
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    
    if form_login.validate_on_submit():
        user = User.query.filter_by(email=form_login.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember=True)
            return redirect(url_for("perfil", id_usuario=user.id))
            
    
    return render_template("homepage.html", form=form_login)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    form_create_account = FormCreateAccount()
    
    
    if form_create_account.validate_on_submit():
            
        password = bcrypt.generate_password_hash(form_create_account.password.data)
        # bcrypt.check_password_hash
        
        user = User(username= form_create_account.username.data, password= password, email= form_create_account.email.data)
        data_base.session.add(user)
        data_base.session.commit()
        
        login_user(user, remember=True)
        return redirect(url_for("perfil", id_usuario=user.id))
        
    return render_template("criar_conta.html", form=form_create_account)


@app.route("/perfil/<id_usuario>",  methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    
    if not int(id_usuario) == int(current_user.id):
        usuario = User.query.get(int(id_usuario))
        return render_template("perfil.html", usuario = usuario, form=None)
    
    
    form_photo = FormPhoto()
    
    if form_photo.validate_on_submit():
        file = form_photo.photo.data
        safe_name = secure_filename(file.filename)
        
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], safe_name)
        file.save(file_path)
        
        photo = Photo(image = safe_name, id_user = int(current_user.id))
        data_base.session.add(photo)
        data_base.session.commit()
        
    
    return render_template("perfil.html", usuario = current_user, form=form_photo)

@app.route("/logout")
@login_required
def logout():
    logout_user() # Pode passar current_user como parametro
    return redirect(url_for("homepage"))



@app.route("/feed")
@login_required
def feed():
    
    photos = Photo.query.order_by(Photo.created_at.desc()).all()
    
    return render_template("feed.html", usuario = current_user, photos = photos)