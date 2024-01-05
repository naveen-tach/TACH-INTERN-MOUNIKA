import sys
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)  # Assuming the LED is connected to GPIO pin 17

        # Create a button
        button = QPushButton('Flash LED', self)
        button.clicked.connect(self.flash_led)

        # Create a layout and set it for the central widget
        layout = QVBoxLayout()
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set up the main window
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('LED Flasher')
        self.show()

    def flash_led(self):
        # Turn on the LED for a short duration
        GPIO.output(17, GPIO.HIGH)
        self.delay(1)  # Adjust the delay time as needed (in milliseconds)
        GPIO.output(17, GPIO.LOW)

    def delay(self, milliseconds):
        # This function is for creating a delay in milliseconds
        from PyQt5.QtCore import QEventLoop, QTimer

        loop = QEventLoop()
        QTimer.singleShot(milliseconds, loop.quit)
        loop.exec_()

    def closeEvent(self, event):
        # Cleanup GPIO when the application is closed
        GPIO.cleanup()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
