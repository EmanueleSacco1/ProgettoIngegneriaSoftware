from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_FrameAreaAssociato(object):
    def setupUi(self, FrameAreaAssociato):
        FrameAreaAssociato.setObjectName("FrameAreaAssociato")
        FrameAreaAssociato.resize(890, 562)
        FrameAreaAssociato.setMaximumSize(QtCore.QSize(890, 562))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FrameAreaAssociato.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(parent=FrameAreaAssociato)
        self.label.setGeometry(QtCore.QRect(480, 40, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=FrameAreaAssociato)
        self.label_2.setGeometry(QtCore.QRect(320, 30, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=FrameAreaAssociato)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 180, 90))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=FrameAreaAssociato)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 100, 180, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=FrameAreaAssociato)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 230, 180, 90))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=FrameAreaAssociato)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 230, 180, 90))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=FrameAreaAssociato)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 360, 180, 90))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=FrameAreaAssociato)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 360, 180, 90))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(FrameAreaAssociato)
        QtCore.QMetaObject.connectSlotsByName(FrameAreaAssociato)

    def retranslateUi(self, FrameAreaAssociato):
        _translate = QtCore.QCoreApplication.translate
        FrameAreaAssociato.setWindowTitle(_translate("FrameAreaAssociato", "AreaAssociato"))
        self.label_2.setText(_translate("FrameAreaAssociato", "AREA ASSOCIATO"))
        self.pushButton.setText(_translate("FrameAreaAssociato", "Visualizza storico gare"))
        self.pushButton_2.setText(_translate("FrameAreaAssociato", "Visualizza gare"))
        self.pushButton_3.setText(_translate("FrameAreaAssociato", "Accettazione gara"))
        self.pushButton_4.setText(_translate("FrameAreaAssociato", "Scarica modulo referto"))
        self.pushButton_5.setText(_translate("FrameAreaAssociato", "Carica modulo referto"))
        self.pushButton_6.setText(_translate("FrameAreaAssociato", "Carica certificato medico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrameAreaAssociato = QtWidgets.QWidget()
    ui = Ui_FrameAreaAssociato()
    ui.setupUi(FrameAreaAssociato)
    FrameAreaAssociato.show()
    sys.exit(app.exec())


