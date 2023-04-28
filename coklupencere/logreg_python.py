
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, resimler
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 639)
        Form.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y2:0.477,stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y2:0.477,stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(150,123,111,255)\n"
"}\n"
"\n"
"QPushButton#pushButton_3{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y2:0.477,stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y2:0.477,stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(150,123,111,255)\n"
"}\n"
"\n"
"QPushButton#pushButton_4{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y2:0.477,stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover{\n"
"    background-color: qlineargradient(spread:pad,x1:0,y2:0.477,stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(150,123,111,255)\n"
"}\n"
"\n"
"")
        

        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(70, 90, 500, 481))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 20, 250, 430))
        self.label.setStyleSheet("border-image: url(:/resim/hibrit-enerji-mevzuat-1200x1200.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 250, 430))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 251, 431))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 241, 130))
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(30, 70, 231, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 220, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255,255,255,200);")
        self.label_8.setObjectName("label_8")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(260, 40, 211, 361))
        self.widget_2.setObjectName("widget_2")
        self.register_2 = QtWidgets.QLabel(self.widget_2)
        self.register_2.setGeometry(QtCore.QRect(60, 40, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("color:rgba(0,0,0,200);")
        self.register_2.setObjectName("register_2")
        self.lineEdit_firstname = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_firstname.setGeometry(QtCore.QRect(20, 90, 81, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_firstname.setFont(font)
        self.lineEdit_firstname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_firstname.setText("")
        self.lineEdit_firstname.setObjectName("lineEdit_firstname")
        self.lineEdit_lastname = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_lastname.setGeometry(QtCore.QRect(130, 90, 81, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_lastname.setFont(font)
        self.lineEdit_lastname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_lastname.setText("")
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.lineEdit_email = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_email.setGeometry(QtCore.QRect(20, 140, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_sifre_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_sifre_3.setGeometry(QtCore.QRect(20, 190, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sifre_3.setFont(font)
        self.lineEdit_sifre_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_sifre_3.setText("")
        self.lineEdit_sifre_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_sifre_3.setObjectName("lineEdit_sifre_3")
        self.lineEdit_sifre_confirm = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_sifre_confirm.setGeometry(QtCore.QRect(20, 240, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sifre_confirm.setFont(font)
        self.lineEdit_sifre_confirm.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_sifre_confirm.setText("")
        self.lineEdit_sifre_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_sifre_confirm.setObjectName("lineEdit_sifre_confirm")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 300, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 60, 30, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(250, 50, 231, 291))
        self.widget_3.setObjectName("widget_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_kullaniciadi = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_kullaniciadi.setGeometry(QtCore.QRect(20, 100, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_kullaniciadi.setFont(font)
        self.lineEdit_kullaniciadi.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_kullaniciadi.setObjectName("lineEdit_kullaniciadi")
        self.lineEdit_sifre = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_sifre.setGeometry(QtCore.QRect(20, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sifre.setFont(font)
        self.lineEdit_sifre.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_sifre.setObjectName("lineEdit_sifre")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 181, 20))
        self.label_5.setStyleSheet("color:rgba(0,0,0,210);")
        self.label_5.setObjectName("label_5")

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.widget_3.hide()
        self.widget_2.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "HREP DESIGN"))
        self.label_8.setText(_translate("Form", "Welcome!\n"
"\n"
" You have made the right decision for\n"
" your hybrid renewable power plant!"))
        self.register_2.setText(_translate("Form", "Register"))
        self.lineEdit_firstname.setPlaceholderText(_translate("Form", "First Name"))
        self.lineEdit_lastname.setPlaceholderText(_translate("Form", "Last Name"))
        self.lineEdit_email.setPlaceholderText(_translate("Form", "Email Address"))
        self.lineEdit_sifre_3.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_sifre_confirm.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.pushButton_3.setText(_translate("Form", "Register"))
        self.pushButton_4.setText(_translate("Form", ">"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit_kullaniciadi.setPlaceholderText(_translate("Form", "User Name"))
        self.lineEdit_sifre.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_5.setText(_translate("Form", "Forgot your User Name or password?"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

