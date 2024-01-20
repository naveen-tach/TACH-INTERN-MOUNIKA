import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Tachyon Automations')

        # Create QLabel widget for the image
        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 1900, 900)  # Adjust the size as needed

        # Create three QPushButton widgets
       # button1 = QPushButton('Button 1', self)
       # button1.setGeometry(10, 220, 80, 30)
       # button1.clicked.connect(self.logo_page)

       # button2 = QPushButton('Button 2', self)
       # button2.setGeometry(100, 220, 80, 30)
        # Connect button2 to another function if needed

        #button3 = QPushButton('Button 3', self)
       # button3.setGeometry(190, 220, 80, 30)
        # Connect button3 to another function if needed
# Call logo_page function to display the image
        self.logo_page()


        self.show()

    def logo_page(self):
        # Load and display the image when the function is called
        pixmap = QPixmap('/home/pi/Downloads/TOM')  # Replace with the actual path to your image
        self.label.setPixmap(pixmap)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())

