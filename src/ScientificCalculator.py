from typing import List
from math import pi, e


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
            'sin': 3,
            'cos': 3,
            '!': 4,
        }
        self.sign = ['+', '-', '*', '/', '^', '(', ')', '!', 'sin', 'cos']

    def brackets_pare(self, expression_list: List) -> bool:
        """judge whether the brackets pare

        Args:
            expression_list (List): the original expression_list

        Returns:
            bool: result
        """
        return True if expression_list.count('(') == expression_list.count(')') else False

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
            if item == 'e':
                expression_list.append(str(e))
            elif item == 'pi':
                expression_list.append(str(pi))
            elif item != "":
                expression_list.append(item)
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
        """return the absolute value of value1

        Args:
            value1 (float): input number

        Returns:
            float: result
        """
        return value1*(-1.0) if value1 < 0 else value1

    def _add(self, value1: float, value2: float) -> float:
        """add

        Args:
            value1 (float): operate value1
            value2 (float): operate value2

        Returns:
            float: result
        """
        return value1+value2
    
    def _add_defects(self, value1: float, value2: float) -> float:
        """add

        Args:
            value1 (float): operate value1
            value2 (float): operate value2

        Returns:
            float: result
        """
        return value1+value1

    def _sub(self, value1: float, value2: float) -> float:
        """subtraction

        Args:
            value1 (float): operate value1
            value2 (float): operate value2

        Returns:
            float: result
        """
        return value2-value1

    def _mul(self, value1: float, value2: float) -> float:
        """multiplication

        Args:
            value1 (float): operate value1
            value2 (float): operate value2

        Returns:
            float: result
        """
        return value1*value2

    def _div(self, value1: float, value2: float) -> float:
        """division

        Args:
            value1 (float): operate value1
            value2 (float): operate value2

        Returns:
            float: result
        """
        return value2/value1

    def _pow(self, value1: float, value2: float) -> float:
        """power

        Args:
            value1 (float): base
            value2 (float): power

        Returns:
            float: result
        """
        return value2**value1

    def _factorial(self, value1: int) -> int:
        """return the factorial of value1

        Args:
            value1 (float): input number

        Returns:
            float: the factorial of value1
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

    def _sin(self, value1: float) -> float:
        """sin

        Args:
            value1 (float): the input number

        Returns:
            float: the calculation result, round to the nearest 1e-10
        """
        iteration, temp_r, temp_l = 1, value1, 0
        while self._fabs(temp_r) >= 1e-15:
            temp_l += temp_r
            iteration += 2
            temp_r *= -value1**2/(iteration*(iteration-1))
        return round(temp_l, 10)

    def _cos(self, value1: float) -> float:
        """cos

        Args:
            value1 (float): the input number

        Returns:
            float: the calculation result, round to the nearest 1e-10
        """
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

        stack_cal = []

        calculate_function = {
            '+': self._add,
            '-': self._sub,
            '*': self._mul,
            '/': self._div,
            '^': self._pow,
            '!': self._factorial,
            'sin': self._sin,
            'cos': self._cos,
            'exp': self._exp,
        }
        for item in postfix:
            if item in self.precedence.keys():
                value1 = float(stack_cal.pop())
                if item not in ['!', 'sin', 'cos']:
                    value2 = float(stack_cal.pop())
                    result = calculate_function[item](value1, value2)
                else:
                    result = calculate_function[item](value1)
                stack_cal.append(result)
            else:
                stack_cal.append(item)

        return stack_cal.pop()

    def calculate_postfix_defects(self, postfix: List) -> float:
        """calculate the result of a postfix list

        Args:
            postfix (List): a list follow the postfix order

        Returns:
            float: the calculation result
        """

        stack_cal = []

        calculate_function = {
            '+': self._add_defects,
            '-': self._sub,
            '*': self._mul,
            '/': self._div,
            '^': self._pow,
            '!': self._factorial,
            'sin': self._sin,
            'cos': self._cos,
            'exp': self._exp,
        }
        for item in postfix:
            if item in self.precedence.keys():
                value1 = float(stack_cal.pop())
                if item not in ['!', 'sin', 'cos']:
                    value2 = float(stack_cal.pop())
                    result = calculate_function[item](value1, value2)
                else:
                    result = calculate_function[item](value1)
                stack_cal.append(result)
            else:
                stack_cal.append(item)

        return stack_cal.pop()