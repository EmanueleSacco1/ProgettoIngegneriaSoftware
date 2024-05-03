from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

finestra = QWidget()
finestra.setWindowTitle("Accesso area riservata")
finestra.show()

sys.exit(app.exec())