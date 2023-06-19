from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pathlib
from pathlib import Path


#def dbconnect(self):
#    """
#    connecting DB
#    """
#    sqlite_connect = sqlite3.connect('airports.db')
#    cursor = sqlite_connect.cursor()
#    cursor.execute(f"SELECT city FROM airports ORDER BY city ASC")
#    return [city for cities in cursor.fetchall() for city in cities]


class UiRoot(object):

#    def __init__(self):
#        self.dbconnect = dbconnect

    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(791, 750)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(root.sizePolicy().hasHeightForWidth())

        root.setSizePolicy(sizePolicy)
        root.setStyleSheet("background-color: rgb(192, 193, 199);\n" "border-color: rgb(0, 4, 255);")
        root.setSizeGripEnabled(False)
        root.setModal(False)

        self.buttonBox = QtWidgets.QDialogButtonBox(root)
        self.buttonBox.setGeometry(QtCore.QRect(600, 0, 171, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())

        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 50))
        self.buttonBox.setMaximumSize(QtCore.QSize(500, 200))
        self.buttonBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.buttonBox.setBaseSize(QtCore.QSize(0, 0))
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.tableWidget = QtWidgets.QTableWidget(root)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 750, 630))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())

        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(('Airlines', 'depart city', 'arrive city', 'latitude', 'longitude'))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.label = QtWidgets.QLabel(root)
        self.label.setGeometry(QtCore.QRect(90, 0, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(root)
        self.label_2.setGeometry(QtCore.QRect(370, 0, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)

        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(root)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)

        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(root)
        self.label_4.setGeometry(QtCore.QRect(370, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)

        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.textBrowser_4 = QtWidgets.QTextBrowser(root)
        self.textBrowser_4.setGeometry(QtCore.QRect(30, 20, 221, 21))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setReadOnly(False)
        self.textBrowser_4.setOverwriteMode(True)
        self.textBrowser_4.setPlaceholderText("")
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.textBrowser_5 = QtWidgets.QTextBrowser(root)
        self.textBrowser_5.setGeometry(QtCore.QRect(310, 20, 221, 21))
        self.textBrowser_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setReadOnly(False)
        self.textBrowser_5.setOverwriteMode(True)
        self.textBrowser_5.setPlaceholderText("")
        self.textBrowser_5.setObjectName("textBrowser_5")

        self.textBrowser_6 = QtWidgets.QTextBrowser(root)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 60, 221, 21))
        self.textBrowser_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_6.setReadOnly(False)
        self.textBrowser_6.setOverwriteMode(True)
        self.textBrowser_6.setPlaceholderText("")
        self.textBrowser_6.setObjectName("textBrowser_6")

        self.textBrowser_7 = QtWidgets.QTextBrowser(root)
        self.textBrowser_7.setGeometry(QtCore.QRect(310, 60, 221, 21))
        self.textBrowser_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_7.setReadOnly(False)
        self.textBrowser_7.setOverwriteMode(True)
        self.textBrowser_7.setPlaceholderText("")
        self.textBrowser_7.setObjectName("textBrowser_7")

        self.retranslateUi(root)
        self.buttonBox.accepted.connect(root.accept) # type: ignore
        self.buttonBox.rejected.connect(root.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(root)

    def table_input(self, data):
        """insert data from DB"""
        self.tableWidget.setRowCount(len(data))
        for i, j in enumerate(data):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(j[0]))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(j[1]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(j[2]))
    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "Airplane location"))
        self.label.setText(_translate("root", "Min latitude"))
        self.label_2.setText(_translate("root", "Max latitude"))
        self.label_3.setText(_translate("root", "Min longitude"))
        self.label_4.setText(_translate("root", "Max longitude"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QDialog()
    ui = UiRoot()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
