import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from design import Ui_MainWindow

import matplotlib

matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# корректная отрисовка на мониторах с высоким разрешением
# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
#
# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class AppWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        # Получение текста из textBox
        self.text = self.textEdit.toPlainText()
        self.text_cache = [self.text]
        # Отрисовка matplotlib в приложении
        canvas = MplCanvas(self)
        self.ax = canvas.axes
        self.ax.text(0.5, 0.9, f"${self.text}$",
                     horizontalalignment='center',
                     verticalalignment='center',
                     fontsize=20, color='black')
        self.ax.axis("off")
        toolbar = NavigationToolbar(canvas, self)
        self.verticalLayout_3.addWidget(toolbar)
        self.verticalLayout_3.addWidget(canvas)
        # Создание сигналов
        self.showButton.clicked.connect(self.show_btn_clicked)

    def show_btn_clicked(self):
        self.ax.clear()
        self.text = self.textEdit.toPlainText()
        self.ax.text(0.5, 0.9, f"${self.text}$",
                     horizontalalignment='center',
                     verticalalignment='center',
                     fontsize=20, color='black')
        self.ax.axis("off")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AppWindow()  # Создаём объект класса AppWindow
    window.show()  # Показываем окно
    sys.exit(app.exec())  # и запускаем приложение


if __name__ == '__main__':
    main()
