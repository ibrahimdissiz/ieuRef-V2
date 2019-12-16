import sys
import bibtexparser
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/logo.png'))
        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("IeuRef")
        self.setMinimumSize(1000, 800)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
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

        selectBibtex_action = QAction(QIcon("icon/addBibtex.png"), "Select BibTeX file", self)
        selectBibtex_action.triggered.connect(self.selectBibtex)
        file_menu.addAction(selectBibtex_action)

        createBibtex_action = QAction(QIcon("icon/create.png"), "Create Bibtex", self)
        createBibtex_action.triggered.connect(self.createBibtex)
        file_menu.addAction(createBibtex_action)

        searchBibtex_action = QAction(QIcon("icon/search.png"), "Search Student", self)
        searchBibtex_action.triggered.connect(self.search)
        file_menu.addAction(searchBibtex_action)

        filterBibtex_action = QAction(QIcon("icon/filterBibtex.png"), "Filter BibTeX ", self)
        filterBibtex_action.triggered.connect(self.filterBibtex)
        file_menu.addAction(filterBibtex_action)

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

    def loaddata(self, author, title, year, type1):
        # Dummy data for searching
        # self.tableWidget.setRowCount(5)
        # self.tableWidget.setItem(0, 0, QTableWidgetItem("1"))
        # self.tableWidget.setItem(0, 1, QTableWidgetItem("Cai, Hongyun and Zheng, Vincent W. and Zhu, Fanwei and Chang, Kevin Chen-Chuan and Huang, Zi"))
        # self.tableWidget.setItem(0, 2, QTableWidgetItem("2017"))
        # self.tableWidget.setItem(0, 3, QTableWidgetItem("article"))
        # self.tableWidget.setItem(0, 4, QTableWidgetItem("From Community Detection to Community Profiling"))
        #
        # self.tableWidget.setItem(1, 0, QTableWidgetItem("2"))
        # self.tableWidget.setItem(1, 1, QTableWidgetItem("Jantz, Michael R. and Robinson, Forrest J. and Kulkarni, Prasad A."))
        # self.tableWidget.setItem(1, 2, QTableWidgetItem("2016"))
        # self.tableWidget.setItem(1, 3, QTableWidgetItem("article"))
        # self.tableWidget.setItem(1, 4, QTableWidgetItem("Impact of Intrinsic Profiling Limitations on Effectiveness of Adaptive Optimizations"))
        #
        # self.tableWidget.setItem(2, 0, QTableWidgetItem("3"))
        # self.tableWidget.setItem(2, 1, QTableWidgetItem("Sharma, Sanket S. and De Choudhury, Munmun"))
        # self.tableWidget.setItem(2, 2, QTableWidgetItem("2015"))
        # self.tableWidget.setItem(2, 3, QTableWidgetItem("inproceedings"))
        # self.tableWidget.setItem(2, 4, QTableWidgetItem("Measuring and Characterizing Nutritional Information of Food and Ingestion Content in Instagram"))
        #
        # self.tableWidget.setItem(3, 0, QTableWidgetItem("4"))
        # self.tableWidget.setItem(3, 1, QTableWidgetItem("Zhan, Ming and Tu, Ruibo and Yu, Qin"))
        # self.tableWidget.setItem(3, 2, QTableWidgetItem("2018"))
        # self.tableWidget.setItem(3, 3, QTableWidgetItem("inproceedings"))
        # self.tableWidget.setItem(3, 4, QTableWidgetItem("Understanding Readers: Conducting Sentiment Analysis of Instagram Captions"))
        #
        # self.tableWidget.setItem(4, 0, QTableWidgetItem("5"))
        # self.tableWidget.setItem(4, 1, QTableWidgetItem("Schlauch, Wolfgang E. and Zweig, Katharina A. and Theory, Graph and Analysis, Network"))
        # self.tableWidget.setItem(4, 2, QTableWidgetItem("2015"))
        # self.tableWidget.setItem(4, 3, QTableWidgetItem("inproceedings"))
        # self.tableWidget.setItem(4, 4, QTableWidgetItem("Influence of the Null-Model on Motif Detection"))

        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(author))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(title))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(year))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(type1))

    def createBibtex(self):
        dlg = CreateDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def selectBibtex(self):
        options = QFileDialog.Options()
        bibtexFile, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                    "BibTeX Files (*.bib)", options=options)

        with open(bibtexFile) as bibtex:

            try:
                bibtex_database = bibtexparser.load(bibtex)
                keyys = bibtex_database.entries
                print(keyys[0].keys())
                author = bibtex_database.entries[0]["author"]  # x yerine istenileni yaz ("title") mesela
                year = bibtex_database.entries[0]["year"]
                title = bibtex_database.entries[0]["title"]
                type1 = bibtex_database.entries[0]["ENTRYTYPE"]
                print(author)
                print(year)
                print(title)
                print(type1)
                self.loaddata(author, year, type1, title)

            except Exception:
                print(format(Exception))
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not load Bibtex file.')

    def filterBibtex(self):
        dlg =FilterDialog()
        dlg.exec_()


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

        layout.addWidget(self.boxlabel)
        layout.addWidget(self.typeinput)
        self.setLayout(layout)

    def selected(self, data):
        if data == "Article":
            dlc = Article()
            dlc.exec_()
        if data == "Book":
            dlc = Book()
            dlc.exec_()
        if data == "Journal":
            dlc = Journal()
            dlc.exec_()
        if data == "Proceeding":
            dlc = Proceeding()
            dlc.exec_()
        if data == "InProceeding":
            dlc = InProceeding()
            dlc.exec_()
        if data == "MasterThesis":
            dlc = MasterThesis()
            dlc.exec_()
        if data == "PhdThesis":
            dlc = PhdThesis()
            dlc.exec_()
        if data == "Unpublished":
            dlc = Unpublished()
            dlc.exec_()
        if data == "Misc":
            dlc = Misc()
            dlc.exec_()


