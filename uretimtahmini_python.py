# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uretimtahmini_python.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(815, 531)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(100, 130, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 130, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(280, 130, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 200, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 260, 47, 13))
        self.label_2.setObjectName("label_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(450, 130, 321, 191))
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(170, 260, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(170, 200, 194, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 350, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(85, 0, 255);\n"
"background-color: rgb(255, 255, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "Yıllık"))
        self.radioButton_2.setText(_translate("Form", "Aylık"))
        self.radioButton_3.setText(_translate("Form", "Günlük"))
        self.label.setText(_translate("Form", "Tarih Başlangıç"))
        self.label_2.setText(_translate("Form", "Tarih Bitiş"))
        self.pushButton.setText(_translate("Form", "Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

