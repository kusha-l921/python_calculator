import sys
import requests
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel,
                            QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
       super().__init__()

       self.expression=""

       self.zero_button=QPushButton("0", self)
       self.one_button=QPushButton("1", self)
       self.two_button=QPushButton("2", self)
       self.three_button=QPushButton("3", self)
       self.four_button=QPushButton("4", self)
       self.five_button=QPushButton("5", self)
       self.six_button=QPushButton("6", self)
       self.seven_button=QPushButton("7", self)
       self.eight_button=QPushButton("8", self)
       self.nine_button=QPushButton("9", self)
       self.add_button=QPushButton("+", self)
       self.sub_button=QPushButton("-", self)
       self.multi_button=QPushButton("*", self)
       self.div_button=QPushButton("/", self)
       self.equal_button=QPushButton("=", self)
       self.decimal_button=QPushButton(".", self)
       self.ans_label=QLabel("0", self)
       self.clear_button=QPushButton("clear", self)

       self.initUI()

    def initUI(self):
        central_widget=QWidget()
        self.setWindowTitle("Calculator App")

        grid=QGridLayout()
        grid.addWidget(self.nine_button, 1,1)
        grid.addWidget(self.eight_button, 1,2)
        grid.addWidget(self.seven_button, 1,3)
        grid.addWidget(self.six_button, 2,1)
        grid.addWidget(self.five_button, 2,2)
        grid.addWidget(self.four_button, 2,3)
        grid.addWidget(self.three_button, 3,1)
        grid.addWidget(self.two_button, 3,2)
        grid.addWidget(self.one_button, 3,3)
        grid.addWidget(self.add_button, 1,5)
        grid.addWidget(self.sub_button, 2,5)
        grid.addWidget(self.multi_button, 3,5)
        grid.addWidget(self.div_button, 4,5)
        grid.addWidget(self.equal_button, 4,3)
        grid.addWidget(self.zero_button, 4,2)
        grid.addWidget(self.decimal_button, 4,1)
        grid.addWidget(self.clear_button, 5,5)
        self.setLayout(grid)

        self.ans_label.setObjectName("answer_label")

        self.ans_label.setStyleSheet("font-size:55px;"
                                    "font-weight: bold;"
                                    "font-family: DS-Digital;")
        grid.addWidget(self.ans_label, 0, 0, 1, 5)
        
        self.one_button.clicked.connect(lambda: self.append_expression("1"))
        self.two_button.clicked.connect(lambda: self.append_expression("2"))
        self.three_button.clicked.connect(lambda: self.append_expression("3"))
        self.four_button.clicked.connect(lambda: self.append_expression("4"))
        self.five_button.clicked.connect(lambda: self.append_expression("5"))
        self.six_button.clicked.connect(lambda: self.append_expression("6"))
        self.seven_button.clicked.connect(lambda: self.append_expression("7"))
        self.eight_button.clicked.connect(lambda: self.append_expression("8"))
        self.nine_button.clicked.connect(lambda: self.append_expression("9"))
        self.zero_button.clicked.connect(lambda: self.append_expression("0"))

        self.add_button.clicked.connect(lambda: self.append_expression("+"))
        self.sub_button.clicked.connect(lambda: self.append_expression("-"))
        self.multi_button.clicked.connect(lambda: self.append_expression("*"))
        self.div_button.clicked.connect(lambda: self.append_expression("/"))
        self.decimal_button.clicked.connect(lambda: self.append_expression("."))

        self.equal_button.clicked.connect(self.cal_result)
        self.clear_button.clicked.connect(self.clear_)

    def append_expression(self, value):
        if self.expression=="0":
            self.expression=value
        else:
            self.expression+=value
        self.update_display()

    def cal_result(self):
        try:
            result=eval(self.expression)
            self.expression=str(result)
        except Exception:
            self.expression="Error"
        self.update_display()

    def clear_(self):
        self.expression = "0"
        self.update_display()

    def update_display(self):
        self.ans_label.setText(self.expression)

 






if __name__=="__main__":
    app=QApplication(sys.argv)
    calci_app=Calculator()
    calci_app.show()
    sys.exit(app.exec_())
     
