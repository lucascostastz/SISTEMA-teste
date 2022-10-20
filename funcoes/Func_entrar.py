import sqlite3
import mysql.connector
import time

def entrar(self):
        try:
            global user_1
            user_1 = self.janela_login.Tx_Usuario.text()
            senha2 = self.janela_login.Tx_Senha.text()
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
            cursor.execute(
                "SELECT senha FROM saude.usuarios WHERE usuario ='{}'".format(user_1))
            senha_db = cursor.fetchall()
            banco.close()
            try:
                if senha2 == senha_db[0][0]:
                    self.start()
                    self.close()
                    self.janela_inicio.show()
                else:
                    self.janela_login.Lb_Info.setText("Dados de login incorretos!")
            except:
                self.janela_login.Lb_Info.setText("Dados de login incorretos!")
        except:
            self.janela_login.Lb_Info_banco.setText("Erro ao conectar ao banco de dados!")

    
def start(self):
    self.janela_login.Lb_Info.clear()
    self.janela_login.Lb_Info_banco.clear()
    carregando = self.janela_login.Lb_Info2.setText("Carregando...")
    print(carregando)
    self.janela_login.my_progressBar.show()
    time.sleep(0.5)
    self.janela_login.my_progressBar.setValue(10)
    time.sleep(0.5)
    self.janela_login.my_progressBar.setValue(20)
    time.sleep(0.5)
    self.janela_login.my_progressBar.setValue(30)
    time.sleep(0.5)
    aguarde = self.janela_login.Lb_Info2.setText("Aguarde...")
    print(aguarde)
    self.janela_login.my_progressBar.setValue(40)
    time.sleep(0.5)
    self.janela_login.my_progressBar.setValue(50)
    time.sleep(0.5)
    self.janela_login.my_progressBar.setValue(60)
    time.sleep(0.5)
    iniciando = self.janela_login.Lb_Info2.setText("Iniciando o sistema...")
    print(iniciando)
    self.janela_login.my_progressBar.setValue(70)
    time.sleep(0.5)
    self.janela_login.my_progressBar.setValue(80)
    time.sleep(0.3)
    self.janela_login.my_progressBar.setValue(90)
    time.sleep(0.1)
    self.janela_login.my_progressBar.setValue(100)
    time.sleep(0.5)
    self.janela_login.my_progressBar.close() 