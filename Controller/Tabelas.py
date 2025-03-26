from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Models.funcoesdb import FuncoesBancoDados



class AtualizarTabelas:
    def __init__(self):
        pass
    
    def CapturarTabelaBrasileiro(self):
        driver = webdriver.Chrome()
        # Configurações do Selenium
        # driver = Options()
        # driver.add_argument("--headless")  # Executa em modo headless (sem abrir o navegador)
        # driver.add_argument("--disable-gpu")
        # driver.add_argument("--no-sandbox")

        # Abre a página
        driver.get("https://ge.globo.com/futebol/brasileirao-serie-a/")
        
        # Espera um pouco para o JavaScript carregar os dados
        driver.implicitly_wait(10)

        # Captura os elementos desejados
        time = driver.find_elements(By.CLASS_NAME, "classificacao__equipes--nome")
        pts = driver.find_elements(By.CLASS_NAME, "classificacao__tabela--linha")


        tb = {"POS":[],"TIME":[],"PTS":[],"J":[],"V":[],"SG":[]}
        i = 1

        for result in time:
            tb['POS'].append(i)
            tb['TIME'].append(result.text)
            i += 1
        for n in pts:
            if '\n' not in n.text:
                valores = list(map(int,n.text.split()))
                tb['PTS'].append(valores[0])
                tb['J'].append(valores[1])
                tb['V'].append(valores[2])
                tb['SG'].append(valores[7])
        driver.quit()
        banco = FuncoesBancoDados()
        for posicao_bd,time_bd,pts_bd,jg_bd,vit_bd,sg_bd, in zip(tb['POS'],tb['TIME'],tb['PTS'],tb['J'],tb['V'],tb['SG']):
            db_banco = banco.AtualizarTabelaBrasileiro(time_bd,pts_bd,jg_bd,vit_bd,sg_bd,posicao_bd)
        
        tb_atualizada = True
        return tb_atualizada


    def AtualizarPontuacao(self):
        pass