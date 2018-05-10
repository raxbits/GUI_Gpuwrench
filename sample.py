import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QPushButton, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from subprocess import check_output,call


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'VaNdEtTa'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createTable()
        self.createButtons()
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.layout.addWidget(self.r_bt)
        self.layout.addWidget(self.i_bt) 
        self.layout.addWidget(self.os_bt) 
        self.setLayout(self.layout) 
 
        # Show widget
        self.show()
 
    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setItem(0,0, QTableWidgetItem(""))

        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
    def createButtons(self):
        self.r_bt = QPushButton("Open System Report")
        self.i_bt = QPushButton("Quick Info")
        self.os_bt = QPushButton("OS Info")
        self.r_bt.clicked.connect(self.r_bt_handler)
        self.i_bt.clicked.connect(self.i_bt_handler)
        self.os_bt.clicked.connect(self.os_bt_handler)
    
    def i_bt_handler(self):
        txt=check_output(["./gpuwrench", "-i"])

        alist=txt.decode()
        alist=alist.rstrip()

        self.tableWidget.setItem(0,0, QTableWidgetItem(alist))

    def r_bt_handler(self):
        call(["./gpuwrench", "-r"])

    def os_bt_handler(self):
        txt=check_output(["./gpuwrench", "-o"])

        alist=txt.decode()
        alist=alist.rstrip()

        print(alist)
        self.tableWidget.setItem(0,0, QTableWidgetItem(alist))
    
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())