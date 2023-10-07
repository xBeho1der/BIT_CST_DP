from typing import List
from math import pi, e, sin, cos, exp
from numpy import deg2rad

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

    def calculate(self, value1: float, value2: float) -> float:
        pass
    
    def sin(self, value1: float) -> float:
        pass
    
    def cos(self, value1: float) -> float:
        pass
    
    def exp(self, value1: float) -> float:
        pass

    def _radian(self, value1: float) -> float:
        """convert the number into the radian

        Args:
            value1 (float): number

        Returns:
            float: the radian expression
        """
        return deg2rad(value1)

    def calculate_postfix(self, postfix: List) -> float:
        """calculate the result of a postfix list

        Args:
            postfix (List): a list follow the postfix order

        Returns:
            float: the calculation result
        """

        stack_cal = []

        calculate_strategy = {
            '+': AdditionStrategy(),
            '-': SubtractionStrategy(),
            '*': MultiplicationStrategy(),
            '/': DivisionStrategy(),
            '^': PowerStrategy(),
            '!': FactorialStrategy(),
            'sin': MathTrigonometryAdapter(),
            'cos': MathTrigonometryAdapter(),
            'exp': MathTrigonometryAdapter(),
        }
        for item in postfix:
            if item in self.precedence.keys():
                value1 = float(stack_cal.pop())
                if item not in ['!', 'sin', 'cos']:
                    value2 = float(stack_cal.pop())
                    result = calculate_strategy[item].calculate(value1, value2)
                elif item == '!':
                    result = calculate_strategy[item].calculate(value1)
                elif item in ['sin', 'cos']:
                    result = getattr(calculate_strategy[item], item)(value1)
                stack_cal.append(result)
            else:
                stack_cal.append(item)

        return stack_cal.pop()

class AdditionStrategy(ScientificCalculator):
    def calculate(self, value1: float, value2: float) -> float:
        return value1 + value2

class SubtractionStrategy(ScientificCalculator):
    def calculate(self, value1: float, value2: float) -> float:
        return value2 - value1

class MultiplicationStrategy(ScientificCalculator):
    def calculate(self, value1: float, value2: float) -> float:
        return value1 * value2

class DivisionStrategy(ScientificCalculator):
    def calculate(self, value1: float, value2: float) -> float:
        return value2 / value1

class PowerStrategy(ScientificCalculator):
    def calculate(self, value1: float, value2: float) -> float:
        return value2 ** value1

class FactorialStrategy(ScientificCalculator):
    def calculate(self, value1: float) -> float:
        if value1 == 0:
            return 1
        else:
            return value1 * self.calculate(value1 - 1)
        
class MathTrigonometryAdapter(ScientificCalculator):
    def sin(self, value1: float) -> float:
        return sin(value1)

    def cos(self, value1: float) -> float:
        return cos(value1)

    def exp(self, value1: float) -> float:
        return exp(value1)