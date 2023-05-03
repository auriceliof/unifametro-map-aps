from PyQt5 import uic
from PyQt5 import QtWidgets

def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    usuario1 = "auricelio"
    usuario2 = "marcos"
    usuario3 = "paulo"
    passwd = "123"
    if nome_usuario == usuario1 and senha == passwd \
            or nome_usuario == usuario2 and senha == passwd \
            or nome_usuario == usuario3 and senha == passwd:
        primeira_tela.close()
        logado = nome_usuario
        segunda_tela.label_2.setText(logado)
        segunda_tela.show()
    else:
        primeira_tela.label_4.setText("Dados de login incorretos!")

def run():
    Result.wResult.setText("TEST")

def logout():
    segunda_tela.close()
    Result.close()
    primeira_tela.show()

def TirarFundo():
    exec(open("TirarFundo.py").read())

def Normalizar():
    exec(open("Normalizar.py").read())

def CriarModelo():
    exec(open("CriarModelo.py").read())

def Reconhecer():
    reconhecer = (__import__("Reconhecer"))
    (Result.show())
    (Result.label_2.setText("Reconhecer"))
#    Result.tableWidget.setRowCount(0)
#    for linha, dados in enumerate(reconhecer):
#        Result.tableWidget.setRowCount(linha)
#        for coluna_n, dados in enumerate(dados):
#            Result.tableWidget.setItem(linha,coluna_n(str(dados)))

app=QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
#Result = uic.loadUi("Result.ui")

primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(TirarFundo)
segunda_tela.pushButton_2.clicked.connect(Normalizar)
segunda_tela.pushButton_3.clicked.connect(CriarModelo)
segunda_tela.pushButton_4.clicked.connect(Reconhecer)
segunda_tela.pushButton_5.clicked.connect(logout)

primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

primeira_tela.show()
app.exec()

