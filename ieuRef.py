import sys
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

import bibtexparser
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap


from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import csv
from bibtexparser.bparser import BibTexParser



data = []
searchedList = []

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/logo.png'))
        file_menu = self.menuBar().addMenu("&File")
        global data
        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("IeuRef")
        self.setMinimumSize(1000, 800)
        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("Author", "Year", "Type", "Title"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        help_action = QAction(QIcon("icon/help.png"), "Help", self)
        help_action.triggered.connect(self.help)
        help_menu.addAction(help_action)

        selectBibtex_action = QAction(QIcon("icon/addBibtex.png"), "Select BibTeX file", self)
        selectBibtex_action.triggered.connect(self.selectBibtex)
        file_menu.addAction(selectBibtex_action)

        createBibtex_action = QAction(QIcon("icon/create.png"), "Create Bibtex", self)
        createBibtex_action.triggered.connect(self.createBibtex)
        file_menu.addAction(createBibtex_action)

        saveBibtex_action = QAction(QIcon("icon/save.png"), "Save BibTeX file", self)
        saveBibtex_action.triggered.connect(self.saveBibtex)
        file_menu.addAction(saveBibtex_action)

        searchBibtex_action = QAction(QIcon("icon/search.png"), "Search", self)
        searchBibtex_action.triggered.connect(self.search)
        file_menu.addAction(searchBibtex_action)

        filterBibtex_action = QAction(QIcon("icon/filterBibtex.png"), "Filter BibTeX ", self)
        filterBibtex_action.triggered.connect(self.filterBibtex)
        file_menu.addAction(filterBibtex_action)

        # Create Author Identity file menu button
        createAuthorIdentityBibtex_action = QAction(QIcon("icon/identity.png"), "Create Author Identity", self)
        createAuthorIdentityBibtex_action.triggered.connect(self.createAuthorIdentity)
        file_menu.addAction(createAuthorIdentityBibtex_action)

        deleteAllBibtex_action = QAction(QIcon("icon/delete.png"), "Delete All", self)
        deleteAllBibtex_action.triggered.connect(self.deleteAllBibtex)
        file_menu.addAction(deleteAllBibtex_action)

        btn_selectBibtex_action = QAction(QIcon("icon/addBibtex.png"), "Select BibTeX file", self)
        btn_selectBibtex_action.triggered.connect(self.selectBibtex)
        btn_selectBibtex_action.setStatusTip('Select BibTeX File')
        toolbar.addAction(btn_selectBibtex_action)

        btn_createBibtex_action = QAction(QIcon("icon/create.png"), "Create Bibtex", self)
        btn_createBibtex_action.triggered.connect(self.createBibtex)
        btn_createBibtex_action.setStatusTip('Create BibTeX Entry')
        toolbar.addAction(btn_createBibtex_action)

        btn_searchBibtex_action = QAction(QIcon("icon/search.png"), "Search Student", self)
        btn_searchBibtex_action.triggered.connect(self.search)
        btn_searchBibtex_action.setStatusTip('Search')
        toolbar.addAction(btn_searchBibtex_action)

        btn_filterBibtex_action = QAction(QIcon("icon/filterBibtex.png"), "Filter BibTeX ", self)
        btn_filterBibtex_action.triggered.connect(self.filterBibtex)
        btn_filterBibtex_action.setStatusTip('Filter BibTeX')
        toolbar.addAction(btn_filterBibtex_action)

        # Create Author Identity button on the main screen with its icon
        btn_createAuthorIdentityBibtex_action = QAction(QIcon("icon/identity.png"), "Create Author Identity", self)
        btn_createAuthorIdentityBibtex_action.triggered.connect(self.createAuthorIdentity)
        btn_createAuthorIdentityBibtex_action.setStatusTip('Create Author Identity')
        toolbar.addAction(btn_createAuthorIdentityBibtex_action)

        btn_saveBibtex_action = QAction(QIcon("icon/save.png"), "Save Bibtex", self)
        btn_saveBibtex_action.triggered.connect(self.saveBibtex)
        btn_saveBibtex_action.setStatusTip('Save')
        toolbar.addAction(btn_saveBibtex_action)

        btn_deleteSelected_action = QAction(QIcon("icon/delete.png"), "Delete All", self)
        btn_deleteSelected_action.triggered.connect(self.deleteAllBibtex)
        btn_deleteSelected_action.setStatusTip('Delete All')
        toolbar.addAction(btn_deleteSelected_action)


    def help(self):
        dlg = HelpDialog()
        dlg.exec_()

    def loaddata(self, keyys):
        print("Selam")
        global data
        data = data + keyys  # append(entry)
        print(data)
        # newData = [(author, year, type1, title)]
        # entry = MainWindow.data
        # entry.append((author, year, type1, title))
        # print("------------------")
        # print(entry)
        self.printData()

    def printData(self):
        # numrows = len(data)  # 6 rows in your example
        # numcols = len(data[0])
        # Printing data to the QTableWidget
        global data
        row = self.tableWidget.rowCount()

        for i in range(row, len(data)):
            item = data[i]
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item["author"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item["year"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(item["ENTRYTYPE"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(item["title"]))
            row = row + 1
            print("row", row)
        # for row in range(numrows):
        #     print(numrows)
        #     self.tableWidget.insertRow(row)
        #     for column in range(numcols):
        #         print(column)
        #         self.tableWidget.setItem(row, column, QTableWidgetItem((data[row][column])))

    def printSearchedList(self):
        # numrows = len(data)  # 6 rows in your example
        # numcols = len(data[0])
        # Printing data to the QTableWidget
        global searchedList
        row = self.tableWidget.rowCount()

        for item in searchedList:
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item["author"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item["year"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(item["ENTRYTYPE"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(item["title"]))
            row = row + 1
            print("row", row)

    def createBibtex(self):
        searchedList.clear()
        dlg = CreateDialog()
        dlg.exec_()
        global data
        self.tableWidget.setRowCount(0)
        self.printData()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()
        global searchedList
        self.tableWidget.setRowCount(0)
        self.printSearchedList()
        searchedList.clear()


    def filterBibtex(self):
        dlg = FilterDialog()
        dlg.exec_()

    def deleteAllBibtex(self):
        buttonReply = QMessageBox.question(self, 'Confirm', "Do you want to delete all?",
                                           QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            data.clear()
            self.tableWidget.setRowCount(0)
        else:
            return

    def saveBibtex(self):
            global data
            print(data)
            db = BibDatabase()
            db.entries = []
            db.entries = data

            writer = BibTexWriter()

            options = QFileDialog.Options()
            bibtexFile, _ = QFileDialog.getSaveFileName(self, "Save Bibtex File", "",
                                                        "BibTeX Files (*.bib)", options=options)
            if (bibtexFile):
                with open(bibtexFile, 'w') as bibfile:
                    bibfile.write(writer.write(db))
            else:
                return

    def deleteSelected(self):
        print("delete selected")
        r = self.tableWidget.selectionModel().selectedItems
        print(r)

    def createAuthorIdentity(self):
        dlg = CreateAuthorIdentityDialog()
        dlg.exec_()

    def selectBibtex(self):
        searchedList.clear()
        self.tableWidget.setRowCount(0)
        options = QFileDialog.Options()
        bibtexFile, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                    "BibTeX Files (*.bib)", options=options)
        if (bibtexFile):
            with open(bibtexFile) as bibtex:

                try:
                    parser = BibTexParser(common_strings=False)
                    parser.ignore_nonstandard_types = False
                    parser.homogenise_fields = False
                    bibtex_database = bibtexparser.load(bibtex)
                    keyys = bibtex_database.entries
                    countEntry = len(keyys)
                    self.loaddata(keyys)

                except Exception:
                    print(format(Exception))
                    QMessageBox.warning(QMessageBox(), 'Error', 'Could not load Bibtex file.')
        else:
            return


class HelpDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(HelpDialog, self).__init__(*args, **kwargs)
        self.im = QPixmap("./icon/help1.png")
        self.label = QLabel()
        self.label.setPixmap(self.im)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.setLayout(self.grid)

        self.setGeometry(50, 50, 320, 200)
        self.setWindowTitle("Help File")
        self.show()


class CreateDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CreateDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Add New ")
        self.setFixedWidth(600)
        self.setFixedHeight(300)

        self.setWindowTitle("Create New BibTeX file")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.boxlabel = QLabel("Entry Type:")

        layout = QFormLayout()
        self.typeinput = QComboBox()
        self.typeinput.addItem("-Please select a BibTeX file type")
        self.typeinput.addItem("Article")
        self.typeinput.addItem("Book")
        self.typeinput.addItem("Journal")
        self.typeinput.addItem("Proceeding")
        self.typeinput.addItem("InProceeding")
        self.typeinput.addItem("MasterThesis")
        self.typeinput.addItem("PhdThesis")
        self.typeinput.addItem("Unpublished")
        self.typeinput.addItem("Misc")
        self.typeinput.activated[str].connect(self.selected)
        self.typeinput.activated.connect(self.close)

        layout.addWidget(self.boxlabel)
        layout.addWidget(self.typeinput)
        self.setLayout(layout)

    def selected(self, data):
        if data == "Article":
            dlc = Article()
            dlc.exec_()

        elif data == "Book":
            dlc = Book()
            dlc.exec_()
        elif data == "Journal":
            dlc = Journal()
            dlc.exec_()
        elif data == "Proceeding":
            dlc = Proceeding()
            dlc.exec_()
        elif data == "InProceeding":
            dlc = InProceeding()
            dlc.exec_()
        elif data == "MasterThesis":
            dlc = MasterThesis()
            dlc.exec_()
        elif data == "PhdThesis":
            dlc = PhdThesis()
            dlc.exec_()
        elif data == "Unpublished":
            dlc = Unpublished()
            dlc.exec_()
        elif data == "Misc":
            dlc = Misc()
            dlc.exec_()


class Article(QDialog):
    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)

        self.setWindowTitle("Article")
        self.setFixedWidth(450)
        self.setFixedHeight(500)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()
        self.line7 = QLineEdit()
        self.line8 = QLineEdit()
        self.line9 = QLineEdit()
        self.line10 = QLineEdit()

        self.text1 = QLabel("Author(*):")
        self.text2 = QLabel("ID(*):")
        self.text3 = QLabel("Title(*):")
        self.text4 = QLabel("Year:")
        self.text5 = QLabel("Journal:")
        self.text6 = QLabel("Number:")
        self.text7 = QLabel("Pages:")
        self.text8 = QLabel("Month:")
        self.text9 = QLabel("Note:")
        self.text10 = QLabel("Volume:")
        self.keyText=QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)
        layout.addWidget(self.text6)
        layout.addWidget(self.line6)
        layout.addWidget(self.text7)
        layout.addWidget(self.line7)
        layout.addWidget(self.text8)
        layout.addWidget(self.line8)
        layout.addWidget(self.text9)
        layout.addWidget(self.line9)
        layout.addWidget(self.text10)
        layout.addWidget(self.line10)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        ID = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()
        journal = self.line5.text()
        number = self.line6.text()
        pages = self.line7.text()
        month = self.line8.text()
        note = self.line9.text()
        volume = self.line10.text()

        if author == "" or title == "" or ID == "" or year == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            year = int(self.line4.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year must be a integer')
            return

        createBib = [{
            'ID': ID,
            'author': author,
            'title': title,
            'journal': journal,
            'year': str(year),
            'ENTRYTYPE': 'article',
            'number': number,
            'pages': pages,
            'month': month,
            'note': note,
            'volume': volume
        }]
        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]
        print(list2)
        global data
        data = data + list2

class Book(QDialog):
    def __init__(self, *args, **kwargs):
        super(Book, self).__init__(*args, **kwargs)
        self.setWindowTitle("Book")
        self.setFixedWidth(400)
        self.setFixedHeight(650)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()
        self.line7 = QLineEdit()
        self.line8 = QLineEdit()
        self.line9 = QLineEdit()
        self.line10 = QLineEdit()
        self.line11 = QLineEdit()
        self.line12 = QLineEdit()

        self.text1 = QLabel("ID(*):")
        self.text2 = QLabel("Author(*):")
        self.text3 = QLabel("Title(*):")
        self.text4 = QLabel("Publisher:")
        self.text5 = QLabel("Year(*):")
        self.text6 = QLabel("Volume:")
        self.text7 = QLabel("Series:")
        self.text8 = QLabel("Address:")
        self.text9 = QLabel("Edition:")
        self.text10 = QLabel("Month:")
        self.text11 = QLabel("Note:")
        self.text12 = QLabel("ISBN:")
        self.keyText = QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)
        layout.addWidget(self.text6)
        layout.addWidget(self.line6)
        layout.addWidget(self.text7)
        layout.addWidget(self.line7)
        layout.addWidget(self.text8)
        layout.addWidget(self.line8)
        layout.addWidget(self.text9)
        layout.addWidget(self.line9)
        layout.addWidget(self.text10)
        layout.addWidget(self.line10)
        layout.addWidget(self.text11)
        layout.addWidget(self.line11)
        layout.addWidget(self.text12)
        layout.addWidget(self.line12)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        ID = self.line1.text()
        author = self.line2.text()
        title = self.line3.text()
        publisher = self.line4.text()
        year = self.line5.text()
        volume = self.line6.text()
        series = self.line7.text()
        address = self.line8.text()
        edition = self.line9.text()
        month = self.line10.text()
        note = self.line11.text()
        isbn = self.line12.text()

        if author == "" or title == "" or ID == "" or year == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            year = int(self.line5.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year/Edition/Series/Volume must be a integer')
            return

        createBib = [{
            'ENTRYTYPE': 'book',
            'ID': ID,
            'author': author,
            'title': title,
            'publisher': publisher,
            'year': str(year),
            'volume': volume,
            'series': series,
            'address': address,
            'edition': edition,
            'month': month,
            'note': note,
            'isbn': isbn
        }]
        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]

        print(list2)

        global data
        data = data + list2


class Journal(QDialog):
    def __init__(self, *args, **kwargs):
        super(Journal, self).__init__(*args, **kwargs)
        self.setWindowTitle("Journal")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()

        self.text1 = QLabel("Author(*):")
        self.text2 = QLabel("ID:")
        self.text3 = QLabel("Title(*):")
        self.text4 = QLabel("Year:")
        self.keyText = QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        ID = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()


        if author == "" or title == "" or ID == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            year = int(self.line4.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year must be a integer')
            return

        createBib = [{
            'ENTRYTYPE': 'journal',
            'ID': ID,
            'author': author,
            'title': title,
            'year': str(year),
        }]

        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]
        print(list2)
        global data
        data = data + list2


class Proceeding(QDialog):
    def __init__(self, *args, **kwargs):
        super(Proceeding, self).__init__(*args, **kwargs)
        self.setWindowTitle("Proceeeding")
        self.setFixedWidth(400)
        self.setFixedHeight(650)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()
        self.line7 = QLineEdit()
        self.line8 = QLineEdit()
        self.line9 = QLineEdit()
        self.line10 = QLineEdit()
        self.line11 = QLineEdit()

        self.text1 = QLabel("ID(*):")
        self.text2 = QLabel("Title(*):")
        self.text3 = QLabel("Year(*):")
        self.text4 = QLabel("Editor:")
        self.text5 = QLabel("Volume:")
        self.text6 = QLabel("Series:")
        self.text7 = QLabel("Address:")
        self.text8 = QLabel("Month:")
        self.text9 = QLabel("Organization:")
        self.text10 = QLabel("Publisher:")
        self.text11 = QLabel("Note:")
        self.keyText = QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)
        layout.addWidget(self.text6)
        layout.addWidget(self.line6)
        layout.addWidget(self.text7)
        layout.addWidget(self.line7)
        layout.addWidget(self.text8)
        layout.addWidget(self.line8)
        layout.addWidget(self.text9)
        layout.addWidget(self.line9)
        layout.addWidget(self.text10)
        layout.addWidget(self.line10)
        layout.addWidget(self.text11)
        layout.addWidget(self.line11)

        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        ID = self.line1.text()
        title = self.line2.text()
        year = self.line3.text()
        editor = self.line4.text()
        volume = self.line5.text()
        series = self.line6.text()
        address = self.line7.text()
        month = self.line8.text()
        organization = self.line9.text()
        publisher = self.line10.text()
        note = self.line11.text()

        if title == "" or year == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            year = int(self.line3.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year/Volume/Series must be a integer')
            return

        createBib = [{
            'ENTRYTYPE': 'proceedings',
            'ID': ID,
            'title': title,
            'year': str(year),
            'author': editor,
            'volume': volume,
            'series': series,
            'address': address,
            'month': month,
            'organization': organization,
            'publisher': publisher,
            'note': note
        }]

        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]
        print(list2)
        global data
        data = data + list2


class InProceeding(QDialog):
    def __init__(self, *args, **kwargs):
        super(InProceeding, self).__init__(*args, **kwargs)
        self.setWindowTitle("InProceeding")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()

        self.text1 = QLabel("Author(*):")
        self.text2 = QLabel("ID(*):")
        self.text3 = QLabel("Title(*):")
        self.text4 = QLabel("Year(*):")
        self.text5 = QLabel("Book Title:")
        self.keyText = QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)
        layout.addWidget(self.text6)
        layout.addWidget(self.line6)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        ID = self.line2.text()
        title = self.line3.text()
        booktitle = self.line5.text()
        if author == "" or title == "" or ID == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            ID = int(self.line5.text())
            year = int(self.line4.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year/ID must be a integer')
            return

        createBib = [{
            'ENTRYTYPE': 'inproceedings',
            'ID': ID,
            'author': author,
            'title': title,
            'year': str(year),
            'booktitle': booktitle
        }]

        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]
        print(list2)
        global data
        data = data + list2


class MasterThesis(QDialog):
    def __init__(self, *args, **kwargs):
        super(MasterThesis, self).__init__(*args, **kwargs)
        self.setWindowTitle("MasterThesis")
        self.setFixedWidth(400)
        self.setFixedHeight(400)


        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()
        self.line7 = QLineEdit()
        self.line8 = QLineEdit()

        self.text1 = QLabel("ID(*):")
        self.text2 = QLabel("Author(*):")
        self.text3 = QLabel("Title(*):")
        self.text4 = QLabel("School:")
        self.text5 = QLabel("Year:")
        self.text6 = QLabel("Address:")
        self.text7 = QLabel("Month:")
        self.text8 = QLabel("Note:")

        self.keyText = QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)
        layout.addWidget(self.text6)
        layout.addWidget(self.line6)
        layout.addWidget(self.text7)
        layout.addWidget(self.line7)
        layout.addWidget(self.text8)
        layout.addWidget(self.line8)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        ID = self.line1.text()
        author = self.line2.text()
        title = self.line3.text()
        school = self.line4.text()
        year = self.line5.text()
        address = self.line6.text()
        month = self.line7.text()
        note = self.line8.text()

        if author == "" or title == "" or ID == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            year = int(self.line5.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year/ID must be a integer')
            return

        createBib = [{
            'ENTRYTYPE': 'mastersthesis',
            'ID': ID,
            'author': author,
            'title': title,
            'school': school,
            'year': str(year),
            'address': address,
            'month': month,
            'note': note
        }]

        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]
        print(list2)
        global data
        data = data + list2


class PhdThesis(QDialog):
    def __init__(self, *args, **kwargs):
        super(PhdThesis, self).__init__(*args, **kwargs)
        self.setWindowTitle("MasterThesis")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()
        self.line7 = QLineEdit()
        self.line8 = QLineEdit()

        self.text1 = QLabel("ID(*):")
        self.text2 = QLabel("Author(*):")
        self.text3 = QLabel("Title(*):")
        self.text4 = QLabel("School:")
        self.text5 = QLabel("Year(*):")
        self.text6 = QLabel("Address:")
        self.text7 = QLabel("Month:")
        self.text8 = QLabel("Note:")

        self.keyText = QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)
        layout.addWidget(self.text6)
        layout.addWidget(self.line6)
        layout.addWidget(self.text7)
        layout.addWidget(self.line7)
        layout.addWidget(self.text8)
        layout.addWidget(self.line8)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        ID = self.line1.text()
        author = self.line2.text()
        title = self.line3.text()
        school = self.line4.text()
        year = self.line5.text()
        address = self.line6.text()
        month = self.line7.text()
        note = self.line8.text()

        if author == "" or title == "" or ID == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            year = int(self.line5.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year must be a integer')
            return

        createBib = [{
            'ENTRYTYPE': 'phdthesis',
            'ID': ID,
            'author': author,
            'title': title,
            'school': school,
            'year': str(year),
            'address': address,
            'month': month,
            'note': note
        }]

        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]
        print(list2)
        global data
        data = data + list2


