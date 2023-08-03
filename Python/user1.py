# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene
from user2 import Ui_Dialog2
import psycopg2
global name,college,phone_no,year,no_student,department

name=" "
college=" "
department=" "   
phone_no=0
year=0
no_student=0
class Ui_Form1(object):
    def move_to_user2(self):
        name=str(self.lineEdit.text())
        college=str(self.lineEdit_2.text())
        department=str(self.lineEdit_3.text())
        phone_no=int(self.lineEdit_4.text())
        year=int(self.lineEdit_5.text())
        no_student=int(self.spinBox.text())
        
        f=open("user1.txt","w")
        f.write(" ".join([str(i) for i in [name,college,phone_no,year,no_student,department]]))
        f.close()
        
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("insert into user_t values(%s,%s,%s,%s,%s,%s,%s);",(1,name,college,department,phone_no,year,no_student))
        conn.commit()
        conn.close()
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog2()
        self.ui.setupUi(self.window)
        self.window.show() 
    def check(self):
        #self.move_to_user2()
        if(len(self.lineEdit.text())!=0 and len(self.lineEdit_2.text())!=0 and len(self.lineEdit_3.text())!=0 and len(self.lineEdit_4.text())==10 and  len(self.lineEdit_5.text())<=5):
            self.move_to_user2()
        else:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(893, 484)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 100, 91, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 140, 101, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 151, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(120, 210, 141, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(170, 250, 101, 41))
        self.label_5.setObjectName("label_5")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(-5, 0, 901, 491))
        self.scene=QGraphicsScene()
        self.scene.addPixmap(QPixmap('2.jpg'))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 110, 231, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 150, 231, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 190, 231, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 230, 231, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 260, 231, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 290, 171, 41))
        self.label_6.setObjectName("label_6")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(240, 300, 91, 31))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 390, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check)
        
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.pushButton.raise_()
        self.label_6.raise_()
        self.spinBox.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Name :</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">College : </span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Department : </span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Phone no : </span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Year : </span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Next"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">No of Students : </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

#print (name)