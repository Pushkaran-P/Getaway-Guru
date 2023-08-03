# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene
from admin2 import Ui_Dialog2

class Ui_Form0(object):
    def move_to_admin1(self):
        print('move_to_admin1')
        self.lineEdit.clear()
        self.lineEdit_2.clear()
    def move_to_admin2(self):
        p=open("admin.txt","w")
        p.write(str(self.y[0]))
        p.close()
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog2()
        self.ui.setupUi(self.window)
        self.window.show()
    def check_admin(self):
        print('check')
        import psycopg2
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur=conn.cursor()
        a=self.lineEdit.text()
        b=self.lineEdit_2.text()
        cur.execute("select admin(%s,%s);",(a,b))
        x=cur.fetchall()
        self.y=list(x[0])
        print(self.y)
        conn.close()
        if(None in self.y):
            print('if 1')
            self.move_to_admin1()
        else:
            print('else')
            self.move_to_admin2()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(749, 474)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 160, 171, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 161, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(270, 170, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 221, 201, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(70, 30, 20, 371))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(40, 350, 631, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 60, 101, 31))
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(220, 70, 441, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(-5, -9, 781, 511))
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.graphicsView.setMouseTracking(False)
        self.scene=QGraphicsScene()
        self.scene.addPixmap(QPixmap('31.jpeg'))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 300, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check_admin)
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.line.raise_()
        self.label_3.raise_()
        self.line_3.raise_()
        self.line_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">User Name </span><span style=\" font-size:16pt;\">:</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-style:italic;\">password </span><span style=\" font-size:16pt;\">:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Sign in</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form0()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

\