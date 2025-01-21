# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuiTBTsis.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setSizeIncrement(QSize(800, 600))
        MainWindow.setBaseSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(298, 0, 172, 22))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 40, 801, 561))
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setIconSize(QSize(32, 32))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1.setFont(font)
        self.tab1.setContextMenuPolicy(Qt.NoContextMenu)
        self.tab1Panel = QWidget(self.tab1)
        self.tab1Panel.setObjectName(u"tab1Panel")
        self.tab1Panel.setEnabled(True)
        self.tab1Panel.setGeometry(QRect(380, 30, 401, 481))
        self.label_11 = QLabel(self.tab1Panel)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(130, 10, 161, 22))
        self.label_12 = QLabel(self.tab1Panel)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 130, 111, 22))
        self.tab1ComboBilete = QComboBox(self.tab1Panel)
        self.tab1ComboBilete.setObjectName(u"tab1ComboBilete")
        self.tab1ComboBilete.setGeometry(QRect(140, 40, 151, 22))
        self.tab1ComboBilete.addItem('a')
        self.tab1ComboBilete.addItem('b')
        self.tab1ComboBilete.currentIndexChanged.connect()
        self.widget = QWidget(self.tab1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 70, 273, 156))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        self.label_9.setPalette(palette)

        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        self.label_7.setPalette(palette1)

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.tab1TfEmail = QLineEdit(self.widget)
        self.tab1TfEmail.setObjectName(u"tab1TfEmail")

        self.gridLayout.addWidget(self.tab1TfEmail, 3, 3, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.tab1TfCnp = QLineEdit(self.widget)
        self.tab1TfCnp.setObjectName(u"tab1TfCnp")

        self.gridLayout.addWidget(self.tab1TfCnp, 2, 3, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.tab1TfNume = QLineEdit(self.widget)
        self.tab1TfNume.setObjectName(u"tab1TfNume")

        self.gridLayout.addWidget(self.tab1TfNume, 0, 3, 1, 1)

        self.tab1TfPrenume = QLineEdit(self.widget)
        self.tab1TfPrenume.setObjectName(u"tab1TfPrenume")

        self.gridLayout.addWidget(self.tab1TfPrenume, 1, 3, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        self.label_8.setPalette(palette2)

        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)

        self.tab1TfTelefon = QLineEdit(self.widget)
        self.tab1TfTelefon.setObjectName(u"tab1TfTelefon")

        self.gridLayout.addWidget(self.tab1TfTelefon, 4, 3, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        self.label_10.setPalette(palette3)

        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.tabWidget.addTab(self.tab3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Powered by CadFrunze", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Selecteaza Tip Ticket", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pret/buc: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CNP", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Prenume", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nume", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Buy Ticket", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Activate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

