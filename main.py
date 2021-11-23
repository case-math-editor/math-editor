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

        # Получение текста из textBox
        self.text = self.textBox.toPlainText()
        # self.text_cache = [self.text]

        # Отрисовка matplotlib в приложении
        self.canvas = MplCanvas(self)
        toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout_3.addWidget(toolbar)
        self.verticalLayout_3.addWidget(self.canvas)
        self.canvas.draw_text(self.text)

        # Создание сигналов
        self.showButton.clicked.connect(self.show_btn_clicked)
        self.clear_textButton.clicked.connect(self.clear_text_btn_clicked)
        self.symbolButton.buttonClicked.connect(self.btn_group_clicked)
        self.textBox.installEventFilter(self)

    # Отрисовка latex
    def show_btn_clicked(self):
        self.text = self.textBox.toPlainText()
        self.canvas.draw_text(self.text)

    # Очистка textBox
    def clear_text_btn_clicked(self):
        self.textBox.clear()

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


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AppWindow()  # Создаём объект класса AppWindow
    window.show()  # Показываем окно
    sys.exit(app.exec())  # и запускаем приложение

if __name__ == '__main__':
    main()
