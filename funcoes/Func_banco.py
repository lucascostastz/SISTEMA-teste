import sqlite3
import mysql.connector


def inserir_dados(self):
        bc = sqlite3.connect('config.db')
        cursor = bc.cursor()
        database = self.janela_login.Tx_Base.text()  
        ip = self.janela_login.Tx_Host.text()  
        porta = self.janela_login.Tx_Porta.text()
        usuario = self.janela_login.Tx_User.text()
        senha = self.janela_login.Tx_Password.text()
        cursor.execute("DELETE FROM config_banco")
        cursor.execute("INSERT INTO config_banco (ip,database,porta,usuario,senha) VALUES('"+ip+"','"+database+"','"+porta+"','"+usuario+"','"+senha+"')")
        bc.commit()
        self.conectar()
    
                   
def conectar(self):
    try:
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
        
        self.janela_login.LB_Erro.clear()
        self.janela_login.LB_Conectado.setText('Conectado!')
        self.janela_login.Tx_Base.clear()
        self.janela_login.Tx_Host.clear()
        self.janela_login.Tx_Password.clear()
        self.janela_login.Tx_Porta.clear()
        self.janela_login.Tx_User.clear()
        self.janela_login.Tx_Senha.clear()
        self.janela_login.LB_Desconectado.clear()      
    except:
        self.janela_login.LB_Erro.setText("Erro ao concectar ao banco de dados!")
        self.janela_login.LB_Desconectado.clear()
        self.janela_login.LB_Conectado.clear()


def desconectar(self):
    try:
        bc = sqlite3.connect('config.db')
        cursor = bc.cursor()
        cursor.execute("DELETE FROM config_banco")
        bc.commit()
        bc.close()
        cursor.close
        self.janela_login.LB_Conectado.clear()
        self.janela_login.LB_Erro.clear()
        self.janela_login.Tx_Base.clear()
        self.janela_login.Tx_Host.clear()
        self.janela_login.Tx_Password.clear()
        self.janela_login.Tx_Porta.clear()
        self.janela_login.Tx_User.clear()
        self.janela_login.Tx_Senha.clear()
        self.janela_login.LB_Desconectado.setText('Desconectado!')
    except:
        self.janela_login.LB_Erro.setText("Erro ao desconcectar o banco de dados!")