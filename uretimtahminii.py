from PyQt5.QtWidgets import *
from uretimtahmini_python import Ui_Form

class UretimTahminiPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.uretimtahminiformu = Ui_Form()
        self.uretimtahminiformu.setupUi(self)

class radioPage(QWidget):
    def __init__(self):
        super().__init__()
        self.radioform = Ui_Form()
        self.radioform.setupUi(self)

        #pushbutton olaylar
        self.radioform.pushButton.clicked.connect(self.radioButton)
    
    def radioButton(self):
        if self.radioform.radioButton.isChecked():
            print("Yıllık üretim tahmini seçildi.")
        if self.radioform.radioButton_2.isChecked():
            print("Aylık üretim tahmini seçildi.")
        if self.radioform.radioButton_3.isChecked():
            print("Günlük üretim tahmini seçildi.")
        

       

 
         
        