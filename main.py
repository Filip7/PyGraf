import sys
from PyQt6 import QtWidgets
from db_3 import Db
from ui import MainWindow


app = QtWidgets.QApplication(sys.argv)


def main():
    db = Db()
    main = MainWindow(app, db)
    main.show()
    app.exec()


if __name__ == "__main__":
    main()
