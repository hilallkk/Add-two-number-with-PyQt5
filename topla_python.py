import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from topla import Ui_MainWindow

class Toplama(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.QtTopla=Ui_MainWindow()
        self.QtTopla.setupUi(self)
        self.QtTopla.pushButton_topla.clicked.connect(self.Toplama_islemi)

    def Toplama_islemi(self):
        sayi1=self.QtTopla.lineEdit_1.text()
        sayi2=self.QtTopla.lineEdit_2.text()
        toplam=int(sayi1) + int(sayi2)
        print("Toplam:",toplam)


app=QApplication([])
pencere=Toplama()
pencere.show()
app.exec_()