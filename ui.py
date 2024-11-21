from PyQt6 import QtWidgets, uic
from graf import Graf


class MainWindow(QtWidgets.QMainWindow):
    graf = Graf()

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load the UI Page
        uic.loadUi("mainwindow.ui", self)

        # Set button actions
        self.add_row_btn.clicked.connect(self.add_row)
        self.remove_row_btn.clicked.connect(self.remove_row)
        self.show_btn.clicked.connect(self.show_graph)
        self.save_file_btn.clicked.connect(self.save_as)
        self.save_file_tight_btn.clicked.connect(self.save_as_tight)
        self.picker_btn.clicked.connect(self.show_color_picker)

        # Set default button value to excape errors
        initial_color = "#000000"
        self.color_edit.setText(initial_color)
        self.color_edit.setStyleSheet(f"background-color: {initial_color}")

        # Menu item actions
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionQuit.triggered.connect(app.quit)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

        # Fill table width
        self.tableWidget.setColumnWidth(0, 353)
        self.tableWidget.setColumnWidth(1, 154)

    def add_row(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())

    def remove_row(self):
        self.tableWidget.removeRow(self.tableWidget.rowCount() - 1)

    def save_as(self):
        self.generate_graph()
        name = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", filter=("Images (*.png *.jpg)")
        )
        self.graf.save_graph_to_file(name[0])

    def save_as_tight(self):
        self.generate_graph()
        name = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", filter=("Images (*.png *.jpg)")
        )
        self.graf.save_graph_as_tight_layout(name[0])

    def show_about(self):
        QtWidgets.QMessageBox.about(
            self,
            "About PyGraf",
            """
            This was built using Python and Qt

            Goal of this app is to generate and save bar graph in any color you wish.
            App is rough around the edges, but this was always 
            more a proof of concept, then anything else.

            Enjoy :)
            """,
        )

    def about_qt(self):
        QtWidgets.QMessageBox.aboutQt(self)

    def generate_graph(self):
        categories = []
        values = []
        for row in range(self.tableWidget.rowCount()):
            column_item = self.tableWidget.item(
                row, 0
            )  # Get the item in the first column
            value_item = self.tableWidget.item(
                row, 1
            )  # Get the item in the second column
            if column_item is None or value_item is None:
                break

            column_name = column_item.text()
            value_name = value_item.text()
            # Unescape the column_name string
            column_name = bytes(column_name, "utf-8").decode("unicode_escape")

            # Check if the text values are empty
            if not column_name.strip() or not value_name.strip():
                break

            categories.append(column_name)
            values.append(int(value_name))

        color_val = self.color_edit.text()
        self.graf.init(categories, values, color_val)

    def show_graph(self):
        self.generate_graph()
        self.graf.show_graph()

    def show_color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        rgb = color.getRgb()
        dark = isDark(rgb)
        self.color_edit.setText(color.name())
        self.color_edit.setStyleSheet(
            f"background-color: {color.name()}; color:  {"white" if dark else "black"}"
        )


# Algorithm from:
# https://stackoverflow.com/questions/3942878/how-to-decide-font-color-in-white-or-black-depending-on-background-color
def isDark(rgb) -> bool:
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    return ((r * 0.299) + (g * 0.587) + (b * 0.114)) <= 186
