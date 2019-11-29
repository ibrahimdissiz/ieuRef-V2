import sys
import bibtexparser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QStringList(object):
    pass


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/logo.png'))  #window icon

        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("IeuRef")
        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(4)
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

        btn_ac_file = QAction(QIcon("icon/file.png"), "Select File", self)  # add student icon
        btn_ac_file.triggered.connect(self.selectBibtex)
        btn_ac_file.setStatusTip("Select File")
        toolbar.addAction(btn_ac_file)

        # btn_ac_refresh = QAction(QIcon("icon/logo.png"), "Refresh", self)  # refresh icon
        # btn_ac_refresh.triggered.connect(self.loaddata)
        # btn_ac_refresh.setStatusTip("Refresh Table")
        # toolbar.addAction(btn_ac_refresh)

        selectBibtex_action = QAction(QIcon("icon/addBibtex.png"), "Select BibTeX file", self)
        selectBibtex_action.triggered.connect(self.selectBibtex)
        file_menu.addAction(selectBibtex_action)

    def selectBibtex(self):
        options = QFileDialog.Options()
        bibtexFile, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "BibTeX Files (*.bib)", options=options)
        if bibtexFile:
            print(bibtexFile)

        # Bibtex parser will be here
        # with open(bibtexFile) as bibtex:
        #     try:
        #         bibtex_database = bibtexparser.load(bibtex)
        #     except Exception:
        #         print(format(Exception))
        #         QMessageBox.warning(QMessageBox(), 'Error', 'Could not load Bibtex file.')
        #     keyys = bibtex_database.entries
        #     print(keyys[0].keys())
        #     author = bibtex_database.entries[0]["author"]  # x yerine istenileni yaz ("title") mesela
        #     year = bibtex_database.entries[0]["year"]
        #     title = bibtex_database.entries[0]["title"]
        #     type1 = bibtex_database.entries[0]["ENTRYTYPE"]
        #     print(author, year, title, type1)
            data = {[author, year, type1, title]}

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    # def setData(self):
    #
    #     for m, item in enumerate(self.data[ ]):
    #         newitem = QTableWidgetItem(item)
    #         self.setItem(m, n, newitem)
    #         # self.tableWidget.setRowCount(0)
    #         # for row_number, row_data in type1(4, ):
    #         #     self.tableWidget.insertRow(row_number)
    #         #     for column_number, data in enumerate(author, year, type1, title):
    #         #         self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    #
    #         print(author, year, title, type1)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())