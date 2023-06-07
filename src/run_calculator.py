from gui import Calculator
import sys
from PyQt5.QtWidgets import QApplication
import argparse
from test_demonstrator import demonstrator



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""
        select running mode of Calculator
                                     """)
    parser.add_argument("--defects", "-d",
                        metavar="", type=str, default="0", help="run the calculator with defects or not")
    parser.add_argument("--tests", "-t",
                        metavar="", type=str, default="0", help="run the calculator with tests results or not")
    args = parser.parse_args()
    defects = eval(args.defects)
    tests = eval(args.tests)
    if tests:
        demonstrator()
    app = QApplication(sys.argv)
    calculator = Calculator(defects)
    calculator.show()
    sys.exit(app.exec_())
