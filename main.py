from PyQt5.QtWidgets import QApplication
from login import LoginPage
from optimizasyon import DepoPage


app = QApplication([])
pencere = LoginPage()
pencere.show()
app.exec_()