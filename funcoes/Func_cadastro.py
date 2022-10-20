import sqlite3
import mysql.connector



def abrir_cadastro(self):
    self.cadastro.show()


def sair_cadastro(self):
    self.close()


def inserir_cadastro(self):
    bc = sqlite3.connect('config.db')
    cursor = bc.cursor() 
    cursor.execute("SELECT *FROM config_banco")
    dados_lidos = cursor.fetchall()
    ip = dados_lidos[0][1]
    database = dados_lidos[0][2]
    porta = dados_lidos[0][3]
    usuario = dados_lidos[0][4]
    senha = dados_lidos[0][5]
    banco = mysql.connector.connect(
        host=ip,
        user=usuario,
        port=porta,
        password=senha,
        database=database)
    cursor = banco.cursor() 
    nome = self.janela_cadastro.tx_Nome.text()
    cpf = self.janela_cadastro.tx_Cpf.text()
    sus = self.janela_cadastro.tx_Sus.text()
    telefone = self.janela_cadastro.tx_Telefone.text()
    email = self.janela_cadastro.tx_Email.text()
    encaminhamento = self.janela_cadastro.tx_Ecaminhamento.text()
    especialidade = self.janela_cadastro.tx_Especialidade.text()
    acompanhante = self.janela_cadastro.tx_Acompanhante.text()
    almoco = self.janela_cadastro.tx_Almoco.text()
    local_atendimento = self.janela_cadastro.tx_Local_atendimento.text()
    cursor.execute("INSERT INTO saude.pacientes (nome,cpf,sus,telefone,email,encaminhamento,especialidade,acompanhante,almoco,local_atendimento) VALUES('"+nome+"','"+
                   cpf+"','"+sus+"','"+telefone+"','"+email+"','"+encaminhamento+"','"+especialidade+"','"+acompanhante+"','"+almoco+"','"+local_atendimento+"')")
    banco.commit()
    banco.close()
    self.fechar_cadastro()


def fechar_cadastro(self):
    self.janela_cadastro.tx_Nome.clear()
    self.janela_cadastro.tx_Cpf.clear()
    self.janela_cadastro.tx_Sus.clear()
    self.janela_cadastro.tx_Telefone.clear()
    self.janela_cadastro.tx_Email.clear()
    self.janela_cadastro.tx_Ecaminhamento.clear()
    self.janela_cadastro.tx_Especialidade.clear()
    self.janela_cadastro.tx_Acompanhante.clear()
    self.janela_cadastro.tx_Almoco.clear()
    self.janela_cadastro.tx_Local_atendimento.clear()