class Article(QDialog):
    def __init__(self, *args, **kwargs):
        super(Article, self).__init__(*args, **kwargs)

        self.setWindowTitle("Article")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()

        self.text1 = QLabel("Author:")
        self.text2 = QLabel("BibTeXKey:")
        self.text3 = QLabel("Title:")
        self.text4 = QLabel("Year:")
        self.text5 = QLabel("ID:")
        self.text6 = QLabel("Journal:")

        layout = QVBoxLayout()
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
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        bibtexkey = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()
        ID = self.line5.text()
        journal = self.line6.text()

        newfile = open(str(bibtexkey) + ".bib", "w")
        newfile.write(
            "@" + "article" + "{" + str(bibtexkey) + "," + "\nAuthor=" + author + "\nYear=" + str(
                year) + "\nTitle=" + title + "\n journal=" + journal + "\n ID=" + str(ID) + "\n}")

        newfile.close()


class Book(QDialog):
    def __init__(self, *args, **kwargs):
        super(Book, self).__init__(*args, **kwargs)
        self.setWindowTitle("Book")
        self.setFixedWidth(400)
        self.setFixedHeight(400)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()

        self.text1 = QLabel("Author:")
        self.text2 = QLabel("BibTeXKey:")
        self.text3 = QLabel("Title:")
        self.text4 = QLabel("Year:")
        self.text5 = QLabel("ID:")
        self.text6 = QLabel("Publisher:")

        layout = QVBoxLayout()
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
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        bibtexkey = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()
        ID = self.line5.text()
        publisher = self.line6.text()

        newfile = open(str(bibtexkey) + ".bib", "w")
        newfile.write(
            "@" + "book" + "{" + str(bibtexkey) + "," + "\nAuthor=" + author + "\nYear=" + str(
                year) + "\nTitle=" + title + "\n publisher=" + publisher + "\n ID=" + str(ID) + "\n}")

        newfile.close()


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
        self.line5 = QLineEdit()

        self.text1 = QLabel("Author:")
        self.text2 = QLabel("BibTeXKey:")
        self.text3 = QLabel("Title:")
        self.text4 = QLabel("Year:")
        self.text5 = QLabel("ID:")

        layout = QVBoxLayout()
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
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        bibtexkey = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()
        ID = self.line5.text()

        newfile = open(str(bibtexkey) + ".bib", "w")
        newfile.write(
            "@" + "journal" + "{" + str(bibtexkey) + "," + "\nAuthor=" + author + "\nYear=" + str(
                year) + "\nTitle=" + title + "\n ID=" + str(ID) + "\n}")

        newfile.close()


class Proceeding(QDialog):
    def __init__(self, *args, **kwargs):
        super(Proceeding, self).__init__(*args, **kwargs)
        self.setWindowTitle("Proceeeding")
        self.setFixedWidth(400)
        self.setFixedHeight(200)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()

        self.text1 = QLabel("Title:")
        self.text2 = QLabel("Year:")

        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.setLayout(layout)

    def btn_clk(self):
        title = self.line1.text()
        year = self.line2.text()

        newfile = open("Proceeding.bib", "w")
        newfile.write(
            "@" + "proceeding" + "{" "\nYear=" + str(year) + "\nTitle=" + title + "\n}")

        newfile.close()


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
        self.line6 = QLineEdit()

        self.text1 = QLabel("Author:")
        self.text2 = QLabel("BibTeXKey:")
        self.text3 = QLabel("Title:")
        self.text4 = QLabel("Year:")
        self.text5 = QLabel("ID:")
        self.text6 = QLabel("Book Title:")

        layout = QVBoxLayout()
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
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        bibtexkey = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()
        ID = self.line5.text()
        booktitle = self.line6.text()

        newfile = open(str(bibtexkey) + ".bib", "w")
        newfile.write(
            "@" + "inproceeding" + "{" + str(bibtexkey) + "," + "\nAuthor=" + author + "\nYear=" + str(
                year) + "\nTitle=" + title + "\n book title=" + booktitle + "\n ID=" + str(ID) + "\n}")

        newfile.close()


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

        self.text1 = QLabel("Author:")
        self.text2 = QLabel("BibTeXKey:")
        self.text3 = QLabel("Title:")
        self.text4 = QLabel("Year:")
        self.text5 = QLabel("ID:")
        self.text6 = QLabel("School:")

        layout = QVBoxLayout()
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
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        bibtexkey = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()
        ID = self.line5.text()
        school = self.line6.text()

        newfile = open(str(bibtexkey) + ".bib", "w")
        newfile.write(
            "@" + "masterthesis" + "{" + str(bibtexkey) + "," + "\nAuthor=" + author + "\nYear=" + str(
                year) + "\nTitle=" + title + "\n school=" + school + "\n ID=" + str(ID) + "\n}")

        newfile.close()


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

        self.text1 = QLabel("Author:")
        self.text2 = QLabel("BibTeXKey:")
        self.text3 = QLabel("Title:")
        self.text4 = QLabel("Year:")
        self.text5 = QLabel("ID:")
        self.text6 = QLabel("School:")

        layout = QVBoxLayout()
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
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        bibtexkey = self.line2.text()
        title = self.line3.text()
        year = self.line4.text()
        ID = self.line5.text()
        school = self.line6.text()

        newfile = open(str(bibtexkey) + ".bib", "w")
        newfile.write(
            "@" + "phdthesis" + "{" + str(bibtexkey) + "," + "\nAuthor=" + author + "\nYear=" + str(
                year) + "\nTitle=" + title + "\n school=" + school + "\n ID=" + str(ID) + "\n}")

        newfile.close()


