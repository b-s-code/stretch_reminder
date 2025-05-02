# This Python file uses the following encoding: utf-8
import sys
import time
from threading import Thread

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

def count_up(widget):
    seconds_left = 60
    while seconds_left > 0:
        seconds_left -= 1
        widget.ui.progressBar.setValue(int(seconds_left / 60 * 100))
        time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    counter_thread = Thread(target=count_up, args=[widget])
    counter_thread.run()
    sys.exit(app.exec())
