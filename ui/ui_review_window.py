# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Review(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        self.bckgr_label = QtWidgets.QLabel(Form)
        self.bckgr_label.setGeometry(QtCore.QRect(-190, -30, 971, 651))
        self.bckgr_label.setStyleSheet("background-image: url(:/newPrefix/ui_design.png);")
        self.bckgr_label.setText("")
        self.bckgr_label.setPixmap(QtGui.QPixmap("C:/Users/yanly/PycharmProjects/games_bd/images/ui_design.png"))
        self.bckgr_label.setScaledContents(True)
        self.bckgr_label.setObjectName("bckgr_label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(193, 187, 255);")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 561, 361))
        self.textEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.340591, y1:0.483, x2:0.755409, y2:0.932, stop:0 rgba(36, 36, 36, 255), stop:1 rgba(97, 97, 97, 255));\n"
"color: rgb(193, 187, 255);\n"
"font: 12pt \"Century Gothic\";")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 540, 171, 51))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.340591, y1:0.483, x2:0.755409, y2:0.932, stop:0 rgba(36, 36, 36, 255), stop:1 rgba(97, 97, 97, 255));\n"
"font: 87 16pt \"Onest\";\n"
"color: rgb(193, 187, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(270, 460, 311, 51))
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.340591, y1:0.483, x2:0.755409, y2:0.932, stop:0 rgba(36, 36, 36, 255), stop:1 rgba(97, 97, 97, 255));\n"
"color: rgb(193, 187, 255);\n"
"font: 87 20pt \"Onest\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 460, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(193, 187, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Напишите ваш отзыв:"))
        self.pushButton.setText(_translate("Form", "Отправить"))
        self.label_3.setText(_translate("Form", "Ваш никнейм:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Review()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
