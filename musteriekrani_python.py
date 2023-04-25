# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musteriekrani_python.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MusteriEkrani(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 570)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 60, 361, 41))
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
        self.label_musteribilgisi = QtWidgets.QLabel(Form)
        self.label_musteribilgisi.setGeometry(QtCore.QRect(100, 140, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_musteribilgisi.setFont(font)
        self.label_musteribilgisi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_musteribilgisi.setObjectName("label_musteribilgisi")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 210, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_musterimesaj = QtWidgets.QTextEdit(Form)
        self.textEdit_musterimesaj.setGeometry(QtCore.QRect(100, 250, 381, 171))
        self.textEdit_musterimesaj.setObjectName("textEdit_musterimesaj")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 450, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "DANIŞMANDAN  MESAJ"))
        self.label_musteribilgisi.setText(_translate("Form", "Şu anda danışmanınızdan gelen bir mesaj bulunmamaktadır."))
        self.label_3.setText(_translate("Form", "BİZE ULAŞIN"))
        self.pushButton.setText(_translate("Form", "Mesaj gönder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MusteriEkrani()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

