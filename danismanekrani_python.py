# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'danismanekrani_python.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DanismanEkrani(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(593, 574)
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"")
        self.label.setObjectName("label")
        self.label_danismanbilgisi = QtWidgets.QLabel(Form)
        self.label_danismanbilgisi.setGeometry(QtCore.QRect(130, 130, 371, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_danismanbilgisi.setFont(font)
        self.label_danismanbilgisi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_danismanbilgisi.setObjectName("label_danismanbilgisi")
        self.textEdit_danismanmesaj = QtWidgets.QTextEdit(Form)
        self.textEdit_danismanmesaj.setGeometry(QtCore.QRect(120, 240, 381, 171))
        self.textEdit_danismanmesaj.setObjectName("textEdit_danismanmesaj")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 200, 191, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_gonder = QtWidgets.QPushButton(Form)
        self.pushButton_gonder.setGeometry(QtCore.QRect(210, 440, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_gonder.setFont(font)
        self.pushButton_gonder.setObjectName("pushButton_gonder")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "MÜŞTERİDEN MESAJ"))
        self.label_danismanbilgisi.setText(_translate("Form", "Şu anda müşteriden gelen bir mesaj bulunmamaktadır."))
        self.label_3.setText(_translate("Form", "DANIŞMAN MESAJ EKRANI"))
        self.pushButton_gonder.setText(_translate("Form", "Müşteriye Mesaj Gönder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_DanismanEkrani()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

