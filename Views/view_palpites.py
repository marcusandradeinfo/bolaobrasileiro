from main import app
from flask import Flask, render_template, request, redirect, url_for, session,flash
from Controller.ConversorMarkdown import ConvertMarkdownToHTML,ConvertMarkdownToText
from Models.funcoesdb import FuncoesBancoDados
from Controller.Forms import FormularioPalpites
### ALTERAÇÕES ENVIAR A LISTA DE POSIÇÕES DE UMA FORMA MELHOR
### VALIDAR DE O USUÁRIO JÁ ENVIOU O PALPITE CASO JÁ TENHA ENVIADO TRAVAR O BOTÃO.

@app.route('/criar_palpites')
def criar_palpites():
    if 'users' in session:
        pos = ['1º','2º','3º','4º','5º','6º','7º','8º','9º','10º','11º','12º','13º','14º','15º','16º','17º','18º','19º','20º']
        dados = pos
        form = FormularioPalpites()
        return render_template('criar_palpites.html',dados = dados,form=form)

@app.route('/enviarpalpite', methods=['POST',])
def enviarpalpite():
    if 'users' in session:
        form = FormularioPalpites(request.form)
        if form.validate_on_submit():
            palpite_usuario = []
            usuario_palpite = session['users']
            #palpite_usuario.append(usuario_palpite)
            
            i = 1
            for i in range(1, 21):
                nome_form = f"equipe_{i}"
                # Certifique-se de que 'equipe_{i}' existe no request
                dados_palpites = request.form.get(nome_form)
                palpite_usuario.append(dados_palpites)


            palpite_usuario = tuple(palpite_usuario)
            
            a = FuncoesBancoDados()
            a.CadastrarPalpites(palpite_usuario,usuario_palpite)
            return redirect(url_for('principal'))


@app.route('/ver_palpites')
def ver_palpites():
    if 'users' in session:
        tb_palpites = {'POS': [], 'Time': [], 'Usuario': []}
        if 'usuario_palpite' in session:
            usuario_palpite = session['usuario_palpite']
            if usuario_palpite != None:
                form = FormularioPalpites(request.form)
                tb_palpites = {'POS': [], 'Time': [], 'Usuario': []}
                tb_usuario = {'Usuario':[]}
                banco = FuncoesBancoDados()
                dados_bd = banco.BuscarTabelaCampeonato()
                for i in dados_bd:
                    tb_palpites['POS'].append(i[0])
                    tb_palpites['Usuario'].append(usuario_palpite)

                dados_bd = banco.BuscarPalpites(usuario_palpite)
                for x in dados_bd[0]:
                    tb_palpites['Time'].append(x)

                usuarios_bolao = banco.BuscarDados('tb_bolao')
                for x in usuarios_bolao:
                    tb_usuario['Usuario'].append(x[3])
                return render_template('ver_palpites.html',form=form,usuariosbolao = tb_usuario, usuario = usuario_palpite ,dados = tb_palpites, zip=zip)        

            else:
                form = FormularioPalpites()
                tb_palpites = {'POS': [], 'Time': [], 'Usuario': []}
                tb_usuario = {'Usuario':[]}
                banco = FuncoesBancoDados()
                dados_bd = banco.BuscarTabelaCampeonato()
                for i in dados_bd:
                    tb_palpites['POS'].append(i[0])
                    tb_palpites['Time'].append(i[1])
                    tb_palpites['Usuario'].append("")

                usuarios_bolao = banco.BuscarDados('tb_bolao')
                for x in usuarios_bolao:
                    tb_usuario['Usuario'].append(x[3])

                return render_template('ver_palpites.html',form=form,usuariosbolao = tb_usuario, usuario = usuario_palpite ,dados = tb_palpites, zip=zip )

@app.route('/checarpalpites', methods=['POST',])
def checarpalpites():
    if 'users' in session:
        form = FormularioPalpites(request.form)
        if form.validate_on_submit():
            participante = request.form['participante']
            session['usuario_palpite'] = participante
            return redirect(url_for('ver_palpites'))






