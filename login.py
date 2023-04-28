from PyQt5.QtWidgets import *
from login_python import Ui_Form
from anapencere import AnapencerePage

class LoginPage(QWidget):
    #def changeForm(self):
      #  if self.pushButton_4.isChecked():
      #      self.widget_3.hide()
       #     self.widget_2.show()

       # else:
       #     self.widget_3.show()
       #     self.widget_2.hide()

    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)   #login_python dosyasını buna bagladik ve degisimler yapabilriz
        self.anapencereac = AnapencerePage()  #anapencereden bir obje olusturduk
        self.loginform.pushButton.clicked.connect(self.GirisYap)  #Giris butonunu aktiflestirecek
        #self.pushButton_4.clicked.connect(self.changeForm)
        

        

    def GirisYap(self):
        kadi = self.loginform.lineEdit_kullaniciadi.text()
        sifre = self.loginform.lineEdit_sifre.text()
        if kadi == "yaren" and sifre=="123":
            self.hide()
            self.anapencereac.show()  #kadi ve sifre dogruysa acacak
