import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtCore import QRegExp

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tachyon Automations")
        self.setGeometry(100, 100, 300, 200)

        # Load an image using QPixmap
        pixmap = QPixmap("/home/pi/Downloads/TOM")

        # Create a QLabel and set the pixmap as its content
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0, 0, 9000, 700)  # Set the position and size of the image label

        # Create the first text field for the username
        self.text_field1 = QLineEdit(self)
        self.text_field1.setGeometry(50, 50, 150, 30)  # Set the position and size of the text field
        self.text_field1.setPlaceholderText("Username")
        regex = QRegExp("[a-zA-Z]+")
        validator = QRegExpValidator(regex)
        self.text_field1.setValidator(validator)

        # Create the second text field for the password
        self.text_field2 = QLineEdit(self)
        self.text_field2.setGeometry(50, 100, 150, 30)  # Set the position and size of the text field
        self.text_field2.setPlaceholderText("Password")
        regex = QRegExp("[a-zA-Z0-9]+")
        validator = QRegExpValidator(regex)
        self.text_field2.setValidator(validator)
        self.text_field2.setEchoMode(QLineEdit.Password)

        # Create a QPushButton for login
        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(50, 150, 100, 30)  # Set the position and size of the button
        self.login_button.clicked.connect(self.on_login)

    def on_login(self):
        # Add your logic here for handling the login button click
        username = self.text_field1.text()
        password = self.text_field2.text()
        print("Username:", username)
        print("Password:", password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


