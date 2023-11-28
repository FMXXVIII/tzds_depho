from fakepintrest import data_base, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(data_base.Model, UserMixin):
    id = data_base.Column(data_base.Integer, primary_key=True)
    username = data_base.Column(data_base.String, nullable=False)
    email = data_base.Column(data_base.String, nullable=False, unique=True)
    password = data_base.Column(data_base.String, nullable=False)
    photo = data_base.relationship("Photo", backref="user", lazy=True)
    

class Photo(data_base.Model):
    id = data_base.Column(data_base.Integer, primary_key=True)
    image = data_base.Column(data_base.String, default="default.png")
    created_at = data_base.Column(data_base.DateTime, nullable=False, default=datetime.utcnow())
    id_user = data_base.Column(data_base.Integer, data_base.ForeignKey("user.id"), nullable=False)