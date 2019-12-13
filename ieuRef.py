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

class CreateDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CreateDialog, self).__init__(*args, **kwargs)
        #Necati Ozkent Task
        #Creating entry code will be here
        #Different types will have different fields


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        #Pelinsu Arslan Task
        #Search code will be here


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = MainWindow()
    window.show()
sys.exit(app.exec_())
