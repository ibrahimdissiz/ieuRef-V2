import sys
import bibtexparser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/logo.png'))
        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("IeuRef")
        self.setMinimumSize(900, 700)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("No.", "Author", "Year", "Type", "Title"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        selectBibtex_action = QAction(QIcon("icon/addBibtex.png"), "Select BibTeX file", self)
        selectBibtex_action.triggered.connect(self.selectBibtex)
        file_menu.addAction(selectBibtex_action)

        createbibtex_action = QAction(QIcon("icon/create.png"),"Create Bibtex", self)
        createbibtex_action.triggered.connect(self.createBibtex)
        file_menu.addAction(createbibtex_action)

    def loadData(self, a, b, c, d):
        self.tableWidget.setItem(1, 0, QTableWidgetItem(a))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(b))
        self.tableWidget.setItem(1, 2, QTableWidgetItem(c))
        self.tableWidget.setItem(1, 3, QTableWidgetItem(d))


    def createBibtex(self):
        dlg = CreateDialog()
        dlg.exec()

    def selectBibtex(self):
        options = QFileDialog.Options()
        bibtexFile, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "BibTeX Files (*.bib)", options=options)
        if bibtexFile:
            print(bibtexFile)
        # dlg = SelectDialog()
        # dlg.exec_()

        with open(bibtexFile) as bibtex:

            try:
                bibtex_database = bibtexparser.load(bibtex)
            except Exception:
                print(format(Exception))
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not load Bibtex file.')
            keyys = bibtex_database.entries
            print(keyys[0].keys())
            author = bibtex_database.entries[0]["author"]  # x yerine istenileni yaz ("title") mesela
            year = bibtex_database.entries[0]["year"]
            title = bibtex_database.entries[0]["title"]
            type1 = bibtex_database.entries[0]["ENTRYTYPE"]
            self.loadData(author, year, title, type1)

            print(author)
            print(year)
            print(title)
            print(type1)

class CreateDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(CreateDialog, self).__init__(*args, **kwargs)
        # Code of Necati Ozkent will be here



app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = MainWindow()
    window.show()
sys.exit(app.exec_())
