import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
import shutil


class CaricaReferto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Carica Referto")
        self.resize(766, 547)
        layout = QVBoxLayout()

        label = QLabel("Clicca il pulsante per caricare il Referto:", self)
        layout.addWidget(label)

        btn_carica_referto = QPushButton("Carica Referto", self)
        btn_carica_referto.clicked.connect(self.carica_referto)
        layout.addWidget(btn_carica_referto)

        self.setLayout(layout)

    def carica_referto(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Documenti (*.docx *.pdf);;Tutti i files (*.*)")

        if file_dialog.exec():
            files = file_dialog.selectedFiles()
            for file in files:
                try:
                    shutil.copy(file, "./")
                    QMessageBox.information(self, "Successo", "Referto caricato con successo!")
                except Exception as e:
                    QMessageBox.critical(self, "Errore", f"Errore durante il caricamento del referto: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaricaReferto()
    window.show()
    sys.exit(app.exec())
