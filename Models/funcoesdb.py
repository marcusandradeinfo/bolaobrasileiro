import psycopg2

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
        DB_HOST = "localhost"   # ou o IP do servidor PostgreSQL
        DB_PORT = "5432"        # porta padrão do PostgreSQL
        DB_NAME = "BolaoBrasileiro"   # nome do banco de dados
        DB_USER = "postgres" # usuário do banco
        DB_PASS = ""   # senha do banco

        try:
            # Conectar ao banco
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            # Criar um cursor para executar comandos SQL
            cursor = conn.cursor()
            return conn, cursor

        except psycopg2.Error as e:
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
    
    def CadastrarPalpites(self,palpites):   
        sql = f"INSERT INTO tb_palpite (usuario, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20) VALUES {palpites}"
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
