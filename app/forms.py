from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    name_user = StringField('Nombre(s):',validators = [
        DataRequired(), 
        Length(min=3, max=50)
    ])
    last_name_user = StringField('Apellido(s):', validators = [
        DataRequired(),
        Length(max=50)
    ])
    username = StringField('Nombre de usuario', validator=[
        DataRequired(),
        Length(min=3, max=15)
    ])
    email_user = EmailField('Email:', validators=[
        DataRequired(),
        Length(max=50)
    ])
    birth_user = DateField('Nacimiento:', validators=[DataRequired()])
    password_user = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')
