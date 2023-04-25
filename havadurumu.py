from PyQt5.QtWidgets import *
from havadurumu_python import Ui_Form

class HavaDurumuPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.havadurumuform = Ui_Form()
        self.havadurumuform.setupUi(self) 