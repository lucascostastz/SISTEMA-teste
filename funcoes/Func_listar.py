import sqlite3
import mysql.connector
from PyQt6 import uic, QtWidgets


def contar_clientes(self):
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
    cursor.execute("SELECT COUNT(nome) FROM saude.pacientes" )
    dados_lido = cursor.fetchall()  
    self.janela_inicio.Lb_Qdt_Clientes.setText(str(dados_lido[0][0])) 
    

def listar_clientes(self):
    self.janela_inicio.tableWidget_2.setColumnWidth(0,19)
    self.janela_inicio.tableWidget_2.setColumnWidth(1,170)
    self.janela_inicio.tableWidget_2.setColumnWidth(2,75)
    self.janela_inicio.tableWidget_2.setColumnWidth(3,85)
    self.janela_inicio.tableWidget_2.setColumnWidth(4,83)
    self.janela_inicio.tableWidget_2.setColumnWidth(5,135)
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
    cursor.execute("SELECT * FROM saude.pacientes")
    dados_lidos = cursor.fetchall()
    self.janela_inicio.tableWidget_2.setRowCount(len(dados_lidos))
    self.janela_inicio.tableWidget_2.setColumnCount(11)
    for a in range(0, len(dados_lidos)):
        for b in range(0, 11):
            self.janela_inicio.tableWidget_2.setItem(
                a, b, QtWidgets.QTableWidgetItem(str(dados_lidos[a][b])))
   