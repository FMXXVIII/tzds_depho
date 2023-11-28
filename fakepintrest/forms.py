from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepintrest.models import User

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit_button = SubmitField("Fazer Login")
    
    
    def validate_email(self, email):
        usuario = User.query.filter_by(email = email.data).first()
        
        if not usuario:
            raise ValidationError("Conta não encontrada! Crie uma conta.")
        


class FormCreateAccount(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    password_confirm = PasswordField("Confirmação de Senha", validators=[DataRequired(), Length(6, 20), EqualTo("password")])
    submit_button = SubmitField("Criar Conta")
    
    def validate_email(self, email):
        usuario = User.query.filter_by(email = email.data).first()
        
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar!")
        
    def validade_password_confirm(self, password, password_confirm):
        if password != password_confirm:
            raise ValidationError("As senhas estão diferentes")
        
        
class FormPhoto(FlaskForm):
    photo = FileField("Foto", validators=[DataRequired()])
    submit_button = SubmitField("Enviar")