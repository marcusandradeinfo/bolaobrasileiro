from main import app
from flask import Flask, render_template, request, redirect, url_for, session,flash
from Models.funcoesdb import FuncoesBancoDados
from Controller.ConversorMarkdown import ConvertMarkdownToHTML,ConvertMarkdownToText
from Controller.Forms import FormularioCadastro, FormularioLogin
from Controller.VariaveisSessao import clear_session


@app.route('/')
def home():
    clear_session()
    form = FormularioLogin()
    return render_template('index.html',form=form)

@app.route('/login', methods=['POST',])
def login():
    form = FormularioLogin(request.form)
    if form.validate_on_submit():
        usuario = form.login.data
        senha = form.senha.data
        banco = FuncoesBancoDados()
        dados_bd = banco.BuscarUsuario('tb_usuarios',usuario,senha)
        if dados_bd != None:
            session['users'] = usuario
            return redirect(url_for('principal'))
        else:
            flash("Usuario ou Senha incorretos!", "danger")  # Mensagem de erro
            return redirect(url_for('home'))
    else:
        print(form.errors)
        flash(form.errors, "danger")
        return redirect(url_for('home'))
    
    

@app.route('/cadastro')
def cadastro():
    form = FormularioCadastro()
    texto_regulamento = ConvertMarkdownToText()
    return render_template('cadastro.html',texto_regulamento = texto_regulamento, form = form )

@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    form = FormularioCadastro(request.form)
    if not form.validate_on_submit():
        print(form.errors)
        flash(form.errors, "danger")
        return redirect(url_for('cadastro'))
    else:
        nome = form.nome.data
        cpf = form.cpf.data
        email = form.email.data
        data_nascimento = str(request.form['data_nacimento'])
        nome_usuario = nome[0:4]+data_nascimento[0:2]+cpf[8:10]
        nome_usuario = nome_usuario.lower()
        senha = form.senha.data
        aceito_termo = True
        cadastrar_bd =FuncoesBancoDados()
        resultcadastro = cadastrar_bd.CadastrarUsuario(nome,nome_usuario,senha,email,data_nascimento,cpf,aceito_termo)
        print(resultcadastro)
        return redirect(url_for('home'))

@app.route('/sair')
def sair():
    clear_session()
    return redirect(url_for('home'))

