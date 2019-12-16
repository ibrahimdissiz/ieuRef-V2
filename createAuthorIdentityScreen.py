# -*- coding: utf-8 -*-

# Ali Gilim
# Author Identity Screen
# 16.12.2019

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import csv

# Builds a Dialog for Create Author Identity Screen with a table, add and remove buttons, save and cancel buttons
class Ui_Dialog(object):

    # Creates UI for Create Author Identity Screen
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(295, 413)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 20, 211, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.addItem = QtWidgets.QPushButton(Dialog)
        self.addItem.setGeometry(QtCore.QRect(90, 260, 51, 41))
        self.addItem.setObjectName("Add Item")
        self.removeItem = QtWidgets.QPushButton(Dialog)
        self.removeItem.setGeometry(QtCore.QRect(150, 260, 51, 41))
        self.removeItem.setObjectName("Remove Item")
        self.saveIdentity = QtWidgets.QPushButton(Dialog)
        self.saveIdentity.setGeometry(QtCore.QRect(60, 330, 81, 51))
        self.saveIdentity.setObjectName("Save Identity")
        self.cancelIdentity = QtWidgets.QPushButton(Dialog)
        self.cancelIdentity.setGeometry(QtCore.QRect(160, 330, 81, 51))
        self.cancelIdentity.setObjectName("Cancel Identity")

        # Displays names and characters for components on the screen
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Loads author identity data from cvs file
        self.loadAuthorIdentityData()

        # Defines function calls for buttons on the screen
        self.addItem.clicked.connect(self.addNewRow)
        self.removeItem.clicked.connect(self.removeSelectedRow)
        self.saveIdentity.clicked.connect(self.saveAuthorIdentityScreen)
        self.cancelIdentity.clicked.connect(self.closeAuthorIdentityScreen)

    # Displays names of UI components on the screen
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create Author Identity"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Author"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Variation"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.addItem.setText(_translate("Dialog", "+"))
        self.removeItem.setText(_translate("Dialog", "-"))
        self.saveIdentity.setText(_translate("Dialog", "SAVE"))
        self.cancelIdentity.setText(_translate("Dialog", "CANCEL"))

    # Removes selected rows from the table widget
    def removeSelectedRow(self):
        indices = self.tableWidget.selectionModel().selectedRows()
        for index in sorted(indices):
            self.tableWidget.removeRow(index.row())

    # Adds a new row at the end of the table widget
    def addNewRow(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    # Saves the current status of the table widget into a csv file
    def saveAuthorIdentityScreen(self):
        with open('authorIdentityData.csv', 'w') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            for row in range(self.tableWidget.rowCount()):
                rowdata = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item is not None:
                        #                        rowdata.append(unicode(item.text()).encode('utf8'))
                        rowdata.append(item.text())  # +
                    else:
                        rowdata.append('')

                writer.writerow(rowdata)
        self.showOKMessage(Dialog)

    # Displays SAVED message after Save button is clicked
    def showOKMessage(self, Dialog):
        QMessageBox.about(Dialog, "Status", "SAVED")

    # Imports author identity data from the csv file into the table widget
    def loadAuthorIdentityData(self):
        with open('authorIdentityData.csv', 'r') as csv_file:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(2)
            my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row_data in my_file:
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                if len(row_data) > 10:
                    self.tableWidget.setColumnCount(len(row_data))
                for column, stuff in enumerate(row_data):
                    item = QTableWidgetItem(stuff)
                    self.tableWidget.setItem(row, column, item)

    # Closes author identity screen
    def closeAuthorIdentityScreen(self):
        Dialog.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
