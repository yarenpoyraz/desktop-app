from PyQt5.QtWidgets import *
from danismanekrani_python import Ui_DanismanEkrani
from PyQt5.QtCore import pyqtSignal

class DanismanPage(QWidget):
    danismansinyali = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.danismanformu = Ui_DanismanEkrani()
        self.danismanformu.setupUi(self)
        