class Unpublished(QDialog):
    def __init__(self, *args, **kwargs):
        super(Unpublished, self).__init__(*args, **kwargs)
        self.setWindowTitle("Unpublished")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()

        self.text1 = QLabel("ID(*):")
        self.text2 = QLabel("Author(*):")
        self.text3 = QLabel("Title(*):")
        self.text4 = QLabel("Year(*):")
        self.text5 = QLabel("Note:")

        self.keyText = QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)

        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        ID = self.line1.text()
        author = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()
        note = self.line5.text()

        if author == "" or title == "" or ID == "" or year == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            year = int(self.line4.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year must be a integer')
            return

        createBib = [{
            'ENTRYTYPE': 'unpublished',
            'ID': ID,
            'author': author,
            'title': title,
            'year': str(year),
            'note': note
        }]

        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]
        print(list2)
        global data
        data = data + list2

class Misc(QDialog):
    def __init__(self, *args, **kwargs):
        super(Misc, self).__init__(*args, **kwargs)
        self.setWindowTitle("Unpublished")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()
        self.line7 = QLineEdit()

        self.text1 = QLabel("ID(*):")
        self.text2 = QLabel("Author(*):")
        self.text3 = QLabel("Title(*):")
        self.text4 = QLabel("How Published:")
        self.text5 = QLabel("Month:")
        self.text6 = QLabel("Year(*):")
        self.text7 = QLabel("Note:")

        self.keyText = QLabel("Key values must be filled(*)")
        self.keyText.setStyleSheet('color: red')

        layout = QVBoxLayout()
        layout.addWidget(self.keyText)
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)
        layout.addWidget(self.text6)
        layout.addWidget(self.line6)
        layout.addWidget(self.text7)
        layout.addWidget(self.line7)


        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.createButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        ID = self.line1.text()
        author = self.line2.text()
        title = self.line3.text()
        howpublished = self.line4.text()
        month = self.line5.text()
        year = self.line6.text()
        note = self.line7.text()

        if author == "" or title == "" or ID == "" or year == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Key values can not be null')
            return

        try:
            year = int(self.line6.text())

        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Year must be a integer')
            return

        createBib = [{
            'ENTRYTYPE': 'misc',
            'ID': ID,
            'author': author,
            'title': title,
            'howpublished': howpublished,
            'month': month,
            'year': str(year),
            'note': note
        }]

        list2 = [{k: v for k, v in i.items() if v != '' or v.strip() != ''} for i in createBib]
        print(list2)
        global data
        data = data + list2


