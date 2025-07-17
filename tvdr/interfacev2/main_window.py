import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from .main_layout import MainLayout


class MainWindows:
    def __init__(self):
        self.app = QApplication([])
        QApplication.setStyle("Fusion")

        self.current_layout = QHBoxLayout()
        self.current_layout.addWidget(MainLayout())
        self.widget = QWidget()
        self.widget.setWindowTitle("TVDR : Traffic Violation Detection and Recognition")
        self.widget.setLayout(self.current_layout)
        self.widget.show()

        sys.exit(self.app.exec_())
