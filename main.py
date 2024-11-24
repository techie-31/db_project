from PyQt6 import QtCore, QtGui, QtWidgets
from loginPage import Ui_Dialog
from inboxPage import Ui_Dialog as box
from outBase import Ui_Dialog as base
import sys
import sqlite3
import os

path = os.getcwd()

def dtafetch():
    con = sqlite3.connect(f"{path}\\account.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM User")  # Fetch all data from the 'User' table
    rows = cur.fetchall()
    con.close()
    return rows

def inboxGui():
    database()
    inbox_dialog = QtWidgets.QDialog()  # Create a new dialog for the inbox
    inbox_ui = box()  # Use the inboxPage's Ui_Dialog
    inbox_ui.setupUi(inbox_dialog)
    inbox_dialog.exec()
    

def outbase():
    row = dtafetch()
    output = QtWidgets.QDialog()
    basegui = base()
    basegui.setupUi(output)
    basegui.tableWidget.setRowCount(len(row))
    for index,value in enumerate(row):
        # print(index,value)
        basegui.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(value[0])))
        basegui.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(str(value[1])))
    output.exec()    

    
def database():
    con = sqlite3.connect(f"{path}\\account.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS User(
        id varchar(50),
        password varchar(50)
        );""")
    
    user_txt= ui.lineEdit.text()
    pass_txt = ui.lineEdit_2.text()
    # print(user_txt,pass_txt)
    
    cur.execute(f"Insert into User(id, password) VALUES (?, ?)", (user_txt, pass_txt))
    con.commit()
    con.close()


    
    
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    
    ui.pushButton.clicked.connect(inboxGui)
    ui.pushButton_2.clicked.connect(outbase)
    # ui.pushButton_2.clicked.connect(dtafetch)
    
    Dialog.show()
    sys.exit(app.exec())