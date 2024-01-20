import sys
from PyQt5.QtWidgets import QApplication
from mywindow import create_and_show_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    create_and_show_window()
    sys.exit(app.exec_())

