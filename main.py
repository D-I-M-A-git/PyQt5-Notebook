from GUi import *
import sys


def button_on(button):
    if button.text() == "&Yes":
        exit()


def save_text():
    from PyQt5.QtWidgets import QInputDialog, QMessageBox
    text = ui.plainTextEdit.toPlainText()
    name_file, val_return = QInputDialog.getText(MainWindow, "Діалог", "Напишіть назву файла.")
    if val_return:
        with open(str(name_file), "w", -1, "utf-8") as f:
            f.write(text)
        message = QMessageBox(MainWindow)
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setWindowTitle("Повідомлення")
        message.setText("Файл збережено!\nЗакрити програму?")
        message.setIcon(QMessageBox.Information)
        message.buttonClicked.connect(button_on)
        message.exec_()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
MainWindow.setFixedSize(300, 400)
ui.button_exit.clicked.connect(lambda: exit())
ui.button_save.clicked.connect(save_text)
sys.exit(app.exec_())
