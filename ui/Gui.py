# -*- coding: utf-8 -*-
import random

################################################################################
## Form generated from reading UI file 'GuiRoaBFx.ui'
##
## Created by: CadFrunze Interface Compiler version 6.5.0
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

from services.services import Services


class Ui_MainWindow(object):
    def __init__(self, srv:Services=Services()):
        self.stocuri:dict = dict()
        self.srv=srv
        self.cantitate:list = list()


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
#------------------------------TAB1 PANEL------------------
        self.tab1Panel = QWidget(self.tab1)
        self.tab1Panel.setObjectName(u"tab1Panel")
        self.tab1Panel.setEnabled(True)
        self.tab1Panel.setGeometry(QRect(380, 30, 401, 481))
        self.label_11 = QLabel(self.tab1Panel)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(130, 10, 161, 22))
        self.tab1LbPretBuc = QLabel(self.tab1Panel)
        self.tab1LbPretBuc.setObjectName(u"tab1LbPretBuc")
        self.tab1LbPretBuc.setGeometry(QRect(30, 130, 131, 22))


#-----------------TAB1 LISTA BILETE---------------------------------------------

        self.tab1ListaBilete = QComboBox(self.tab1Panel)
        self.tab1ListaBilete.setObjectName(u"tab1ListaBilete")
        self.tab1ListaBilete.setGeometry(QRect(130, 40, 161, 22))



#-----------------TAB1 CANTITATE---------------------------------------------
        self.tab1LbCantitate = QLineEdit(self.tab1Panel)
        self.tab1LbCantitate.setObjectName(u"tab1LbCantitate")
        self.tab1LbCantitate.setGeometry(QRect(340, 130, 51, 22))
        self.label_13 = QLabel(self.tab1Panel)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(230, 140, 99, 12))
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(True)
        self.label_13.setFont(font1)
        self.tab1LbCost = QLabel(self.tab1Panel)
        self.tab1LbCost.setObjectName(u"tab1LbCost")
        self.tab1LbCost.setGeometry(QRect(110, 260, 211, 51))
        self.tab1ButBuy = QPushButton(self.tab1Panel)
        self.tab1ButBuy.setObjectName(u"tab1ButBuy")
        self.tab1ButBuy.setGeometry(QRect(110, 363, 211, 71))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.tab1ButBuy.setPalette(palette)
        self.tab1ButBuy.setCursor(QCursor(Qt.OpenHandCursor))
        self.layoutWidget = QWidget(self.tab1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 70, 273, 156))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        self.label_9.setPalette(palette1)

        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        self.label_7.setPalette(palette2)

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

