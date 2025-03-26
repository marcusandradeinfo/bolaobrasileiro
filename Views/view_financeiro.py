from main import app
from flask import Flask, render_template, request, redirect, url_for, session,flash
import os
from Controller.ConversorMarkdown import ConvertMarkdownToHTML,ConvertMarkdownToText



@app.route('/pagarbolao')
def pagarbolao():
    return render_template('pagarbolao.html')




@app.route('/regulamento')
def regulamento():
    texto_regulamento = ConvertMarkdownToHTML()
    return render_template('regulamento.html',texto_regulamento = texto_regulamento )





@app.route('/comprovante', methods=['POST',])
def comprovante():
    arquivo = request.files['arquivo']
    # Salvar o arquivo no diretório definido
    caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], arquivo.filename)
    arquivo.save(caminho_arquivo)
    return redirect(url_for('principal'))