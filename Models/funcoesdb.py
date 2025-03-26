import mysql.connector

class FuncoesBancoDados:
    def __init__(self):
        pass

    def ConexaoDB(self):
        ## endpoit bolaobrasileiro.cmdmioaeoe41.us-east-1.rds.amazonaws.com
        ##BolaoBrasileiroAWS
        ## dados banco nuvem
        ##dbbolaobrasileirao
        ##marcusandradeinf
        ## AQVA5xgn5RMkZQVR
        ##porta - 5432

        # Configuração da conexão
        DB_HOST = "dbbolaobrasil.mysql.dbaas.com.br"   # ou o IP do servidor PostgreSQL
        DB_PORT = "3306"        # porta padrão do PostgreSQL
        DB_NAME = "dbbolaobrasil"   # nome do banco de dados
        DB_USER = "dbbolaobrasil" # usuário do banco
        DB_PASS = "M@TRixzh0015"   # senha do banco

        try:
            # Conectar ao banco
            conn = mysql.connector.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            # Criar um cursor para executar comandos SQL
            cursor = conn.cursor()
            return conn, cursor

        except mysql.connector.Error as e:
            print("Erro ao conectar ao PostgreSQL:", e)


    def AtualizarTabelaBrasileiro(self,time,pts,jogos,vitorias,saldo,pos):
        conexao,cursor = self.ConexaoDB()
        query = (f"UPDATE tb_campeonato SET time='{time}', pts='{pts}', jogos='{jogos}', vitoria='{vitorias}', saldo='{saldo}' WHERE id ='{pos}'")
        result = cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()
        return result


    def CadastrarUsuario(self,nome,usuario,senha,email,data_nascimento,cpf,concordo):
        conexao,cursor = self.ConexaoDB()
        result = cursor.execute (f"INSERT INTO tb_usuarios (nome, usuario, senha, email ,data_nascimento, cpf, termo_aceito) VALUES {nome,usuario,senha,email,data_nascimento, cpf,concordo}")
        conexao.commit()
        cursor.close()
        conexao.close()
        return result
    
    def CadastrarPalpites(self,palpites,usuario):   
        sql = f"UPDATE tb_palpite SET pos1 = '{palpites[0]}', pos2 = '{palpites[1]}',pos3 = '{palpites[2]}', pos4 = '{palpites[3]}', pos5 = '{palpites[4]}', pos6 = '{palpites[5]}', pos7 = '{palpites[6]}', pos8 = '{palpites[7]}', pos9 = '{palpites[8]}', pos10 = '{palpites[9]}', pos11 = '{palpites[10]}', pos12 = '{palpites[11]}', pos13 = '{palpites[12]}', pos14 = '{palpites[13]}', pos15 = '{palpites[14]}', pos16 = '{palpites[15]}', pos17 = '{palpites[16]}', pos18 = '{palpites[17]}', pos19 = '{palpites[18]}', pos20 = '{palpites[19]}' WHERE usuario = '{usuario}'"
        conexao, cursor = self.ConexaoDB()
        cursor.execute(sql,)  # Aqui está o ajuste
        conexao.commit()
        cursor.close()
        conexao.close()


    
    def BuscarDados(self,tabela):
        conexao,cursor = self.ConexaoDB()
        cursor.execute(f"SELECT * FROM {tabela}")
        result = cursor.fetchall()
        cursor.close()
        conexao.close()
        return result
    
    def BuscarTabelaCampeonato(self):
        conexao,cursor = self.ConexaoDB()
        query = "select posicao,time,pts,jogos,vitoria,saldo from tb_campeonato"
        cursor.execute(query,)
        result = cursor.fetchall()
        cursor.close()
        conexao.close()
        return result
    
    def BuscarPalpites(self,usuario):
        conexao,cursor = self.ConexaoDB()
        query = "select * from tb_palpite where usuario = %s;"
        cursor.execute(query,(usuario, ))
        result = cursor.fetchall()
        dados_filtrados = [linha[3:] for linha in result]
        cursor.close()
        conexao.close()
        return dados_filtrados
    
    def BuscarPalpitesPrincipal(self,usuario):
        conexao,cursor = self.ConexaoDB()
        query = "select * from tb_palpite where usuario = %s;"
        cursor.execute(query,(usuario, ))
        result = cursor.fetchall()
        dados_filtrados = [linha[3:] for linha in result]
        palpitou = None 
        for i in dados_filtrados:
            if i[0] == 'vazio':
                palpitou = False
                break
            else:
                palpitou = True
                break
        cursor.close()
        conexao.close()
        return palpitou
    
    def BuscarUsuario(self,tabela,usuario,senha):
        usuario = usuario.replace('"',"'")
        senha = senha.replace('"',"'")
        conexao,cursor = self.ConexaoDB()
        # Query segura com placeholders (%s)
        query = f"SELECT * FROM {tabela} WHERE usuario LIKE %s AND senha = %s"
        # Executar query com parâmetros
        cursor.execute(query, (usuario, senha))  # LIKE apenas no usuário (se necessário)
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            conexao.close()
            return result
        else:
            return None
    
    def BuscarPosicao(self,tabela,usuario):
        conexao,cursor = self.ConexaoDB()
        # Query segura com placeholders (%s)
        query = f"SELECT * FROM {tabela} WHERE usuario = %s"
        # Executar query com parâmetros
        cursor.execute(query, (usuario,))  # LIKE apenas no usuário (se necessário)
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            conexao.close()
            return result
        else:
            return None




### criação de tabelas ####

### tabela de usuários

# CREATE TABLE tb_usuarios (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     senha TEXT NOT NULL,
#     data_nascimento TEXT NOT NULL,
#     cpf TEXT NOT NULL,
#     aceito_termo TEXT NOT NULL);


#### tabela bolão com relacionamento

# CREATE TABLE tb_bolao (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     usuario TEXT NOT NULL,
#     pts INTEGER DEFAULT 0,
#     posicao INTEGER DEFAULT 0,
#     FOREIGN KEY (usuario) REFERENCES tb_usuarios(nome) ON DELETE CASCADE
# );




















# a = FuncoesBancoDados()
# resultado = a.BuscarDados('usuarios')
# print(resultado)


##### modelo utilizando SQL ALCHEMY ####


# class Pessoa(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     senha = db.Column(db.String(100), nullable=False)
#     data_nascimento = db.Column(db.String(10), nullable=False)  # Formato: 'YYYY-MM-DD'
#     cpf = db.Column(db.String(11), unique=True, nullable=False)  # CPF sem formatação
#     concordo = db.Column(db.Boolean, nullable=False)

#     def __repr__(self):
#         return f"<Pessoa {self.nome}>"


# def CadastrarUsuario(nome, email, senha, data_nascimento, cpf, concordo):
#     # Criando uma nova instância do modelo Pessoa
#     nova_pessoa = Pessoa(nome=nome, email=email, senha=senha, 
#                          data_nascimento=data_nascimento, cpf=cpf, concordo=concordo)
    
#     # Adicionando ao banco de dados e confirmando a transação
#     db.session.add(nova_pessoa)
#     db.session.commit()

#     print(f"Usuário {nome} cadastrado com sucesso!")
