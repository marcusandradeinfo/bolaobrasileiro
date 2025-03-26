from flask import Flask, render_template, request, redirect, url_for, session,flash
from Controller.ConversorMarkdown import ConvertMarkdownToHTML,ConvertMarkdownToText
from Models.funcoesdb import FuncoesBancoDados
import os
import uuid
from flask_sqlalchemy import SQLAlchemy
from main import app


@app.route('/tabela_bolao')
def tabela_bolao():
    if 'users' in session:
        banco = FuncoesBancoDados()
        dados_bolao = banco.BuscarDados('tb_bolao')
        colunas = ["id", "posicao", "pts", "usuario"]
        dados = [dict(zip(colunas, row)) for row in dados_bolao]
        return render_template('tabela_bolao.html',dados_bolao = dados)


@app.route('/tabela_brasileiro')
def tabela_brasileiro():
    if 'users' in session:
        tb_brasileiro = {'POS': [], 'Time': [], 'PTS': [], 'J': [], 'V': [], 'SG': []}
        banco = FuncoesBancoDados()
        dados_bd = banco.BuscarTabelaCampeonato()
        for i in dados_bd:
            tb_brasileiro['POS'].append(i[0])
            tb_brasileiro['Time'].append(i[1])
            tb_brasileiro['PTS'].append(i[2])
            tb_brasileiro['J'].append(i[3])
            tb_brasileiro['V'].append(i[4])
            tb_brasileiro['SG'].append(i[5])
        return render_template('tabela_brasileiro.html',tb_brasileiro = tb_brasileiro, zip=zip)
