from PyQt5.QtWidgets import *
from musteriekrani_python import Ui_MusteriEkrani
from PyQt5.QtCore import pyqtSignal

class MusteriPage(QWidget):
    musterisinyali = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.musteriformu = Ui_MusteriEkrani()
        self.musteriformu.setupUi(self)
        self.musteriformu.pushButton.clicked.connect(self.MusteriMesaj)
    
    def MusteriMesaj(self):
        bilgi = self.musteriformu.textEdit_musterimesaj.toPlainText()
        self.musterisinyali.emit(bilgi)     #butona basildiginda bir sinyal gidecek
