# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QTimer, Slot
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

        # Don't show the percentage completion on the progress bar.
        # It distracts from what's important.
        self.ui.progressBar.setTextVisible(False)

        self.timer = QTimer(self)

        # Defines a one minute stretch break.
        self.break_duration_seconds = 60

        # Give the user a 3 second head start.  57 seconds of good stretching
        # motivated by a head start AKA a little bit of cheating is better than
        # 60 seconds of half-hearted stretching.  Note that a similarly
        # important value, used to the same effect, is also defined in the GUI
        # design code.
        self.break_time_elapsed_seconds = 3

        # Do not confuse the stretch break duration/timer with the QTimer.
        # The QTimer a class in the framework that's used for ticking and can
        # raise an event ("signal") each tick, with configurable tick duration.
        # The stretch break duration/time elapsed track the actual time of the
        # stretch break and are nothing to do with signals and slots/events and
        # handlers.

        # We want the progress bar updated once every 1000ms.
        # We need the event (1000ms timeout elapsing) to be handled by the
        # method we're passing to connect() here.
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_progress_bar)

    @Slot()
    def update_progress_bar(self):
        if self.break_time_elapsed_seconds >= self.break_duration_seconds:
            exit()
        else:
            proportion_elapsed = int(
                self.break_time_elapsed_seconds
                / self.break_duration_seconds * 100)
            self.ui.progressBar.setValue(proportion_elapsed)
            self.break_time_elapsed_seconds += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
