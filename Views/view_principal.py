
from main import app
from flask import Flask, render_template, request, redirect, url_for, session,flash
from Controller.ConversorMarkdown import ConvertMarkdownToHTML,ConvertMarkdownToText
from Models.funcoesdb import FuncoesBancoDados


@app.route('/principal')
def principal():
    if 'users' in session:
        session['usuario_palpite'] = None
        user = session['users']  # Obtém o usuário da sessão
        banco = FuncoesBancoDados()
        dados_bd = banco.BuscarPosicao('tb_bolao',user)
        dados_bd = dados_bd[0]
        posicao = dados_bd[1]
        pts = dados_bd[2]
        palpite_enviado = banco.BuscarPalpitesPrincipal(user)
        if palpite_enviado == True:
             btn_palpite = 'true'
        
        return render_template('principal.html', user=user, posicao = posicao, pts = pts)
    else:
        user = None  # Caso não esteja logado
        return redirect(url_for('home'))