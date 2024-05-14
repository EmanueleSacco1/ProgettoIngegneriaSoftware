import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QRect


class ModificaUtente(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modifica Utente")
        self.resize(766, 547)

        label = QLabel("Modifica Utente", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(330, 100)

        self.pushButton_1 = QPushButton("Modifica Amministratore", self)
        self.pushButton_1.setGeometry(QRect(270, 230, 180, 90))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.modifica_amministratore)

        self.pushButton_2 = QPushButton("Modifica Associato", self)
        self.pushButton_2.setGeometry(QRect(490, 230, 180, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.modifica_associato)

        icon = QIcon()
        icon.addPixmap(QPixmap("../download.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)

    def modifica_amministratore(self):
        print("Modifica Amministratore")

    def modifica_associato(self):
        print("Modifica Associato")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModificaUtente()
    window.show()
    sys.exit(app.exec())
