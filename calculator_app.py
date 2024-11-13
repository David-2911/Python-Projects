import sys
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")

        # Create a label to display the result
        self.display = QLabel()
        self.display.setText("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Create number buttons and store those buttons inside an array
        self.buttons = [QPushButton(str(i)) for i in range(10)]

        # Create the operator buttons
        self.operators = ["+", "-", "*", "/"]
        self.operator_buttons = [QPushButton(op) for op in self.operators]

        # Create clear and equals button
        self.equals_button = QPushButton("=")
        self.equals_button.clicked.connect(self.calculate)
        self.clear_button = QPushButton("C")
        self.clear_button.clicked.connect(self.clear)

        # Create a layout and add it to the window
        layout = QGridLayout()

        # Add the display widget to the layout
        layout.addWidget(self.display, 0, 0, 1, 4)

        # Adding the number buttons to the layout
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            layout.addWidget(button, row + 1, col)
            button.clicked.connect(self.number_button_clicked)

        # Adding operator buttons
        for i, op_button in enumerate(self.operator_buttons):
            layout.addWidget(op_button, i + 1, 3)
            op_button.clicked.connect(self.operator_button_clicked)

        # Add = and C button
        layout.addWidget(self.clear_button, 4, 2)
        layout.addWidget(self.equals_button, 4, 1)

        self.setLayout(layout)

        # Create three variables, current input, previous input and current operator
        self.current_input = "0"
        self.current_operator = ""
        self.previous_input = ""

    def number_button_clicked(self):
        digit = self.sender().text()
        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        self.display.setText(self.current_input)

    def operator_button_clicked(self):
        operator = self.sender().text()
        if self.current_operator == "":
            self.previous_input = self.current_input
            self.current_input = "0"
            self.current_operator = operator
        else:
            self.calculate()
            self.previous_input = self.current_input
            self.current_operator = operator
            self.current_input = "0"

    def calculate(self):
        if self.current_operator == "+":
            result = str(float(self.previous_input) + float(self.current_input))
        elif self.current_operator == "-":
            result = str(float(self.previous_input) - float(self.current_input))
        elif self.current_operator == "*":
            result = str(float(self.previous_input) * float(self.current_input))
        elif self.current_operator == "/":
            if self.current_input == "0":
                result = "Error"
            else:
                result = str(float(self.previous_input) / float(self.current_input))
        else:
            result = self.current_input
        self.display.setText(result)
        self.current_input = result
        self.current_operator = ""

    def clear(self):
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""
        self.display.setText("0")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
