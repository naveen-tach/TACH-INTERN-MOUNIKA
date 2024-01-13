import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

class MyCentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Add an image to the central widget
        label = QLabel(self)
        pixmap = QPixmap('/home/pi/Downloads/dorabujji_files/3a3e2c283edbd8befb8e55adb7521c25.jpg')  # Using PyQt5 default logo
        label.setPixmap(pixmap)
        layout.addWidget(label)

        # Add three buttons to the central widget
        self.add_buttons(layout)

    def add_buttons(self, layout):
        button1 = QPushButton('Button 1', self)
        layout.addWidget(button1)

        button2 = QPushButton('Button 2', self)
        layout.addWidget(button2)

        button3 = QPushButton('Button 3', self)
        layout.addWidget(button3)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Window")
        self.setGeometry(100, 100, 400, 300)  # x, y, width, height

        # Set the central widget to the custom widget
        central_widget = MyCentralWidget()
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
