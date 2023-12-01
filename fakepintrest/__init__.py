from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

#import os
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
#CONFIGURAR A VARIAVEL "DATABASE_URL" NO AMBIENTE DENTRO DO RENDER => KEY: VARIAVEL, VALUE: LINK DO BANCO
#POSTGRESQL: PIP INSTALL PSYCOPG2

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = "090cbdb0590663e6"
app.config["UPLOAD_FOLDER"] = "static\\fotos_posts"


data_base = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from fakepintrest import routes