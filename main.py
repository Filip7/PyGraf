import sys
from PyQt6 import QtWidgets
from ui import MainWindow


app = QtWidgets.QApplication(sys.argv)


def main():
    main = MainWindow(app)
    main.show()
    app.exec()


if __name__ == "__main__":
    main()
