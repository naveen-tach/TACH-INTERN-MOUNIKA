import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtCore import QRegExp

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tachyon Automations")
        self.setGeometry(100, 100, 300, 200)

        self.setup_ui()

    def setup_ui(self):
        self.setup_image_label()
        self.setup_username_field()
        self.setup_password_field()
        self.setup_login_button()

    def setup_image_label(self):
        pixmap = QPixmap("/home/pi/Downloads/TOM")
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0, 0, 9000, 700)

    def setup_username_field(self):
        self.text_field1 = QLineEdit(self)
        self.text_field1.setGeometry(50, 50, 150, 30)
        self.text_field1.setPlaceholderText("Username")
        self.setup_validator(self.text_field1, "[a-zA-Z]+")

    def setup_password_field(self):
        self.text_field2 = QLineEdit(self)
        self.text_field2.setGeometry(50, 100, 150, 30)
        self.text_field2.setPlaceholderText("Password")
        self.text_field2.setEchoMode(QLineEdit.Password)
        self.setup_validator(self.text_field2, "[a-zA-Z0-9]+")

    def setup_validator(self, line_edit, regex_pattern):
        regex = QRegExp(regex_pattern)
        validator = QRegExpValidator(regex)
        line_edit.setValidator(validator)

    def setup_login_button(self):
        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(50, 150, 100, 30)
        self.login_button.clicked.connect(self.on_login)

    def on_login(self):
        username = self.text_field1.text()
        password = self.text_field2.text()
        print("Username:", username)
        print("Password:", password)

def create_and_show_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

