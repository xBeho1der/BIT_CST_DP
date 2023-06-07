from gui import Calculator
import sys
from PyQt5.QtWidgets import QApplication
import argparse
from ScientificCalculator import ScientificCalculator
from prettytable import PrettyTable
from math import pi, e, sin, cos

def demonstrator() -> None:
    equation = [
        "1+1 =",
        "2.4+5.6 =",
        "5*6 =",
        "2.5 + 3.7 =",
        "10.3 - 4.2 =",
        "4.6 * 2.2 =",
        "15.8 / 3.2 =",
        "2.4 ^ 1.5 =",
        "e =",
        "sin(0.7) =",
        "cos(1.2) =",
        "8.9 + 0.3 =",
        "7.2 - 1.5 =",
        "5.4 * 0.8 =",
        "12.7 / 2.5 =",
        "3.3 ^ 0.6 =",
        "e =",
        "sin(0.9) =",
        "cos(0.4) =",
        "9.6 + 1.1 =",
        "15.2 - 2.8 =",
        "6.7 * 1.3 =",
        "18.5 / 2.2 =",
        "4.2 ^ 0.9 =",
        "e =",
        "sin(0.3) =",
        "cos(0.8) =",
        "3.5 + 9.4 =",
        "20.1 - 10.5 =",
        "7.9 * 5.6 =",
        "36.4 / 6.7 =",
        "2.6 ^ 1.7 =",
        "e =",
        "sin(1.2) =",
        "cos(0.6) =",
        "12.4 + 4.6 =",
        "8.8 - 2.2 =",
        "9.3 * 7.5 =",
        "30.7 / 5.2 =",
        "5.8 ^ 2.3 =",
        "e =",
        "sin(1.6) =",
        "cos(1.9) =",
        "15.7 + 8.9 =",
        "25.2 - 12.6 =",
        "6.4 * 9.2 =",
        "48.1 / 8.3 =",
        "1.9 ^ 3.1 =",
        "e =",
        "sin(2.3) =",
        "cos(2.6) =",
        "8.1 + 3.2 =",
        "4.5 - 1.8 =",
        "3.6 * 2.5 =",
        "9.7 / 3.8 =",
        "2.1 ^ 0.7 =",
        "e =",
        "sin(2.8) =",
        "cos(3.1) =",
        "5.9 + 2.4 =",
        "7.2 - 0.9 =",
        "4.3 * 1.7 =",
        "10.5 / 2.3 =",
        "1.4 ^ 0.5 =",
        "e =",
        "sin(3.4) =",
        "cos(3.7) =",
        "9.2 + 1.3 =",
        "6.6 - 1.1 =",
        "7.8 * 0.9 =",
        "12.6 / 3.1 =",
        "2.5 ^ 1.2 =",
        "e =",
        "sin(4.1) =",
    ]
    table = PrettyTable(['No.', 'equation', 'output', 'expectation', 'result'])
    count = 0
    for item in equation:
        count += 1
        expect = eval(item[:-1].replace("^",'**'))
        cal = ScientificCalculator()
        test = cal.calculate_postfix(cal.postfix(
            cal.expression_pretreatment(item[:-1])))
        result = test == expect
        table.add_row([count, item, test, expect, result])
    print(table)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""
        The mode of Calculator\n
        e.g python run_calculator.py --defects 1
                                     """)
    parser.add_argument("--defects", "-d",
                        metavar="", type=str, default="0", help="run the calculator with defects or not")
    args = parser.parse_args()
    defects = eval(args.defects)
    demonstrator()
    app = QApplication(sys.argv)
    calculator = Calculator(defects)
    calculator.show()
    sys.exit(app.exec_())
