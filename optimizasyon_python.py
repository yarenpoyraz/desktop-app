# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimizasyon_python.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(971, 562)
        Form.setStyleSheet("")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(70, 250, 821, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(391, 90, 20, 20))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.checkBox_depolama = QtWidgets.QCheckBox(Form)
        self.checkBox_depolama.setGeometry(QtCore.QRect(300, 80, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.checkBox_depolama.setFont(font)
        self.checkBox_depolama.setObjectName("checkBox_depolama")
        self.pushButton_sonuc = QtWidgets.QPushButton(Form)
        self.pushButton_sonuc.setGeometry(QtCore.QRect(410, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sonuc.setFont(font)
        self.pushButton_sonuc.setStyleSheet("color: rgb(85, 0, 255);\n"
"background-color: rgb(255, 255, 0);\n"
"")
        self.pushButton_sonuc.setObjectName("pushButton_sonuc")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 120, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(550, 120, 113, 20))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(390, 80, 221, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Optimum Senaryo"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Senaryo 2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Senaryo 3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "Senaryo 4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "Senaryo 5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "Senaryo 6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "Senaryo 7"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "RES Kurulu Güç"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "GES Kurulu Güç"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Toplam Satış"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Batarya Kapasitesi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Batarya Kullanım Ömrü"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Toplam Maliyet"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Yatırım Kararı"))
        self.checkBox_depolama.setText(_translate("Form", "Depolama "))
        self.pushButton_sonuc.setText(_translate("Form", "Sonuç"))
        self.label.setText(_translate("Form", "Ortalama Birim Enerji Satış Fiyatı Giriniz ($)"))
        self.label_3.setText(_translate("Form", "(Hibrit santrale enerji depolama ekleme tercihi)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

