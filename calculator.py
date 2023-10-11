import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("calculator.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")

        # 변수 초기화
        self.result = 0
        self.elementary = ['+', '-', '*', '/', "."]

        # 버튼 초기화
        self.btn_0.clicked.connect(self.input_value)
        self.btn_1.clicked.connect(self.input_value)
        self.btn_2.clicked.connect(self.input_value)
        self.btn_3.clicked.connect(self.input_value)
        self.btn_4.clicked.connect(self.input_value)
        self.btn_5.clicked.connect(self.input_value)
        self.btn_6.clicked.connect(self.input_value)
        self.btn_7.clicked.connect(self.input_value)
        self.btn_8.clicked.connect(self.input_value)
        self.btn_9.clicked.connect(self.input_value)

        self.btn_ac.clicked.connect(self.resulted)
        self.btn_equal.clicked.connect(self.resulted)

        self.btn_dot.clicked.connect(self.calculating)
        self.btn_div.clicked.connect(self.calculating)
        self.btn_minus.clicked.connect(self.calculating)
        self.btn_multi.clicked.connect(self.calculating)
        self.btn_plus.clicked.connect(self.calculating)

        self.btn_opposite.clicked.connect(self.func)
        self.btn_div_100.clicked.connect(self.func)

        self.label.setText(str(self.result))

        # 현재 입력중인 값을 저장
        self.current_input = ""
        # 입력한 계산식 저장
        self.cal_text = ""

    def input_value(self):
        input = self.sender()
        
        if input == self.btn_0:
            self.current_input += "0"
        elif input == self.btn_1:
            self.current_input += "1"
        elif input == self.btn_2:
            self.current_input += "2"
        elif input == self.btn_3:
            self.current_input += "3"
        elif input == self.btn_4:
            self.current_input += "4"
        elif input == self.btn_5:
            self.current_input += "5"
        elif input == self.btn_6:
            self.current_input += "6"
        elif input == self.btn_7:
            self.current_input += "7"
        elif input == self.btn_8:
            self.current_input += "8"
        elif input == self.btn_9:
            self.current_input += "9"
        else:
            pass

        self.label.setText(self.current_input)

    def calculating(self):
        cal = self.sender()

        if self.current_input == "":
            if cal == self.btn_plus:
                self.current_input += "+"
            elif cal == self.btn_minus:
                self.current_input += "-"
            elif cal == self.btn_multi:
                self.current_input += "*"
            elif cal == self.btn_div:
                self.current_input += "/"
            elif cal == self.btn_dot:
                self.current_input += "."
        else:
            if self.current_input[-1] in self.elementary:
                pass
            else:
                if cal == self.btn_plus:
                    self.current_input += "+"
                elif cal == self.btn_minus:
                    self.current_input += "-"
                elif cal == self.btn_multi:
                    self.current_input += "*"
                elif cal == self.btn_div:
                    self.current_input += "/"
                elif cal == self.btn_dot:
                    self.current_input += "."
        self.label.setText(self.current_input)        

    def resulted(self):
        res = self.sender()
        
        print("current_input", self.current_input)
        print("cal_text", self.cal_text)

        if res == self.btn_equal:
            try:
                if self.cal_text == "" and self.current_input != "":
                    self.cal_text = self.current_input
                    self.result = eval(self.cal_text)
                    self.current_input = ""
                    self.cal_text = ""
                    self.cal_text = str(self.result)
                elif self.cal_text != "" and self.current_input != "":
                    if self.current_input[0] in self.elementary:
                        if self.current_input[0] == ".":
                            self.cal_text = ""
                            self.cal_text = self.current_input
                            self.result = eval(self.cal_text)
                            self.current_input = ""
                        else:
                            self.cal_text += self.current_input
                            self.result = eval(self.cal_text)
                            self.current_input = ""
                            self.cal_text = ""
                            self.cal_text = str(self.result)
                    else:
                        self.cal_text = ""
                        self.cal_text = self.current_input
                        self.result = eval(self.cal_text)
                        self.current_input = ""
                else:
                    pass
                self.label.setText(str(self.result))                
            except ZeroDivisionError:
                self.label.setText("Error : Division by zero")
                self.current_input = ""
                self.cal_text = ""
            except Exception as e:
                self.label.setText("Error")
                self.current_input = ""
                self.cal_text = ""
        elif res == self.btn_ac:
            self.current_input = ""
            self.cal_text = ""
            self.result = 0
            self.label.setText(str(self.result))
        else:
            self.label.setText("resulted error")

    def func(self):
        func = self.sender()

        if func == self.btn_div_100:
            if self.current_input == "":
                pass
            else:
                if self.current_input[-1] in self.elementary:
                    pass
                else:
                    value = eval(self.current_input)
                    result = value / 100
                    self.label.setText(str(result))
                    self.current_input = str(result)
        elif func == self.btn_opposite:
            if self.current_input == "":
                pass
            else:
                if self.current_input[-1] in self.elementary:
                    pass
                else:
                    value = eval(self.current_input)
                    result = -value
                    self.label.setText(str(result))
                    self.current_input = str(result)
        else:
            self.label.setText("function error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())