class FilterDialog(QDialog):
    rowdataauthor = []
    rowdatatitle = []
    rowdatatype = []
    yeardata = []
    filteredlist=[]


    def __init__(self, *args, **kwargs):
        super(FilterDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 459)
        self.pushButtonsearch = QtWidgets.QPushButton(Dialog)
        self.pushButtonsearch.setGeometry(QtCore.QRect(310, 400, 75, 23))
        self.pushButtonsearch.setObjectName("pushButtonsearch")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 120, 401, 194))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidgetauthor = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidgetauthor.setObjectName("tableWidgetauthor")
        self.tableWidgetauthor.setColumnCount(1)
        self.tableWidgetauthor.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetauthor.setHorizontalHeaderItem(0, item)
        self.horizontalLayout.addWidget(self.tableWidgetauthor)
        self.tableWidgettitle = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidgettitle.setObjectName("tableWidgettitle")
        self.tableWidgettitle.setColumnCount(1)
        self.tableWidgettitle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgettitle.setHorizontalHeaderItem(0, item)
        self.horizontalLayout.addWidget(self.tableWidgettitle)
        self.tableWidgettype = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidgettype.setObjectName("tableWidgettype")
        self.tableWidgettype.setColumnCount(1)
        self.tableWidgettype.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgettype.setHorizontalHeaderItem(0, item)
        self.horizontalLayout.addWidget(self.tableWidgettype)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 90, 401, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonaddauthor = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonaddauthor.setObjectName("pushButtonaddauthor")
        self.horizontalLayout_2.addWidget(self.pushButtonaddauthor)
        self.pushButtonaddtitle = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonaddtitle.setObjectName("pushButtonaddtitle")
        self.horizontalLayout_2.addWidget(self.pushButtonaddtitle)
        self.pushButtonaddtype = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonaddtype.setObjectName("pushButtonaddtype")
        self.horizontalLayout_2.addWidget(self.pushButtonaddtype)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 20, 401, 20))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(19, 360, 401, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdityearto = QtWidgets.QLineEdit(self.layoutWidget3)  # year to
        self.lineEdityearto.setObjectName("lineEdityearto")
        self.horizontalLayout_5.addWidget(self.lineEdityearto)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEditfrom = QtWidgets.QLineEdit(self.layoutWidget3)  # year from
        self.lineEditfrom.setObjectName("lineEditfrom")
        self.horizontalLayout_5.addWidget(self.lineEditfrom)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # function calls for buttons on the screen
        self.pushButtonaddauthor.clicked.connect(self.addNewRowAuthor)
        self.pushButtonaddtitle.clicked.connect(self.addNewRowTitle)
        self.pushButtonaddtype.clicked.connect(self.addNewRowType)

        self.pushButtonsearch.clicked.connect(self.saveAuthortable)
        self.pushButtonsearch.clicked.connect(self.saveTitletable)
        self.pushButtonsearch.clicked.connect(self.saveTypetabel)
        self.pushButtonsearch.clicked.connect(self.saveYear)
        self.pushButtonsearch.clicked.connect(self.filtering)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Filter"))

        self.pushButtonsearch.setText(_translate("Dialog", "SEARCH"))
        item = self.tableWidgetauthor.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Author"))
        item = self.tableWidgettitle.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "TITLE"))
        item = self.tableWidgettype.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "TYPE"))
        self.pushButtonaddauthor.setText(_translate("Dialog", "ADD"))
        self.pushButtonaddtitle.setText(_translate("Dialog", "ADD"))
        self.pushButtonaddtype.setText(_translate("Dialog", "ADD"))
        self.label.setText(_translate("Dialog", "               AUTHOR"))
        self.label_2.setText(_translate("Dialog", "                TITLE"))
        self.label_3.setText(_translate("Dialog", "                 TYPE"))
        self.label_4.setText(_translate("Dialog", "Year to"))
        self.label_5.setText(_translate("Dialog", "year from"))

    def addNewRowAuthor(self):  # add row Author table
        rowPosition = self.tableWidgetauthor.rowCount()
        self.tableWidgetauthor.insertRow(rowPosition)

    def saveAuthortable(self):

        for x in range(self.tableWidgetauthor.rowCount()):
            item = self.tableWidgetauthor.item(x, 0)
            if item is not None:

                self.rowdataauthor.append(item.text())
            else:
                self.rowdataauthor.append('')



        #print(rowdataauthor)  # silincek

    def addNewRowTitle(self):  # add row Title table
        rowPosition = self.tableWidgettitle.rowCount()
        self.tableWidgettitle.insertRow(rowPosition)

    def saveTitletable(self):


        for x in range(self.tableWidgettitle.rowCount()):
            item = self.tableWidgettitle.item(x, 0)
            if item is not None:

                self.rowdatatitle.append(item.text())
            else:
                self.rowdatatitle.append('')

        #print(self.rowdatatitle)  # silinecek

    def addNewRowType(self):  # add row Type table
        rowPosition = self.tableWidgettype.rowCount()
        self.tableWidgettype.insertRow(rowPosition)

    def saveTypetabel(self):


        for x in range(self.tableWidgettype.rowCount()):
            item = self.tableWidgettype.item(x, 0)
            if item is not None:

                self.rowdatatype.append(item.text())
            else:
                self.rowdatatype.append('')

        #print(self.rowdatatype)  # silinecek

    def saveYear(self):

        yearto = self.lineEdityearto.text()
        yearfrom = self.lineEditfrom.text()
        # print(yearto)
        # print(yearfrom)

        a = int(yearto)
        b = int(yearfrom)

        if a < b:
            while a < b:
                d = a + 1
                self.yeardata.append(d)
                a = d

        else:
            while b < a:
                ey = b + 1
                self.yeardata.append(ey)
                b = ey


        #print(self.yeardata)

    def filtering(self):

        item=self.filteredlist
        # searching author
        while bool(self.rowdataauthor):
            for a in self.rowdataauthor:
                input=a
                for item in MainWindow.data:
                    for b in item.items():
                        if input in b:
                            self.filteredlist.append(item)
                            #print(self.filteredlist)
            break
          # searching title

        while bool(self.rowdatatitle):
            for c in self.rowdatatitle:
                input=c
                for item in MainWindow.data:
                    for d in item.items():
                        if input in d:
                            self.filteredlist.append(item)
                            #print(self.filteredlist)
            break
         #searching type
        while bool(self.rowdatatype):
            for e in self.rowdatatype:
                input=e
                for item in MainWindow.data:
                    for f in item.items():
                        if input in f:
                            self.filteredlist.append(item)
                            #print(self.filteredlist)
            break
           # searching year
        while bool(self.yeardata):
            for g in self.yeardata:
                input=g
                for item in MainWindow.data:
                    for h in item.items():
                        if input in h:
                            self.filteredlist.append(item)
                            #print(self.filteredlist)
            break

        print(self.filteredlist)


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        # Pelinsu Arslan Task
        # Search code will be here
        self.searchString = "Shi"
        self.setWindowTitle("Search")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        layout = QFormLayout()
        self.setWindowTitle("Search")
        self.setFixedWidth(400)
        self.setFixedHeight(100)
        self.searchButton = QPushButton("Search")
        self.line1 = QLineEdit()
        self.text1 = QLabel("Please enter")
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.btn_clk)
        self.searchButton.clicked.connect(self.close)
        self.setLayout(layout)

    def btn_clk(self):
        input = self.line1.text()
        global data
        global searchedList
        item = searchedList
        for item in data:
            for k, v in item.items():
                if input in v:
                    searchedList.append(item)


class CreateAuthorIdentityDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CreateAuthorIdentityDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

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
        self.cancelIdentity.clicked.connect(self.close)

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
        # Supports Turkish special characters with UTF-8 encoding
        with open('authorIdentityData.csv', 'w', encoding='UTF-8', newline='') as stream:
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

        # Displays SAVED message after Save button is clicked
        msg = QMessageBox()
        QMessageBox.about(msg, "Status", "SAVED")

        # Gets author identity data from csv file and puts the contents into a list
        with open('authorIdentityData.csv', 'r', encoding='UTF-8', newline='') as csv_file:
            authorIdentityData = list(csv.reader(csv_file))
        print(authorIdentityData)

    # Imports author identity data from the csv file into the table widget
    def loadAuthorIdentityData(self):
        # Support Turkish special characters with UTF-8 encoding
        with open('authorIdentityData.csv', 'r', encoding='UTF-8', newline='') as csv_file:
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


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = MainWindow()
    window.show()

sys.exit(app.exec_())