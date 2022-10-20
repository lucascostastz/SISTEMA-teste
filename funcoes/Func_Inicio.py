from PyQt6 import QtCore, QtGui, QtWidgets


def sair_inicio(self):
        self.close()


def expaandir_left_menu(self):
    tamanho = self.janela_inicio.frame_2.width()
    if tamanho == 0:
        novo_tamanho = 100
    else:
        novo_tamanho = 0
        
    self.animacao = QtCore.QPropertyAnimation(self.janela_inicio.frame_2,  b"minimumWidth")
    self.animacao.setStartValue(tamanho)
    self.animacao.setEndValue(novo_tamanho)
    self.animacao.setDuration(350)
    self.animacao.start()   