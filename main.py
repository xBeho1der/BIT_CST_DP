from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
import sys
from typing import List
from math import pi


class ScientificCalculator:
    def __init__(self):
        """define the related variable
        """
        self.result = None
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '!': 4
        }
        self.sign = ['+', '-', '*', '/', '^', '(', ')', '!', 'sin', 'cos']

    def expression_pretreatment(self, expression: str) -> List:
        """pretreat the input infix expression, dealing with "-" and "." in the expression.

        Args:
            expression (str): the infix expression

        Returns:
            List: a list follow the infix order after pretreatment
        """
        expression_opt = ""
        for i in range(len(expression)):
            if expression[i] == " ":
                continue
            elif expression[i] == '-':
                if i == 0 or expression[i-1] == '(':
                    expression_opt += "0"
                expression_opt += " "
                expression_opt += expression[i]
                expression_opt += " "
            elif expression[i] in self.sign:
                expression_opt += " "
                expression_opt += expression[i]
                expression_opt += " "
            else:
                expression_opt += expression[i]

        expression_list = []
        for item in expression_opt.split(" "):
            if item != "":
                expression_list.append(item)
        print(expression_list)
        return expression_list

    def postfix(self, expression_list: List) -> List:
        """transform the infix expression to the postfix expression

        Args:
            expression_list (List): a list follow the infix order after pretreatment

        Returns:
            List: return a list follow the postfix order
        """
        stack = []
        postfix = []

        for item in expression_list:
            if item == '(':
                stack.append('(')
            elif item == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
            elif item in self.precedence.keys():
                while stack and stack[-1] != '(' and self.precedence.get(stack[-1], 0) >= self.precedence.get(item):
                    postfix.append(stack.pop())
                stack.append(item)
            else:
                postfix.append(item)

        while stack:
            postfix.append(stack.pop())
        return postfix

    def _fabs(self, value1: float) -> float:
        return value1*(-1.0) if value1 < 0 else value1

    def _add(self, value1: float, value2: float) -> float:
        return value1+value2

    def _sub(self, value1: float, value2: float) -> float:
        return value2-value1

    def _mul(self, value1: float, value2: float) -> float:
        return value1*value2

    def _div(self, value1: float, value2: float) -> float:
        return value2/value1

    def _sqr(self, value1: float) -> float:
        return value1*value1

    def _sqrt(self, value1: float) -> float:
        # TODO
        return value1**0.5

    def _cube(self, value1: float) -> float:
        return value1*value1*value1

    def _cubert(self, value1: float) -> float:
        # TODO
        return value1**(1.0/3.0)

    def _pow(self, value1: float, value2: float) -> float:
        # TODO
        return value2**value1

    def _factorial(self, value1: int) -> int:
        """_summary_

        Args:
            value1 (int): number

        Returns:
            int: the factorial of calculation
        """
        if value1 == 0:
            return 1
        else:
            return value1 * self._factorial(value1 - 1)

    def _radian(self, value1: float) -> float:
        """convert the number into the radian

        Args:
            value1 (float): number

        Returns:
            float: the radian expression
        """
        return value1*pi/180

    def _sin(self, value1: float, mode=0) -> float:
        """sin

        Args:
            value1 (float): the input number
            mode (int, optional): the input in radian or num. Defaults to 0, which stands for radian.

        Returns:
            float: the calculation result, round to the nearest 1e-10
        """
        if mode == 1:
            value1 = self._radian(value1)
        iteration, temp_r, temp_l = 1, value1, 0
        while self._fabs(temp_r) >= 1e-15:
            temp_l += temp_r
            iteration += 2
            temp_r *= -value1**2/(iteration*(iteration-1))
        return round(temp_l, 10)

    def _cos(self, value1: float, mode=0) -> float:
        """cos

        Args:
            value1 (float): the input number
            mode (int, optional): the input in radian or num. Defaults to 0, which stands for nums.

        Returns:
            float: the calculation result, round to the nearest 1e-10
        """
        if mode == 1:
            value1 = self._radian(value1)
        iteration, temp_r, temp_l = 0, 1, 0
        while self._fabs(temp_r) >= 1e-15:
            temp_l += temp_r
            iteration += 2
            temp_r *= -value1**2/(iteration*(iteration-1))
        return round(temp_l, 10)

    def _exp(self, value1: float) -> float:
        """exp

        Args:
            value1 (float): the input number

        Returns:
            float: the calculation result, round to the nearest 1e-10
        """
        iteration, temp_r, temp_l = 0, 1, 0
        while self._fabs(temp_r) >= 1e-15:
            temp_l += temp_r
            iteration += 1
            temp_r *= value1/(iteration)
        return round(temp_l, 10)

    def calculate_postfix(self, postfix: List) -> float:
        """calculate the result of a postfix list

        Args:
            postfix (List): a list follow the postfix order

        Returns:
            float: the calculation result
        """
        print(postfix)

        stack_cal = []

        calculate_function = {
            '+': self._add,
            '-': self._sub,
            '*': self._mul,
            '/': self._div,
            '^': self._pow,
            '!': self._factorial
        }

        for item in postfix:
            if item in self.precedence.keys():
                value1 = float(stack_cal.pop())
                if item not in ['!']:
                    value2 = float(stack_cal.pop())
                    result = calculate_function[item](value1, value2)
                else:
                    result = calculate_function[item](value1)
                stack_cal.append(result)
            else:
                stack_cal.append(item)

        return stack_cal.pop()


def add_superscript(text):
    superscript_mapping = str.maketrans(
        "0123456789+-=()abcdefghijklmnopqrstuvwxyzAB",
        "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ½⅓"
    )
    return text.translate(superscript_mapping)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Scientific Calculator')

        self.line_edit = QLineEdit(self)
        self.line_edit.setReadOnly(True)

        self.buttons = [
            '7',  '8', '9', '/',
            '4',  '5', '6', '*',
            '1',  '2', '3', '-',
            '0',  '.', '=', '+',
            '!',  'sin', 'cos',
            "e"+add_superscript("x"),
            'x'+add_superscript("2"),
            'x'+add_superscript("A"),
            'x'+add_superscript("3"),
            'x'+add_superscript("B")
        ]

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        
        button_style = '''
        QPushButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            font-size: 18px;
            height: 40px;
        }

        QPushButton:hover {
            background-color: #45a049;
        }
        '''
        
        for button_text in self.buttons:
            button = QPushButton(button_text)
            button.setStyleSheet(button_style)
            button.clicked.connect(self.button_clicked)
            layout.addWidget(button)

        layout = QGridLayout()
        layout.addWidget(self.line_edit, 0, 0, 1, 4)

        row = 1
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
        # 获取点击的按钮
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                infix_expression = self.line_edit.text()
                cal = ScientificCalculator()
                res = cal.calculate_postfix(cal.postfix(cal.expression_pretreatment(infix_expression)))
                self.line_edit.setText(str(res))
            except:
                self.line_edit.setText('Error')
        else:
            self.line_edit.setText(self.line_edit.text() + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":
#     cal = ScientificCalculator()
#     while True:
#         infix = input("Enter your calculate expression:\n")
#         try:
#             print(
#                 f"Your result is {cal.calculate_postfix(cal.postfix(cal.expression_pretreatment(infix)))}\n"
#             )
#         except:
#             print("ERROR\nEnter again!\n")
