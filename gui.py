from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QHeaderView
import sys
from ScientificCalculator import ScientificCalculator
from math import pi, e


def add_superscript(text):
    superscript_mapping = str.maketrans(
        "0123456789+-=()abcdefghijklmnopqrstuvwxyzAB",
        "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ½⅓"
    )
    return text.translate(superscript_mapping)


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(960, 700)
        self.setWindowTitle('Scientific Calculator')

        self.special_sign = [
            "e"+add_superscript("x"),
            'x'+add_superscript("2"),
            'x'+add_superscript("A"),
            'x'+add_superscript("3"),
            'x'+add_superscript("B"),
            'x'+add_superscript("y"),
            'RAD', 'sin', 'cos'
        ]

        self.line_edit = QLineEdit(self)
        self.line_edit.setReadOnly(True)

        self.buttons = [
            'C',  'RAD', '!',  'Backspace',
            '7',  '8',   '9',  '/',
            '4',  '5',   '6',  '*',
            '1',  '2',   '3',  '-',
            '0',  '.',   '=',  '+',
            '(', ')',  'sin', 'cos',
            'e'+add_superscript("x"),
            'x'+add_superscript("2"),
            'x'+add_superscript("A"),
            'x'+add_superscript("3"),
            'x'+add_superscript("B"),
            'x'+add_superscript("y"), "e", "Pi"
        ]

        # layout = QVBoxLayout()
        layout = QGridLayout()
        self.line_edit.setFixedHeight(150)
        font = QFont("Arial", 32)
        self.line_edit.setFont(font)
        layout.addWidget(self.line_edit)
        button_style = '''
        QPushButton {
            background-color: #D3D3D3;
            border: none;
            color: black;
            font: Arial;
            font-size: 36px;
            height: 100;
            width: 180;
            border-style: outset;
            border: 2px solid #778899
        }

        QPushButton:hover {
            background-color: #45a049;
        }        
        '''
        for button_text in self.buttons:
            button = QPushButton(button_text)
            button.setStyleSheet(button_style)
            # button.setStyleSheet()
            button.clicked.connect(self.button_clicked)
            layout.addWidget(button)

        layout = QGridLayout()
        layout.addWidget(self.line_edit, 0, 0, 2, 4)

        row = 3
        col = 0
        for button_text in self.buttons:
            button = QPushButton(button_text)
            button.setStyleSheet(button_style)
            button.clicked.connect(self.button_clicked)
            layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.setLayout(layout)


    def button_clicked(self):

        if self.line_edit.text() == 'Error':
            self.line_edit.clear()

        button = self.sender()
        text = button.text()
        if text == '=':
            try:
                infix_expression = self.line_edit.text()
                cal = ScientificCalculator()
                res = cal.calculate_postfix(cal.postfix(
                    cal.expression_pretreatment(infix_expression)))
                self.line_edit.setText(str(res))
            except:
                self.line_edit.setText('Error')
        elif text == 'Pi':
            self.line_edit.setText(str(pi))
        elif text == 'e':
            self.line_edit.setText(str(e))
        elif text == 'C':
            self.line_edit.clear()
        elif text == 'Backspace':
            self.line_edit.backspace()
        else:
            if text not in self.special_sign:
                self.line_edit.setText(self.line_edit.text() + text)
            else:
                # if text == "e"+add_superscript("x"):
                # str_tmp = self.line_edit.text()+
                # self.line_edit.setText
                if text == 'x'+add_superscript("2"):
                    str_tmp = self.line_edit.text()
                    # 前一位是右括号并且有匹配时计算括号内计算式结果的平方
                    # 是阶乘则先计算阶乘
                    # 否则计算前一位的平方，平方优先级高！！！
                    list_temp = ScientificCalculator().expression_pretreatment(expression=str_tmp)
                    
                    for item in list_temp:
                        
                    print(a)
                    self.line_edit.setText(str_tmp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
