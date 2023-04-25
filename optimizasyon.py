from PyQt5.QtWidgets import *
from optimizasyon_python import Ui_Form

class OptimizasyonPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.optimizasyonform = Ui_Form()
        self.optimizasyonform.setupUi(self)

class DepoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.depo = Ui_Form()
        self.depo.setupUi(self)
        self.depo.pushButton_sonuc.clicked.connect(self.Sonuc)

    def Sonuc(self):
        if self.depo.checkBox_depolama.isChecked():
            print("Depolama olmasına karar verildi.")
