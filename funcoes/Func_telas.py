def tela_banco(self):
        self.janela_login.Tx_Base.clear()
        self.janela_login.Tx_Host.clear()
        self.janela_login.Tx_Password.clear()
        self.janela_login.Tx_Porta.clear()
        self.janela_login.Tx_User.clear()
        self.janela_login.Tx_Senha.clear()
        self.janela_login.LB_Conectado.clear()
        self.janela_login.LB_Desconectado.clear()
        self.janela_login.LB_Erro.clear()
        self.janela_login.config_banco.clicked.connect(
            lambda: self.janela_login.stackedWidget.setCurrentWidget(self.janela_login.Banco))
    

def tela_login(self):
    self.janela_login.Tx_Usuario.clear()
    self.janela_login.Tx_Senha.clear()
    self.janela_login.Lb_Info.clear()
    self.janela_login.Lb_Info_banco.clear()
    self.janela_login.Bt_Tela_Login.clicked.connect(
        lambda: self.janela_login.stackedWidget.setCurrentWidget(self.janela_login.Login))


def tela_inicio(self):
        self.janela_inicio.Bt_Inicio.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.janela_inicio.inicio))
        """ self.contar_notificacao() """
        
       
def tela_pacientes(self):
    self.janela_inicio.Bt_Cadastro.clicked.connect(
    lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.janela_inicio.clientes))
    self.listar_clientes()