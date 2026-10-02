import sys

from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox
from In_Class_example import Ui_Dialog


class SimpleDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.Buttton1.button(
            QDialogButtonBox.StandardButton.Ok
        )
        self.ok_button.clicked.connect(self.on_ok_clicked)

    def on_ok_clicked(self):
        print(self.ui.LineEditName.text())
        self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = SimpleDialog()
    dlg.exec()

print("Christian Ramirez-Flores")