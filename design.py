# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(240,247,248);")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.rightFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightFrame.sizePolicy().hasHeightForWidth())
        self.rightFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.rightFrame.setFont(font)
        self.rightFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightFrame.setObjectName("rightFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rightFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout.addWidget(self.rightFrame, 0, 1, 2, 1)
        self.leftFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftFrame.sizePolicy().hasHeightForWidth())
        self.leftFrame.setSizePolicy(sizePolicy)
        self.leftFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.leftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(self.leftFrame)
        self.saveButton.setBaseSize(QtCore.QSize(0, 0))
        self.saveButton.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"border: none")
        self.saveButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/actions/save_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QtCore.QSize(30, 30))
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.undoButton = QtWidgets.QPushButton(self.leftFrame)
        self.undoButton.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"border: none")
        self.undoButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/actions/undo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon2)
        self.undoButton.setIconSize(QtCore.QSize(22, 22))
        self.undoButton.setObjectName("undoButton")
        self.horizontalLayout.addWidget(self.undoButton)
        self.redoButton = QtWidgets.QPushButton(self.leftFrame)
        self.redoButton.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"border: none")
        self.redoButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/actions/redo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon3)
        self.redoButton.setIconSize(QtCore.QSize(22, 22))
        self.redoButton.setObjectName("redoButton")
        self.horizontalLayout.addWidget(self.redoButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clear_textButton = QtWidgets.QPushButton(self.leftFrame)
        self.clear_textButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_textButton.sizePolicy().hasHeightForWidth())
        self.clear_textButton.setSizePolicy(sizePolicy)
        self.clear_textButton.setMinimumSize(QtCore.QSize(60, 30))
        self.clear_textButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(18,83,130);\n"