#---------------------------------TAB1 EMAIL------------------
        self.tab1TfEmail = QLineEdit(self.layoutWidget)
        self.tab1TfEmail.setObjectName(u"tab1TfEmail")

        self.gridLayout.addWidget(self.tab1TfEmail, 3, 3, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

#------------- --------------------------TAB1 CNP------------------
        self.tab1TfCnp = QLineEdit(self.layoutWidget)
        self.tab1TfCnp.setObjectName(u"tab1TfCnp")

        self.gridLayout.addWidget(self.tab1TfCnp, 2, 3, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

#------------------------------------TAB1 NUME------------------
        self.tab1TfNume = QLineEdit(self.layoutWidget)
        self.tab1TfNume.setObjectName(u"tab1TfNume")

        self.gridLayout.addWidget(self.tab1TfNume, 0, 3, 1, 1)


#--------------------------TAB1 PRENUME------------------
        self.tab1TfPrenume = QLineEdit(self.layoutWidget)
        self.tab1TfPrenume.setObjectName(u"tab1TfPrenume")

        self.gridLayout.addWidget(self.tab1TfPrenume, 1, 3, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        self.label_8.setPalette(palette3)

        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)

#-------------------------------------TAB1 TELEFON------------------
        self.tab1TfTelefon = QLineEdit(self.layoutWidget)
        self.tab1TfTelefon.setObjectName(u"tab1TfTelefon")

        self.gridLayout.addWidget(self.tab1TfTelefon, 4, 3, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        self.label_10.setPalette(palette4)

        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)

        self.tab1LbCredential = QLabel(self.tab1)
        self.tab1LbCredential.setObjectName(u"tab1LbCredential")
        self.tab1LbCredential.setGeometry(QRect(20, 260, 321, 16))
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tab2TfSerie1 = QLineEdit(self.tab2)
        self.tab2TfSerie1.setObjectName(u"tab2TfSerie1")
        self.tab2TfSerie1.setGeometry(QRect(220, 40, 41, 21))
        self.tab2TfSerie1.setMaxLength(3)
        self.label_14 = QLabel(self.tab2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 40, 148, 22))
        self.tab2TfSerie2 = QLineEdit(self.tab2)
        self.tab2TfSerie2.setObjectName(u"tab2TfSerie2")
        self.tab2TfSerie2.setGeometry(QRect(290, 40, 41, 21))
        self.tab2TfSerie2.setMaxLength(3)
        self.tab2TfSerie3 = QLineEdit(self.tab2)
        self.tab2TfSerie3.setObjectName(u"tab2TfSerie3")
        self.tab2TfSerie3.setGeometry(QRect(360, 40, 41, 21))
        self.tab2TfSerie3.setMaxLength(3)
        self.label_15 = QLabel(self.tab2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(270, 40, 13, 22))
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_16 = QLabel(self.tab2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(340, 40, 13, 22))
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_17 = QLabel(self.tab2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(510, 40, 33, 22))
        self.tab2TfCnp = QLineEdit(self.tab2)
        self.tab2TfCnp.setObjectName(u"tab2TfCnp")
        self.tab2TfCnp.setGeometry(QRect(570, 40, 181, 21))
        self.tab2Panel = QWidget(self.tab2)
        self.tab2Panel.setObjectName(u"tab2Panel")
        self.tab2Panel.setGeometry(QRect(20, 130, 751, 371))
        self.tab2LbRezultat = QLabel(self.tab2Panel)
        self.tab2LbRezultat.setObjectName(u"tab2LbRezultat")
        self.tab2LbRezultat.setGeometry(QRect(280, 40, 181, 51))
        self.tab2ButActiveaza = QPushButton(self.tab2Panel)
        self.tab2ButActiveaza.setObjectName(u"tab2ButActiveaza")
        self.tab2ButActiveaza.setGeometry(QRect(250, 140, 211, 61))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.tab2ButActiveaza.setPalette(palette5)
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.tab2ButActiveaza.setFont(font2)
        self.tab2ButActiveaza.setCursor(QCursor(Qt.OpenHandCursor))
        self.tab2LbAchizitionat = QLabel(self.tab2Panel)
        self.tab2LbAchizitionat.setObjectName(u"tab2LbAchizitionat")
        self.tab2LbAchizitionat.setGeometry(QRect(260, 250, 251, 31))
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.label_18 = QLabel(self.tab3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 40, 148, 22))
        self.tab3TfSerie1 = QLineEdit(self.tab3)
        self.tab3TfSerie1.setObjectName(u"tab3TfSerie1")
        self.tab3TfSerie1.setGeometry(QRect(230, 40, 41, 21))
        self.tab3TfSerie1.setMaxLength(3)
        self.tab3TfSerie3 = QLineEdit(self.tab3)
        self.tab3TfSerie3.setObjectName(u"tab3TfSerie3")
        self.tab3TfSerie3.setGeometry(QRect(370, 40, 41, 21))
        self.tab3TfSerie3.setMaxLength(3)
        self.label_19 = QLabel(self.tab3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(280, 40, 13, 22))
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_20 = QLabel(self.tab3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(350, 40, 13, 22))
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_21 = QLabel(self.tab3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(520, 40, 33, 22))
        self.tab3TfSerie2 = QLineEdit(self.tab3)
        self.tab3TfSerie2.setObjectName(u"tab3TfSerie2")
        self.tab3TfSerie2.setGeometry(QRect(300, 40, 41, 21))
        self.tab3TfSerie2.setMaxLength(3)
        self.tab3TfCnp = QLineEdit(self.tab3)
        self.tab3TfCnp.setObjectName(u"tab3TfCnp")
        self.tab3TfCnp.setGeometry(QRect(580, 40, 181, 21))
        self.tab3Panel = QWidget(self.tab3)
        self.tab3Panel.setObjectName(u"tab3Panel")
        self.tab3Panel.setGeometry(QRect(20, 110, 751, 391))
        self.tab3LbNume = QLabel(self.tab3Panel)
        self.tab3LbNume.setObjectName(u"tab3LbNume")
        self.tab3LbNume.setGeometry(QRect(20, 30, 181, 16))
        self.tab3LbPrenume = QLabel(self.tab3Panel)
        self.tab3LbPrenume.setObjectName(u"tab3LbPrenume")
        self.tab3LbPrenume.setGeometry(QRect(250, 30, 281, 16))
        self.tab3LbCnp = QLabel(self.tab3Panel)
        self.tab3LbCnp.setObjectName(u"tab3LbCnp")
        self.tab3LbCnp.setGeometry(QRect(550, 30, 191, 16))
        self.label_24 = QLabel(self.tab3Panel)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 80, 41, 22))
        self.label_24.setTextFormat(Qt.PlainText)
        self.label_25 = QLabel(self.tab3Panel)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(430, 80, 56, 22))
        self.tab3TfEmail = QLineEdit(self.tab3Panel)
        self.tab3TfEmail.setObjectName(u"tab3TfEmail")
        self.tab3TfEmail.setGeometry(QRect(90, 80, 171, 21))
        self.tab3TfTelefon = QLineEdit(self.tab3Panel)
        self.tab3TfTelefon.setObjectName(u"tab3TfTelefon")
        self.tab3TfTelefon.setGeometry(QRect(510, 80, 191, 21))
        self.tab3ButSave = QPushButton(self.tab3Panel)
        self.tab3ButSave.setObjectName(u"tab3ButSave")
        self.tab3ButSave.setGeometry(QRect(300, 170, 151, 61))
        palette6 = QPalette()
        brush3 = QBrush(QColor(0, 255, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        self.tab3ButSave.setPalette(palette6)
        self.tab3ButSave.setCursor(QCursor(Qt.OpenHandCursor))
        self.tab3ButDelete = QPushButton(self.tab3Panel)
        self.tab3ButDelete.setObjectName(u"tab3ButDelete")
        self.tab3ButDelete.setGeometry(QRect(300, 250, 151, 61))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.tab3ButDelete.setPalette(palette7)
        self.tab3ButDelete.setCursor(QCursor(Qt.OpenHandCursor))
        self.tab3LbPremiu = QLabel(self.tab3Panel)
        self.tab3LbPremiu.setObjectName(u"tab3LbPremiu")
        self.tab3LbPremiu.setGeometry(QRect(10, 190, 251, 16))
        self.tabWidget.addTab(self.tab3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)

#----------------------SLOTURI-------------------------
#----------------------PT TAB1------------------------
        self.tab1Panel.setVisible(False)
        self.tab1TfNume.textChanged.connect(self.change_text)
        self.tab1TfPrenume.textChanged.connect(self.change_text)
        self.tab1TfCnp.textChanged.connect(self.change_text)
        self.tab1TfEmail.textChanged.connect(self.change_text)
        self.tab1ListaBilete.currentTextChanged.connect(self.elements_tickets)
        self.tab1LbCantitate.textChanged.connect(self.calcul_bilete)


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Powered by CadFrunze", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Selecteaza Tip Ticket", None))
        self.tab1LbPretBuc.setText(QCoreApplication.translate("MainWindow", u"Pret/buc: ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Introdu nr. bilete", None))
        self.tab1LbCost.setText(QCoreApplication.translate("MainWindow", u"Cost: ", None))
        self.tab1ButBuy.setText(QCoreApplication.translate("MainWindow", u"Plateste:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CNP", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Prenume", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nume", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.tab1LbCredential.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Buy Ticket", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Introdu Serie Ticket", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CNP", None))
        self.tab2LbRezultat.setText(QCoreApplication.translate("MainWindow", u"Bilet: ", None))
        self.tab2ButActiveaza.setText(QCoreApplication.translate("MainWindow", u"Activeaza si intra in tragere la sorti!", None))
        self.tab2LbAchizitionat.setText(QCoreApplication.translate("MainWindow", u"Bilet achizitionat:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Activate", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Introdu Serie Ticket", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CNP", None))
        self.tab3LbNume.setText(QCoreApplication.translate("MainWindow", u"Nume: ", None))
        self.tab3LbPrenume.setText(QCoreApplication.translate("MainWindow", u"Prenume:", None))
        self.tab3LbCnp.setText(QCoreApplication.translate("MainWindow", u"CNP: ", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.tab3ButSave.setText(QCoreApplication.translate("MainWindow", u"Save!", None))
        self.tab3ButDelete.setText(QCoreApplication.translate("MainWindow", u"Delete!", None))
        self.tab3LbPremiu.setText(QCoreApplication.translate("MainWindow", u"Premiu Castigat:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

#--------METODE PT TAB1------------------------
    def change_text(self):
        self.tab1ListaBilete.clear()
        check_cnp:bool = self.srv.check_cnp(self.tab1TfCnp.text().strip())
        if (check_cnp is False) and len(self.tab1TfNume.text().strip())>2 and len(self.tab1TfPrenume.text().strip())>2 and len(self.tab1TfCnp.text().strip())>2 and len(self.tab1TfEmail.text().strip())>2:
            self.tab1Panel.setVisible(True)
            self.stocuri: dict = self.srv.stoc_bilete()
            for elem in self.stocuri.keys():
                self.tab1ListaBilete.addItem(elem)
        else:
            self.tab1Panel.setVisible(False)


    def calcul_bilete(self):
        pret_bilet: int = self.stocuri[self.tab1ListaBilete.currentText()][0]
        nr_locuri_total: int = self.stocuri[self.tab1ListaBilete.currentText()][1]
        nr_locuri_selectat: str = self.tab1LbCantitate.text().strip()
        if not nr_locuri_selectat.isdigit():
            self.tab1LbCredential.setText("Introdu' doar cifre!")
            self.tab1LbCost.setText("Cost: 0 RON")
            self.tab1ButBuy.setEnabled(False)
            self.tab1ButBuy.setText("")
            return
        elif len(self.tab1LbCantitate.text().strip()) == 0 or int(nr_locuri_selectat) == 0:
            self.tab1LbCantitate.setText("1")
            self.tab1LbCredential.setText("Alege cel putin 1 bilet")
            return
        elif int(nr_locuri_selectat) > nr_locuri_total:
            self.tab1LbCantitate.setText(str(nr_locuri_total))
            self.tab1LbCredential.setText(f"Maxim: {nr_locuri_total}")
            return
        else:
            self.tab1LbCredential.setText("")
            self.tab1LbPretBuc.setText(f"Pret: {pret_bilet} RON")
            self.tab1LbCost.setText(f"Cost: {nr_locuri_selectat} X {pret_bilet} = {int(nr_locuri_selectat) * pret_bilet} RON")
            self.tab1ButBuy.setEnabled(True)
            self.tab1ButBuy.setText(f"Plateste: {int(nr_locuri_selectat) * pret_bilet}")

    def elements_tickets(self):
        lista_elem = [key for key in self.stocuri.keys()]
        curren_text: str = self.tab1ListaBilete.currentText().lower().strip()
        if not curren_text or curren_text not in lista_elem:
            return
        else:
            self.tab1LbCantitate.setText(str(self.stocuri[self.tab1ListaBilete.currentText()][1]))
            self.calcul_bilete()






