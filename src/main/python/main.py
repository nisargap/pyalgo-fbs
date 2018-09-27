from fbs_runtime.application_context import ApplicationContext,  cached_property
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QVBoxLayout, QVBoxLayout, QCalendarWidget

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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        layout.addWidget(cal)
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        layout.addWidget(self.lbl)
        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
    def showDate(self, date): 
        self.lbl.setText(date.toString())
        
        
if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)