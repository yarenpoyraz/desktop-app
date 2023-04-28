from PyQt5.QtWidgets import *
from anapenceree_python import Ui_MainWindow
from havadurumu import HavaDurumuPage    #havadurumu penceresini acmak icin
from uretimtahminii import UretimTahminiPage
from optimizasyon import OptimizasyonPage
from danismanekrani_python import Ui_DanismanEkrani
from musterimesaj import MusteriPage
from danismanmesaj import DanismanPage
from PyQt5.QtCore import pyqtSignal


class AnapencerePage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anapencereform = Ui_MainWindow()
        self.anapencereform.setupUi(self)   #login_python dosyasını buna bagladik ve degisimler yapabilriz

        self.havadurumuform = HavaDurumuPage()  #havadurumupageten havadurumuforma bir obje üretecek

        self.uretimtahminiformu = UretimTahminiPage() 

        self.optimizasyonform = OptimizasyonPage()

        self.musteriformu = MusteriPage()
        
        self.danismanformu = DanismanPage()




       # self.danisman = Ui_DanismanEkrani()
       # self.danisman.setupUi(self)
       # self.musteri = MusteriPage()
       # self.musteri.musterisinyali.connect(self.MusteriBilgi)
        #self.danisman.pushButton_gonder.clicked.connect(self.danismanBilgi)

     
        


        self.anapencereform.havadurumu.triggered.connect(self.HavaDurumuFormu)  #buradaki havadurumu objesi visualdaki isminden geliyor
        self.anapencereform.uretimtahmini.triggered.connect(self.UretimTahmini) #buradaki uretimtahmini objesi visualdaki isminden geliyor
        self.anapencereform.optimizasyon.triggered.connect(self.OptimizasyonFormu)
        self.anapencereform.bizeulasin.triggered.connect(self.Musteri)
        self.anapencereform.bizeulasin.triggered.connect(self.Danisman)



    
   # def MusteriBilgi(self,bilgi):
    #    self.danisman.label_danismanbilgisi.setText(bilgi)
   # def danismanBilgi(self):
    #    danismanbilgi = self.danisman.textEdit_danismanmesaj.toPlainText()
    #    self.musteri.musteriformu.label_musteribilgisi.setText(danismanbilgi)



    def HavaDurumuFormu(self):
        self.havadurumuform.show()      #havadurumunu iceri cekiyoruz yani seceneklerde tiklandiginda havadurumu sayfasi gelecek

    def UretimTahmini(self):
        self.uretimtahminiformu.show()

    def OptimizasyonFormu(self):
        self.optimizasyonform.show()
    
    def Musteri(self):
        self.musteriformu.show()

    def Danisman(self):
        self.danismanformu.show()


        
