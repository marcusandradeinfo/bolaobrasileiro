from flask_wtf import FlaskForm
from wtforms import StringField,validators,PasswordField,SubmitField
from wtforms.validators import DataRequired, Regexp, Length


class FormularioCadastro(FlaskForm):
    ## tamanho min de 10 max de 50 - não pode
    nome = StringField("Digite seu nome",[validators.DataRequired(),validators.length(min=10,max=50)]) 
    ### somente números 
    cpf = StringField("Digite seu CPF (Somente Números)",[validators.DataRequired(),Length(min=11,max=11),Regexp(r'^\d+$', message="Apenas números são permitidos!")])
    email = StringField("Digite seu E-mail",[validators.DataRequired(),validators.length(min=10,max=50)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8,max=8)])
    cadastrar = SubmitField('Cadastrar')

class FormularioLogin(FlaskForm):
    login = StringField("Digite seu Login",[validators.DataRequired(),validators.length(min=8,max=12)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8,max=8)])
    entrar = SubmitField('Login')

class FormularioPalpites(FlaskForm):
    pass
