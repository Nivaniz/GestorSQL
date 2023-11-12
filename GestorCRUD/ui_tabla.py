# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablattXIlP.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(922, 505)
        icon = QIcon()
        icon.addFile(u"../../../Downloads/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 301, 431))
        font = QFont()
        font.setFamilies([u"Microsoft Yi Baiti"])
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 330, 271, 89))
        self.verticalLayout_3 = QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.boton_nuevo = QPushButton(self.horizontalLayoutWidget)
        self.boton_nuevo.setObjectName(u"boton_nuevo")
        font1 = QFont()
        font1.setFamilies([u"Microsoft Sans Serif"])
        font1.setPointSize(11)
        self.boton_nuevo.setFont(font1)

        self.verticalLayout_3.addWidget(self.boton_nuevo)

        self.boton_borrar = QPushButton(self.horizontalLayoutWidget)
        self.boton_borrar.setObjectName(u"boton_borrar")
        self.boton_borrar.setFont(font1)

        self.verticalLayout_3.addWidget(self.boton_borrar)

        self.boton_modificar = QPushButton(self.horizontalLayoutWidget)
        self.boton_modificar.setObjectName(u"boton_modificar")
        self.boton_modificar.setFont(font1)

        self.verticalLayout_3.addWidget(self.boton_modificar)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 40, 64, 261))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.widget)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setFont(font1)

        self.verticalLayout.addWidget(self.label_nombre)

        self.label_apellido = QLabel(self.widget)
        self.label_apellido.setObjectName(u"label_apellido")
        self.label_apellido.setFont(font1)

        self.verticalLayout.addWidget(self.label_apellido)

        self.label_sexo = QLabel(self.widget)
        self.label_sexo.setObjectName(u"label_sexo")
        self.label_sexo.setFont(font1)

        self.verticalLayout.addWidget(self.label_sexo)

        self.label_edad = QLabel(self.widget)
        self.label_edad.setObjectName(u"label_edad")
        self.label_edad.setFont(font1)

        self.verticalLayout.addWidget(self.label_edad)

        self.label_empleo = QLabel(self.widget)
        self.label_empleo.setObjectName(u"label_empleo")
        self.label_empleo.setFont(font1)

        self.verticalLayout.addWidget(self.label_empleo)

        self.label_numero = QLabel(self.widget)
        self.label_numero.setObjectName(u"label_numero")
        self.label_numero.setFont(font1)

        self.verticalLayout.addWidget(self.label_numero)

        self.label_email = QLabel(self.widget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setFont(font1)

        self.verticalLayout.addWidget(self.label_email)

        self.widget1 = QWidget(self.groupBox)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(90, 40, 191, 271))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_nombre = QLineEdit(self.widget1)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setFont(font1)

        self.verticalLayout_2.addWidget(self.line_nombre)

        self.line_apellido = QLineEdit(self.widget1)
        self.line_apellido.setObjectName(u"line_apellido")
        self.line_apellido.setFont(font1)

        self.verticalLayout_2.addWidget(self.line_apellido)

        self.line_sexo = QLineEdit(self.widget1)
        self.line_sexo.setObjectName(u"line_sexo")
        self.line_sexo.setFont(font1)

        self.verticalLayout_2.addWidget(self.line_sexo)

        self.line_edad = QLineEdit(self.widget1)
        self.line_edad.setObjectName(u"line_edad")
        self.line_edad.setFont(font1)

        self.verticalLayout_2.addWidget(self.line_edad)

        self.line_empleo = QLineEdit(self.widget1)
        self.line_empleo.setObjectName(u"line_empleo")
        self.line_empleo.setFont(font1)

        self.verticalLayout_2.addWidget(self.line_empleo)

        self.line_telefono = QLineEdit(self.widget1)
        self.line_telefono.setObjectName(u"line_telefono")
        self.line_telefono.setFont(font1)

        self.verticalLayout_2.addWidget(self.line_telefono)

        self.line_email = QLineEdit(self.widget1)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setFont(font1)

        self.verticalLayout_2.addWidget(self.line_email)

        self.tabla = QTableView(self.centralwidget)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(340, 30, 561, 421))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 922, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestor de Personal", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos de Registro", None))
        self.boton_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.boton_borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.boton_modificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.label_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombres", None))
        self.label_apellido.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None))
        self.label_sexo.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.label_edad.setText(QCoreApplication.translate("MainWindow", u"Edad", None))
        self.label_empleo.setText(QCoreApplication.translate("MainWindow", u"Empleo", None))
        self.label_numero.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
    # retranslateUi

