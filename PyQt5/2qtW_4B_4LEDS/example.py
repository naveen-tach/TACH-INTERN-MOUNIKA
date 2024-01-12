import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QMessageBox
from PyQt5.QtCore import QTimer
import RPi.GPIO as GPIO

class LedControlWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LED Control")
        self.setGeometry(200, 200, 400, 200)

        # Set up GPIO
        GPIO.setmode(GPIO.BOARD)
        self.led_pins = [11,13, 15, 27]  # Modify these pin numbers according to your setup

        self.init_ui_led_control()

    def init_ui_led_control(self):
        layout = QVBoxLayout(self)

        # Create LED buttons
        led1_button = QPushButton("LED 1")

        led2_button = QPushButton("LED 2")
        led3_button = QPushButton("LED 3")
        led4_button = QPushButton("LED 4")

        # Connect the button's clicked signals to their respective functions
        led1_button.clicked.connect(lambda: self.control_led(1))
        led2_button.clicked.connect(lambda: self.control_led(2))
        led3_button.clicked.connect(lambda: self.control_led(3))
        led4_button.clicked.connect(lambda: self.control_led(4))

        # Add LED buttons to the layout
        layout.addWidget(led1_button)
        layout.addWidget(led2_button)
        layout.addWidget(led3_button)
        layout.addWidget(led4_button)

        # Set layout for the LED control window
        self.setLayout(layout)

    def control_led(self, led_number):
        # Function to handle LED control
        self.toggle_led(led_number)

    def toggle_led(self, led_number):
        # Toggle the state of the specified LED
        pin = self.led_pins[led_number - 1]
        GPIO.setup(pin, GPIO.OUT)
        state = not GPIO.input(pin)
        GPIO.output(pin, state)

class MultiTitleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("welcome")
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Create labels with titles
        title1_label = QLabel("tachyon automations")  # Modified title
        

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.show_led_control_window)

        self.led_control_window = LedControlWindow()

        layout.addWidget(title1_label)
        
        layout.addWidget(login_button)

        self.setLayout(layout)

    def show_led_control_window(self):
        # Function to show the LED control window
        self.led_control_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultiTitleWindow()
    window.show()
    sys.exit(app.exec_())

