from PyQt5.QtWidgets import QMainWindow
from models.algoritmoRecursivo import AlgoritmoRecursivo
from views.Ui_home_view import Ui_MainWindow


class HomeController(QMainWindow):
    def __init__(self):
        super(HomeController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_invalido.setVisible(False)
        self.ui.label_valido.setVisible(False)
        self.ui.pushButton_verificar.clicked.connect(self.validarComando)


    def validarComando(self):
        texto = self.ui.lineEdit_texto.text()
        texto = texto.replace(' ', '')
        lista_analizar = list(texto)
        print(lista_analizar)

        algoritmoRecursivo =  AlgoritmoRecursivo(lista_analizar)
        evaluarCadena = algoritmoRecursivo.produccion()
        print(evaluarCadena)

        if(evaluarCadena == "no paso"):
            self.ui.label_valido.setVisible(False)
            self.ui.label_invalido.setVisible(True)
        else:
            self.ui.label_valido.setVisible(True)
            self.ui.label_invalido.setVisible(False)
