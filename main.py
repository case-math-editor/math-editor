import sys

from PyQt5 import QtWidgets, QtGui, QtCore
import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from design import Ui_MainWindow

mpl.use("Qt5Agg")
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'


# корректная отрисовка на мониторах с высоким разрешением
# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
#
# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=4, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.patch.set_alpha(0)
        self.axes = fig.add_subplot(111)
        self.axes.patch.set_alpha(0)
        super(MplCanvas, self).__init__(fig)

    def draw_text(self, text):
        self.axes.clear()
        self.axes.axis("off")
        if text != "":
            text = "".join(text.splitlines())
            self.axes.text(0.5, 0.5, f"${text}$",
                           horizontalalignment='center',
                           verticalalignment='center',
                           fontsize=30, color='black')
        self.draw()


class AppWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.textBox.moveCursor(QtGui.QTextCursor.End)
        self.textBox.setFocus()

        self.text = self.textBox.toPlainText()
        self.file_path = None

        # Отрисовка matplotlib в приложении
        self.canvas = MplCanvas(self)
        toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout_3.addWidget(toolbar)
        self.verticalLayout_3.addWidget(self.canvas)
        self.canvas.draw_text(self.text)

        # Создание сигналов
        self.showButton.clicked.connect(self.show_latex)
        self.clear_textButton.clicked.connect(self.clear_text)
        self.symbolButton.buttonClicked.connect(self.btn_group_clicked)
        self.textBox.installEventFilter(self)
        self.actionOpen.triggered.connect(self.open_file)
        self.saveButton.clicked.connect(self.save)
        self.actionSave.triggered.connect(self.save)
        self.actionSaveAs.triggered.connect(self.save_as)
        self.actionNew.triggered.connect(self.new_file)
        self.actionExit.triggered.connect(self.close)
        self.redoButton.clicked.connect(self.redo_text)
        self.undoButton.clicked.connect(self.undo_text)
        self.actionRedo.triggered.connect(self.redo_text)
        self.actionUndo.triggered.connect(self.undo_text)

    # Отрисовка latex
    def show_latex(self):
        try:
            self.text = self.textBox.toPlainText()
            self.canvas.draw_text(self.text)
        except RuntimeError as e:
            QtWidgets.QMessageBox.about(self, "Ошибка", "Введите корректную latex последовательность")

    # Очистка textBox
    def clear_text(self):
        self.textBox.clear()
        self.text = self.textBox.toPlainText()

    # Добавление символа/операции из меню
    def btn_group_clicked(self, btn):
        self.textBox.insertPlainText(btn.whatsThis())
        self.textBox.setFocus()

    # Добавление новой строки latex после нажатия enter в textBox
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.textBox:
            if event.key() == QtCore.Qt.Key_Return and self.textBox.hasFocus():
                self.textBox.appendPlainText(r"\\")
                return True
        return super().eventFilter(obj, event)

    # Сохранить
    def save(self):
        if self.file_path is None:
            self.save_as()
        else:
            self.__save_txt(self.file_path)

    # Сохранить как
    def save_as(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл",
                                                        filter="Text files (*.txt)")
        if path != '':
            self.__save_txt(path)
            self.file_path = path

    def undo_text(self):
        self.textBox.undo()

    def redo_text(self):
        self.textBox.redo()

    # Диалоговое окно о сохранении файла
    def __save_popup(self):
        # Создание диалогового окна
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle('Сохранение')
        box.setText('Сохранить изменения?')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        yes_btn = box.button(QtWidgets.QMessageBox.Yes)
        yes_btn.setText('Да')
        no_btn = box.button(QtWidgets.QMessageBox.No)
        no_btn.setText('Нет')
        cnl_btn = box.button(QtWidgets.QMessageBox.Cancel)
        cnl_btn.setText('Отмена')
        box.exec_()
        # Обработка нажатий на кнопки
        if box.clickedButton() == yes_btn:
            self.save_as()
            return ""
        elif box.clickedButton() == no_btn:
            return ""
        elif box.clickedButton() == cnl_btn:
            return "cancel"

    # Открытие текстового файла
    def open_file(self):
        reply = None
        if self.file_path is None and self.text != "":
            reply = self.__save_popup()
        if reply != "cancel":
            path, _ = QtWidgets.QFileDialog.getOpenFileName()
            if path != "":
                self.file_path = path
                with open(self.file_path, 'r') as f:
                    self.textBox.insertPlainText(f.read())
                    self.text = self.textBox.toPlainText()

    # Создать новый файл
    def new_file(self):
        reply = None
        if self.file_path is None and self.text != "":
            reply = self.__save_popup()
        if reply != "cancel":
            self.clear_text()
            self.show_latex()
            self.file_path = None

    # Закрытие приложения
    def closeEvent(self, event):
        reply = None
        if self.file_path is None and self.text != "":
            reply = self.__save_popup()
        if reply == "":
            event.accept()
        else:
            event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AppWindow()  # Создаём объект класса AppWindow
    window.show()  # Показываем окно
    sys.exit(app.exec())  # и запускаем приложение


if __name__ == '__main__':
    main()
