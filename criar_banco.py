from fakepintrest import data_base, app
from fakepintrest.models import User, Photo

with app.app_context():
    data_base.create_all()