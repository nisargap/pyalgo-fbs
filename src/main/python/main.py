from fbs_runtime.application_context import ApplicationContext,  cached_property
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QCalendarWidget

import sys

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):
        stylesheet = self.get_resource('styles.qss')
        self.app.setStyleSheet(open(stylesheet).read())
        self.window.show()
        return self.app.exec_()
    @cached_property
    def window(self):
        return MainWindow()

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

        layout.addWidget(calFrom, 0, 0)
        layout.addWidget(calTo, 0, 1)

        self.lbl = QLabel(self)
        self.lblTwo = QLabel(self)

        date = calFrom.selectedDate()
        dateTwo = calTo.selectedDate()

        self.lbl.setText(date.toString())
        self.lblTwo.setText(dateTwo.toString())

        layout.addWidget(self.lbl, 1, 0)
        layout.addWidget(self.lblTwo, 1, 1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Equities data')
        self.show()

    def showDate(self, date): 
        self.lbl.setText(date.toString())
    def showDateTwo(self, date):
        self.lblTwo.setText(date.toString())
        
        
if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)