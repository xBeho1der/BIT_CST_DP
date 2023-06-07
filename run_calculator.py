from gui import Calculator
import sys
from PyQt5.QtWidgets import QApplication
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""
        The mode of Calculator\n
        e.g python run_calculator.py --defects 1
                                     """)
    parser.add_argument("--defects", "-d",
                        metavar="", type=str, default="0", help="run the calculator with defects or not")
    args = parser.parse_args()
    defects = eval(args.defects)
    app = QApplication(sys.argv)
    calculator = Calculator(defects)
    calculator.show()
    sys.exit(app.exec_())
