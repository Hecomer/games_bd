# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_already_exists.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CurrentUser(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(316, 80)
        Dialog.setMinimumSize(QtCore.QSize(316, 80))
        Dialog.setMaximumSize(QtCore.QSize(316, 80))
        self.bckgr_label = QtWidgets.QLabel(Dialog)
        self.bckgr_label.setGeometry(QtCore.QRect(-50, -50, 371, 281))
        self.bckgr_label.setStyleSheet("background-image: url(:/newPrefix/ui_design.png);")
        self.bckgr_label.setText("")
        self.bckgr_label.setPixmap(QtGui.QPixmap("C:/Users/yanly/PycharmProjects/games_bd/images/ui_design.png"))
        self.bckgr_label.setScaledContents(True)
        self.bckgr_label.setObjectName("bckgr_label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 289, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(193, 187, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.340591, y1:0.483, x2:0.755409, y2:0.932, stop:0 rgba(36, 36, 36, 255), stop:1 rgba(97, 97, 97, 255));\n"
"color: rgb(193, 187, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "ЭТО ИМЯ ЗАНЯТО"))
        self.pushButton.setText(_translate("Dialog", "ОК"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
