from Tela_login import Ui_Tela_login
from Tela_inicio import Ui_Tela_inicio
from Tela_cadastro import Ui_Cadastro
from Tela_editar import Ui_Editar

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys
import sqlite3
import mysql.connector
import time


class Classe_Inicio (QMainWindow):
    from Func_listar import listar_clientes
    from Func_telas import tela_pacientes
    from Func_telas import tela_inicio
    from Func_cadastro import abrir_cadastro
    from Func_Inicio import sair_inicio
    from Func_Inicio import expaandir_left_menu
    def __init__(self):
        super().__init__()
        self.janela_inicio = Ui_Tela_inicio()
        self.janela_inicio.setupUi(self)
        self.cadastro = Classe_cadastro()
        
    
        ################## - BOTÕES - INÍCIO - ##################
        self.janela_inicio.Bt_cadastro.clicked.connect(self.abrir_cadastro)
        self.janela_inicio.Bt_sair.clicked.connect(self.sair_inicio)
        self.janela_inicio.Bt_Expandir.clicked.connect(self.expaandir_left_menu)
        self.janela_inicio.Bt_Inicio.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_inicio()))
        self.tela_inicio()
        self.janela_inicio.Bt_Cadastro.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_pacientes()))
        self.tela_pacientes()




class Classe_cadastro (QMainWindow):
    from Func_cadastro import sair_cadastro, inserir_cadastro, fechar_cadastro
    from Func_listar import listar_clientes
    def __init__(self):
        super().__init__()
        self.janela_cadastro = Ui_Cadastro()
        self.janela_cadastro.setupUi(self)
       


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Classe_Inicio()
    window.show()
    sys.exit(app.exec())