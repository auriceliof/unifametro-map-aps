from PyQt5 import uic
from PyQt5 import QtWidgets

def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nome_usuario == "auricelio" and senha == "123":
        primeira_tela.close()
        segunda_tela.show()
    else:
        primeira_tela.label_4.setText("Dados de login incorretos!")

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
    (__import__("Reconhecer"))
    (Result.show())

app=QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
Result = uic.loadUi("Result.ui")

primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(TirarFundo)
segunda_tela.pushButton_2.clicked.connect(Normalizar)
segunda_tela.pushButton_3.clicked.connect(CriarModelo)
segunda_tela.pushButton_4.clicked.connect(Reconhecer)

primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

segunda_tela.show()
app.exec()