"border-radius: 10px;\n"
"")
        self.clear_textButton.setFlat(False)
        self.clear_textButton.setObjectName("clear_textButton")
        self.horizontalLayout.addWidget(self.clear_textButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBox = QtWidgets.QPlainTextEdit(self.leftFrame)
        self.textBox.setObjectName("textBox")
        self.verticalLayout.addWidget(self.textBox)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.showButton = QtWidgets.QPushButton(self.leftFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showButton.sizePolicy().hasHeightForWidth())
        self.showButton.setSizePolicy(sizePolicy)
        self.showButton.setMinimumSize(QtCore.QSize(60, 30))
        self.showButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(18,83,130);\n"
"border-radius: 10px;\n"
"")
        self.showButton.setObjectName("showButton")
        self.horizontalLayout_8.addWidget(self.showButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.gridLayout.addWidget(self.leftFrame, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(199, 70))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.alphaButton = QtWidgets.QPushButton(self.tab)
        self.alphaButton.setEnabled(True)
        self.alphaButton.setStatusTip("")
        self.alphaButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/symbols/alpha.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alphaButton.setIcon(icon4)
        self.alphaButton.setIconSize(QtCore.QSize(9, 9))
        self.alphaButton.setObjectName("alphaButton")
        self.symbolButton = QtWidgets.QButtonGroup(MainWindow)
        self.symbolButton.setObjectName("symbolButton")
        self.symbolButton.addButton(self.alphaButton)
        self.horizontalLayout_2.addWidget(self.alphaButton)
        self.betaButton = QtWidgets.QPushButton(self.tab)
        self.betaButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/symbols/beta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.betaButton.setIcon(icon5)
        self.betaButton.setIconSize(QtCore.QSize(15, 15))
        self.betaButton.setObjectName("betaButton")
        self.symbolButton.addButton(self.betaButton)
        self.horizontalLayout_2.addWidget(self.betaButton)
        self.deltaButton = QtWidgets.QPushButton(self.tab)
        self.deltaButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/symbols/delta.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deltaButton.setIcon(icon6)
        self.deltaButton.setIconSize(QtCore.QSize(15, 15))
        self.deltaButton.setObjectName("deltaButton")
        self.symbolButton.addButton(self.deltaButton)
        self.horizontalLayout_2.addWidget(self.deltaButton)
        self.lambdaButton = QtWidgets.QPushButton(self.tab)
        self.lambdaButton.setStyleSheet("align-items: center")
        self.lambdaButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/symbols/lambda.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lambdaButton.setIcon(icon7)
        self.lambdaButton.setIconSize(QtCore.QSize(12, 12))
        self.lambdaButton.setObjectName("lambdaButton")
        self.symbolButton.addButton(self.lambdaButton)
        self.horizontalLayout_2.addWidget(self.lambdaButton)
        self.thetaButton = QtWidgets.QPushButton(self.tab)
        self.thetaButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/symbols/theta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thetaButton.setIcon(icon8)
        self.thetaButton.setIconSize(QtCore.QSize(15, 15))
        self.thetaButton.setObjectName("thetaButton")
        self.symbolButton.addButton(self.thetaButton)
        self.horizontalLayout_2.addWidget(self.thetaButton)
        self.gammaButton = QtWidgets.QPushButton(self.tab)
        self.gammaButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/symbols/gamma.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gammaButton.setIcon(icon9)
        self.gammaButton.setIconSize(QtCore.QSize(15, 15))
        self.gammaButton.setObjectName("gammaButton")
        self.symbolButton.addButton(self.gammaButton)
        self.horizontalLayout_2.addWidget(self.gammaButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.alphaButton_2 = QtWidgets.QPushButton(self.tab)
        self.alphaButton_2.setEnabled(True)
        self.alphaButton_2.setStatusTip("")
        self.alphaButton_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/symbols/pi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alphaButton_2.setIcon(icon10)
        self.alphaButton_2.setIconSize(QtCore.QSize(9, 9))
        self.alphaButton_2.setObjectName("alphaButton_2")
        self.symbolButton.addButton(self.alphaButton_2)
        self.horizontalLayout_3.addWidget(self.alphaButton_2)
        self.alphaButton_3 = QtWidgets.QPushButton(self.tab)
        self.alphaButton_3.setEnabled(True)
        self.alphaButton_3.setStatusTip("")
        self.alphaButton_3.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/symbols/omega.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alphaButton_3.setIcon(icon11)
        self.alphaButton_3.setIconSize(QtCore.QSize(11, 12))
        self.alphaButton_3.setObjectName("alphaButton_3")
        self.symbolButton.addButton(self.alphaButton_3)
        self.horizontalLayout_3.addWidget(self.alphaButton_3)
        self.alphaButton_4 = QtWidgets.QPushButton(self.tab)
        self.alphaButton_4.setEnabled(True)
        self.alphaButton_4.setStatusTip("")
        self.alphaButton_4.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/symbols/mu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alphaButton_4.setIcon(icon12)
        self.alphaButton_4.setIconSize(QtCore.QSize(15, 15))
        self.alphaButton_4.setObjectName("alphaButton_4")
        self.symbolButton.addButton(self.alphaButton_4)
        self.horizontalLayout_3.addWidget(self.alphaButton_4)
        self.alphaButton_5 = QtWidgets.QPushButton(self.tab)
        self.alphaButton_5.setEnabled(True)
        self.alphaButton_5.setStatusTip("")
        self.alphaButton_5.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/symbols/phi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alphaButton_5.setIcon(icon13)
        self.alphaButton_5.setIconSize(QtCore.QSize(14, 14))
        self.alphaButton_5.setObjectName("alphaButton_5")
        self.symbolButton.addButton(self.alphaButton_5)
        self.horizontalLayout_3.addWidget(self.alphaButton_5)
        self.alphaButton_6 = QtWidgets.QPushButton(self.tab)
        self.alphaButton_6.setEnabled(True)
        self.alphaButton_6.setStatusTip("")
        self.alphaButton_6.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/symbols/epsilon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alphaButton_6.setIcon(icon14)
        self.alphaButton_6.setIconSize(QtCore.QSize(16, 16))
        self.alphaButton_6.setObjectName("alphaButton_6")
        self.symbolButton.addButton(self.alphaButton_6)
        self.horizontalLayout_3.addWidget(self.alphaButton_6)
        self.alphaButton_7 = QtWidgets.QPushButton(self.tab)
        self.alphaButton_7.setEnabled(True)
        self.alphaButton_7.setStatusTip("")
        self.alphaButton_7.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/symbols/rho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alphaButton_7.setIcon(icon15)
        self.alphaButton_7.setIconSize(QtCore.QSize(14, 14))
        self.alphaButton_7.setObjectName("alphaButton_7")
        self.symbolButton.addButton(self.alphaButton_7)
        self.horizontalLayout_3.addWidget(self.alphaButton_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.integralButton = QtWidgets.QPushButton(self.tab_2)
        self.integralButton.setIconSize(QtCore.QSize(30, 16))
        self.integralButton.setObjectName("integralButton")
        self.symbolButton.addButton(self.integralButton)
        self.horizontalLayout_4.addWidget(self.integralButton)
        self.limitButton = QtWidgets.QPushButton(self.tab_2)
        self.limitButton.setObjectName("limitButton")
        self.symbolButton.addButton(self.limitButton)
        self.horizontalLayout_4.addWidget(self.limitButton)
        self.matrixButton = QtWidgets.QPushButton(self.tab_2)
        self.matrixButton.setObjectName("matrixButton")
        self.symbolButton.addButton(self.matrixButton)
        self.horizontalLayout_4.addWidget(self.matrixButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.integralButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.integralButton_2.setIconSize(QtCore.QSize(30, 16))
        self.integralButton_2.setObjectName("integralButton_2")
        self.symbolButton.addButton(self.integralButton_2)
        self.horizontalLayout_5.addWidget(self.integralButton_2)
        self.integralButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.integralButton_3.setIconSize(QtCore.QSize(30, 16))
        self.integralButton_3.setObjectName("integralButton_3")
        self.symbolButton.addButton(self.integralButton_3)
        self.horizontalLayout_5.addWidget(self.integralButton_3)
        self.integralButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.integralButton_4.setIconSize(QtCore.QSize(30, 16))
        self.integralButton_4.setObjectName("integralButton_4")
        self.symbolButton.addButton(self.integralButton_4)
        self.horizontalLayout_5.addWidget(self.integralButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 576, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Equation Editor*"))
        self.clear_textButton.setText(_translate("MainWindow", "ОЧИСТИТЬ"))
        self.textBox.setPlainText(_translate("MainWindow", "\\\\y=\\frac{1}{\\sqrt{x}}"))
        self.showButton.setText(_translate("MainWindow", "ПОКАЗАТЬ"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "\\beta"))
        self.alphaButton.setWhatsThis(_translate("MainWindow", "\\alpha"))
        self.betaButton.setWhatsThis(_translate("MainWindow", "\\beta"))
        self.deltaButton.setWhatsThis(_translate("MainWindow", "\\delta"))
        self.lambdaButton.setWhatsThis(_translate("MainWindow", "\\lambda"))
        self.thetaButton.setWhatsThis(_translate("MainWindow", "\\theta"))
        self.gammaButton.setWhatsThis(_translate("MainWindow", "\\gamma"))
        self.alphaButton_2.setWhatsThis(_translate("MainWindow", "\\pi"))
        self.alphaButton_3.setWhatsThis(_translate("MainWindow", "\\omega"))
        self.alphaButton_4.setWhatsThis(_translate("MainWindow", "\\mu"))
        self.alphaButton_5.setWhatsThis(_translate("MainWindow", "\\phi"))
        self.alphaButton_6.setWhatsThis(_translate("MainWindow", "\\varepsilon"))
        self.alphaButton_7.setWhatsThis(_translate("MainWindow", "\\rho"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Символы"))
        self.integralButton.setWhatsThis(_translate("MainWindow", "\\int_{a}^{b} x \\,dx"))
        self.integralButton.setText(_translate("MainWindow", "Интеграл"))
        self.limitButton.setWhatsThis(_translate("MainWindow", "\\lim_{x\\to\\infty} f(x)"))
        self.limitButton.setText(_translate("MainWindow", "Предел"))
        self.matrixButton.setWhatsThis(_translate("MainWindow", "\\begin{bmatrix}1 & 2 & 3\\\\a & b & c\\end{bmatrix}"))
        self.matrixButton.setText(_translate("MainWindow", "Матрица"))
        self.integralButton_2.setWhatsThis(_translate("MainWindow", "\\frac{a}{b}"))
        self.integralButton_2.setText(_translate("MainWindow", "Дробь"))
        self.integralButton_3.setWhatsThis(_translate("MainWindow", "\\sum_{n=1}^{infty} 2^{-n} = 1"))
        self.integralButton_3.setText(_translate("MainWindow", "Сумма"))
        self.integralButton_4.setWhatsThis(_translate("MainWindow", "\\log_b a"))
        self.integralButton_4.setText(_translate("MainWindow", "Логарифм"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Операции"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menuEdit.setTitle(_translate("MainWindow", "Правка"))
        self.actionNew.setText(_translate("MainWindow", "Создать"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Открыть"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Сохранить"))
        self.actionSaveAs.setText(_translate("MainWindow", "Сохранить как"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Выход"))
        self.actionUndo.setText(_translate("MainWindow", "Отменить"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Повторить"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+R"))
