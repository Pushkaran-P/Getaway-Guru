# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
class Ui_Dialog5(object):
    def insert_view(self):
        a=str(self.name)
        b=int(self.phone_no)
        c=int(self.stay_cost)
        d=str(self.path1)
        f=str(self.path2)
        g=str(self.path3)
        h=str(self.hotel_name1)
        i=str(self.hotel_name2)
        j=str(self.hotel_name3)
        k=str(self.bus_type)
        l=int(self.no_bus)
        m=int(self.t_cost)
        n=int(self.f_cost)
        o=int(self.no_student)
        p=int(self.company_id)
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("insert into view values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(a,b,c,d,f,g,h,i,j,k,l,m,n,o,p))
        conn.commit()
        conn.close()
    def print_element(self):
        f=open("user1.txt","r")
        x=f.read()
        y=x.split(" ")
        self.name=y[0]
        self.phone_no=y[2]
        self.no_student=int(y[4])
        self.textEdit.setText(self.name)
        self.textEdit_2.setText(self.phone_no)
        f.close()
        
        f=open("user2.txt","r")
        x=f.read()
        y=x.split(" ")
        path1_id=int(y[0])
        self.no_bus=y[1]
        self.bus_type=y[2]
        self.textEdit_7.setText(self.no_bus)
        self.textEdit_6.setText(self.bus_type)
        
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("select startpoint,via,endpoint from path where path_id=(%s);",[path1_id])
        x=cur.fetchall()
        y="-".join([i for i in x[0]])
        self.path1=y
        self.textEdit_3.setText(y)
        conn.commit()
        conn.close()
        f.close()
        
        f=open("user3.txt","r")
        x=f.read()
        hotel1_id=int(x)
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("select similar_hotel from hotel where hotel_id=(%s);",[hotel1_id])
        x=cur.fetchall()
        self.hotel_name1=x[0][0]
        self.textEdit_10.setText(x[0][0])
        conn.close()
        f.close()
        
        f=open("user4.txt","r")
        x=f.read()
        y=x.split(" ")
        f.close()   
        path2_id=int(y[0])
        self.company_id=int(y[4])
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("select startpoint,via,endpoint from path where path_id=(%s);",[path2_id])
        x=cur.fetchall()
        z="-".join([i for i in x[0]])
        self.path2=z
        self.textEdit_4.setText(z)
        path3_id=int(y[1])
        cur.execute("select startpoint,via,endpoint from path where path_id=(%s);",[path3_id])
        x=cur.fetchall()
        print(x)
        z="-".join([i for i in x[0]])
        self.path3=z
        self.textEdit_5.setText(z)
        
        hotel2_id=int(y[2])
        hotel3_id=int(y[3])
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("select similar_hotel from hotel where hotel_id=(%s);",[hotel2_id])
        x=cur.fetchall()
        self.hotel_name2=x[0][0]
        self.textEdit_11.setText(x[0][0])
        cur.execute("select similar_hotel from hotel where hotel_id=(%s);",[hotel3_id])
        x=cur.fetchall()
        self.hotel_name3=x[0][0]
        self.textEdit_12.setText(x[0][0])
        conn.close()
        
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("select travelcost from path where path_id=(%s) or path_id=(%s) or path_id=(%s);",(path1_id,path2_id,path3_id))
        x=cur.fetchall()
        ans=x[0][0]+x[1][0]+x[2][0]
        self.t_cost=ans
        self.textEdit_8.setText(str(ans))
        cur.execute("select foodcost_id from path where path_id=(%s) or path_id=(%s) or path_id=(%s);",(path1_id,path2_id,path3_id))
        x=cur.fetchall()
        ans=x[0][0]+x[1][0]+x[2][0]
        self.f_cost=ans
        self.textEdit_9.setText(str(ans))
        self.checkBox.clicked.connect(self.insert_view)
        
        conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fuckoff13", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        no=int(self.no_student)
        cur.execute("select cost*((%s)/no_per_room) from hotel where hotel_id=(%s) or hotel_id=(%s) or hotel_id=(%s);",(no,path1_id,path2_id,path3_id))
        self.stay_cost=x[0][0]+x[1][0]+x[2][0]
        
        conn.close()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(798, 543)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(200, 460, 211, 51))
        self.checkBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 460, 191, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.print_element)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 100, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 100, 55, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(14, 160, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 61, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 71, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 310, 81, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 380, 101, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(450, 100, 121, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(380, 130, 161, 61))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(390, 190, 151, 41))
        self.label_9.setObjectName("label_9")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 150, 171, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 210, 171, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(100, 260, 171, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(100, 320, 171, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(100, 380, 171, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(540, 110, 171, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_8.setGeometry(QtCore.QRect(540, 150, 171, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_9.setGeometry(QtCore.QRect(540, 200, 171, 31))
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(420, 260, 121, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(430, 310, 131, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(430, 360, 111, 31))
        self.label_12.setObjectName("label_12")
        self.textEdit_10 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_10.setGeometry(QtCore.QRect(540, 260, 171, 31))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_11.setGeometry(QtCore.QRect(540, 310, 171, 31))
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_12.setGeometry(QtCore.QRect(540, 360, 171, 31))
        self.textEdit_12.setObjectName("textEdit_12")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "click to confirm"))
        self.pushButton.setText(_translate("Dialog", "Place your booking"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Name :</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Phone no :</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">path1 :</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">path2 :</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">path3 :</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">bus Type :</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">No of bus : </span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Total cost of travel :</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Total cost of food :</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Hotel1 Name :</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Hotel2 name:</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Hotel3 name :</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

