from flask import Flask, render_template, request, redirect, url_for, session,flash
from Controller.ConversorMarkdown import ConvertMarkdownToHTML,ConvertMarkdownToText
from Models.funcoesdb import FuncoesBancoDados
import os
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta

app = Flask(__name__)
# app.config.from_pyfile('config.py')
app.secret_key = "TESTE"

UPLOAD_FOLDER = 'static\\comprovantes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.permanent_session_lifetime = timedelta(minutes=10)

from Views.view_users import *
from Views.view_principal import *
from Views.view_palpites import *
from Views.view_tabelas import *
from Views.view_financeiro import *

csrf =CSRFProtect(app)

# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
#         SGDB = 'postgres+psycopg2',
#         usuario = 'postgres',
#         senha ='BolaoBrasileiro',
#         servidor = 'localhost'
#     )


if __name__ == '__main__':
    app.run()