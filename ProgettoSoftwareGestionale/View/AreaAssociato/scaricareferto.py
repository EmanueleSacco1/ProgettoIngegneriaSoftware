import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
import shutil


class ScaricaReferto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scarica Referto")
        self.resize(766, 547)

        layout = QVBoxLayout()

        label = QLabel("Clicca il pulsante per scaricare il Referto Ufficiale:", self)
        layout.addWidget(label)

        btn_scarica_referto = QPushButton("Scarica Referto", self)
        btn_scarica_referto.clicked.connect(self.scarica_referto)
        layout.addWidget(btn_scarica_referto)

        self.setLayout(layout)

    def scarica_referto(self):
        try:
            shutil.copy("RefertoUfficiale.doc", "./")
            QMessageBox.information(self, "Successo", "Referto scaricato con successo!")
        except FileNotFoundError:
            QMessageBox.critical(self, "Errore", "Impossibile trovare il file RefertoUfficiale.doc")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScaricaReferto()
    window.show()
    sys.exit(app.exec())
