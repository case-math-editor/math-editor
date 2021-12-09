import sys
from functools import wraps


from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWinExtras import QtWin
import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

from design import Ui_MainWindow

# Отображение иконки в панели задач
myappid = 'mycompany.myproduct.subproduct.version'
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)

# Использование latex в matplotlib
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

    def draw_text(self, text, fontsize):
        self.axes.clear()
        self.axes.axis("off")
        if text != "":
            text = "".join(text.splitlines())
            self.axes.text(0.5, 0.5, f"${text}$",
                           horizontalalignment='center',
                           verticalalignment='center',
                           fontsize=fontsize, color='black')
        self.draw()


class NavigationToolbar(NavigationToolbar2QT):
    toolitems = [t for t in NavigationToolbar2QT.toolitems if
                 t[0] in ('Home', 'Back', 'Forward', 'Pan', 'Save')]


class SaveMessageBox(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        super().setIcon(QtWidgets.QMessageBox.Question)
        super().setWindowTitle('Сохранение')
        super().setText('Сохранить изменения?')
        super().setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        self.yes_btn = self.button(QtWidgets.QMessageBox.Yes)
        self.yes_btn.setText('Да')
        self.no_btn = self.button(QtWidgets.QMessageBox.No)
        self.no_btn.setText('Нет')
        self.cnl_btn = self.button(QtWidgets.QMessageBox.Cancel)
        self.cnl_btn.setText('Отмена')
        self.exec_()


class AppWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.textBox.moveCursor(QtGui.QTextCursor.End)
        self.textBox.setFocus()

        self.text = self.textBox.toPlainText()
        self.saved_text = None
        self.is_saved = False
        self.file_path = None

        # Отрисовка matplotlib в приложении
        self.canvas = MplCanvas(self)
        toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout_3.addWidget(toolbar)
        self.verticalLayout_3.addWidget(self.canvas)
        self.canvas.draw_text(self.text, self.fontsizeBox.value())

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
        self.textBox.textChanged.connect(self.text_changed)

    # Отрисовка latex
    def show_latex(self):
        try:
            self.canvas.draw_text(self.text, self.fontsizeBox.value())
        except RuntimeError as e:
            self.text = ""
            QtWidgets.QMessageBox.about(self, "Ошибка", "Введите корректную latex последовательность")

    # Очистка textBox
    def clear_text(self):
        self.textBox.selectAll()
        self.textBox.textCursor().removeSelectedText()
        self.textBox.appendPlainText(r"\\")

    # Изменение текста в textBox
    def text_changed(self):
        if self.textBox.toPlainText() != self.saved_text:
            self.setWindowTitle("Equation Editor*")
            self.is_saved = False
            self.text = self.textBox.toPlainText()

        else:
            self.text = self.saved_text
            self.setWindowTitle("Equation Editor")
            self.is_saved = True

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

    def __save_txt(self, path):
        with open(path, 'w') as f:
            f.write(self.text)
        self.setWindowTitle("Equation Editor")
        self.file_path = path
        self.is_saved = True
        self.saved_text = self.text

    def undo_text(self):
        self.textBox.undo()

    def redo_text(self):
        self.textBox.redo()

    # Диалоговое окно о сохранении файла
    def __save_popup(self):
        if not self.is_saved:
            box = SaveMessageBox()
            if box.clickedButton() == box.yes_btn:
                self.save()
            elif box.clickedButton() == box.cnl_btn:
                return False
        return True

    # Открытие текстового файла
    def open_file(self):
        reply = self.__save_popup()
        if reply:
            path, _ = QtWidgets.QFileDialog.getOpenFileName()
            if path != "":
                self.file_path = path
                self.is_saved = True
                with open(self.file_path, 'r') as f:
                    self.saved_text = f.read()
                    self.clear_text()
                    self.textBox.insertPlainText(self.saved_text)
                    self.text = self.saved_text

    # Создать новый файл
    def new_file(self):
        reply = self.__save_popup()
        if reply:
            self.clear_text()
            self.show_latex()
            self.file_path = None
            self.is_saved = False

    # Закрытие приложения
    def closeEvent(self, event):
        reply = self.__save_popup()
        if not reply:
            event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AppWindow()  # Создаём объект класса AppWindow
    window.show()  # Показываем окно
    sys.exit(app.exec())  # и запускаем приложение


if __name__ == '__main__':
    main()