class Unpublished(QDialog):
    def __init__(self, *args, **kwargs):
        super(Unpublished, self).__init__(*args, **kwargs)
        self.setWindowTitle("Unpublished")
        self.setFixedWidth(400)
        self.setFixedHeight(250)

        self.createButton = QPushButton("Create")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()

        self.text1 = QLabel("Author:")
        self.text2 = QLabel("Title:")
        self.text3 = QLabel("Note:")

        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.line3)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        title = self.line2.text()
        note = self.line3.text()

        newfile = open("Unpublished.bib", "w")
        newfile.write(
            "@" + "unpublished" + "{," + "\nAuthor=" + author + "\nTitle=" + title + "\n note=" + note + "\n}")

        newfile.close()


class Misc(QDialog):
    def __init__(self, *args, **kwargs):
        super(Misc, self).__init__(*args, **kwargs)
        self.setWindowTitle("Misc")
        self.setFixedWidth(250)
        self.setFixedHeight(100)

        self.createButton = QPushButton("Create")

        self.text1 = QLabel("Click create for creating a misc file")

        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.createButton)
        self.createButton.clicked.connect(self.btn_clk)
        self.setLayout(layout)

    def btn_clk(self):


        newfile = open("misc.bib", "w")
        newfile.write(
            "@" + "misc" + "{" "\n}")

        newfile.close()

class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        # Pelinsu Arslan Task
        # Search code will be here


class FilterDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(FilterDialog, self).__init__(*args, **kwargs)

        self.setWindowsTitle("Filter")
        self.setFixedWidht(800)
        self.setFixedHeight(800)

        self.createButton = QPushButton("Filter")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()




        self.text1 = QLabel("Index 1:")
        self.text2 = QLabel("Index 2:")
        self.text3 = QLabel("Index 2:")
        self.text4 = QLabel("Year From:")
        self.text5 = QLabel("Year To:")

        layout = QFormLayout()
        self.combobox1 = QComboBox()
        self.combobox1.addItem("-Please select a Type or Author")
        self.combobox1.addItem("Type")
        self.combobox1.addItem("Author")
        self.combobox1.activated[str].connect(self.selected)

        self.combobox2 = QComboBox()
        self.combobox2.addItem("-Please select a Type or Author")
        self.combobox2.addItem("Type")
        self.combobox2.addItem("Author")
        self.combobox2.activated[str].connect(self.selected)

        self.combobox3 = QComboBox()
        self.combobox3.addItem("-Please select a Type or Author")
        self.combobox3.addItem("Type")
        self.combobox3.addItem("Author")
        self.combobox3.activated[str].connect(self.selected)



        layout.addWidget(self.boxlabel)

        self.setLayout(layout)


        layout.addWidget(self.text1)
        layout.addWidget(self.combobox1)
        layout.addWidget(self.line1)
        layout.addWidget(self.text2)
        layout.addWidget(self.combobox2)
        layout.addWidget(self.line2)
        layout.addWidget(self.text3)
        layout.addWidget(self.combobox3)
        layout.addWidget(self.line3)
        layout.addWidget(self.text4)
        layout.addWidget(self.line4)
        layout.addWidget(self.text5)
        layout.addWidget(self.line5)

        self.filterButton.clicked.connect(self.btn_clk)
        self.setLayout(layout)

    def selected(self,data):
        if data == "Type":
            dlc = Type()
            dlc.exec_()
        if data == "Author":
            dlc =Author()
            dlc.exec_()



    def btn_clk(self):
        index1 = self.line1.text()
        index2 = self.line2.text()
        index3 = self.line3.text()
        yearfrom = self.line4.text()
        yearto = self.line5.text()

        newfile = open(str())



app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = MainWindow()
    window.show()
sys.exit(app.exec_())