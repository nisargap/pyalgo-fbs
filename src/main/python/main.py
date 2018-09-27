from fbs_runtime.application_context import ApplicationContext,  cached_property
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QLineEdit, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QCalendarWidget, QPushButton

import sys

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):
        self.window.show()
        stylesheet = self.get_resource('styles.qss')
        self.app.setStyleSheet(open(stylesheet).read())
        return self.app.exec_()
    @cached_property
    def window(self):
        mw = MainWindow()
        return mw

def createCalendar(ref, clickAction):
    cal = QCalendarWidget(ref)
    cal.setGridVisible(True)
    cal.clicked[QDate].connect(clickAction)
    return cal

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        
        calFrom = createCalendar(self, self.showDate)
        calTo = createCalendar(self, self.showDateTwo)

        titleFromLbl = QLabel(self)
        titleFromLbl.setText("Select a from date: ")
        titleToLbl = QLabel(self)
        titleToLbl.setText("Select a to date: ")
        titleFromLbl.setMaximumHeight(20)
        titleToLbl.setMaximumHeight(20)

        layout.addWidget(titleFromLbl, 0, 0)
        layout.addWidget(calFrom, 1, 0)
        
        layout.addWidget(titleToLbl, 0, 1)
        layout.addWidget(calTo, 1, 1)

        self.lbl = QLabel(self)
        self.lblTwo = QLabel(self)

        self.lbl.setAlignment(Qt.AlignTop)
        self.lblTwo.setAlignment(Qt.AlignTop)

        date = calFrom.selectedDate()
        dateTwo = calTo.selectedDate()

        self.lbl.setText("Selected from date: " + date.toString())
        self.lblTwo.setText("Selected to date: " + dateTwo.toString())

        layout.addWidget(self.lbl, 2, 0)
        layout.addWidget(self.lblTwo, 2, 1)

        lineEditLayout = QVBoxLayout()
        lineEditLayout.setContentsMargins(0,0,0,0)
        lineEditLayout.setSpacing(5)

        tickerLbl = QLabel(self)
        tickerLbl.setMaximumHeight(20)
        tickerLineEdit = QLineEdit(self)
        tickerLineEdit.setMaximumHeight(20)
        tickerLineEdit.setAlignment(Qt.AlignTop)
        tickerLbl.setText("Enter ticker symbol: ")
        tickerLbl.setAlignment(Qt.AlignTop)
        datasetLbl = QLabel(self)
        datasetLbl.setMaximumHeight(20)
        datasetLbl.setText("Enter the Quandl Dataset Code: ")
        datasetLbl.setAlignment(Qt.AlignTop)

        getDataBtn = QPushButton(self)
        getDataBtn.setText("Download CSV Data")

        quandlLineEdit = QLineEdit(self)
        quandlLineEdit.setMaximumHeight(20)
        quandlLineEdit.setAlignment(Qt.AlignTop)

        lineEditLayout.addWidget(tickerLbl, 0, Qt.AlignTop)
        lineEditLayout.addWidget(tickerLineEdit, 0, Qt.AlignTop)
        lineEditLayout.addWidget(datasetLbl)
        lineEditLayout.addWidget(quandlLineEdit)
        lineEditLayout.addWidget(getDataBtn)

        layout.addLayout(lineEditLayout, 3, 0)


        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(10)
        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Equities data')

    def showDate(self, date): 
        self.lbl.setText("Selected from date: " + date.toString())
    def showDateTwo(self, date):
        self.lblTwo.setText("Selected to date: " + date.toString())
        
        
if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)