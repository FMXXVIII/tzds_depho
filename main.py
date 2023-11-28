#pip install flask
#pip install flask-sqlalchemy
#pip install flask-login flask-bcrypt
#pip install flask-wtf
#pip install email-validator


from fakepintrest import app


if __name__ == "__main__":
    app.run(debug=False)