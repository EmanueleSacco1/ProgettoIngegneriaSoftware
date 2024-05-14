import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
import shutil


class CaricaCertificatoMedico(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Carica Certificato Medico")
        self.resize(766, 547)

        layout = QVBoxLayout()

        label = QLabel("Clicca il pulsante per caricare il Certificato Medico:", self)
        layout.addWidget(label)

        btn_carica_certificato = QPushButton("Carica Certificato", self)
        btn_carica_certificato.clicked.connect(self.carica_certificato)
        layout.addWidget(btn_carica_certificato)

        self.setLayout(layout)

    def carica_certificato(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Documenti (*.docx *.pdf);;Tutti i files (*.*)")

        if file_dialog.exec():
            files = file_dialog.selectedFiles()
            for file in files:
                try:
                    shutil.copy(file, "./")
                    QMessageBox.information(self, "Successo", "Certificato caricato con successo!")
                except Exception as e:
                    QMessageBox.critical(self, "Errore", f"Errore durante il caricamento del certificato: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaricaCertificatoMedico()
    window.show()
    sys.exit(app.exec())
