import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class VisualizzaGara(QWidget):
    def __init__(self, gara):
        super().__init__()
        self.setWindowTitle("Visualizza Gara")
        self.resize(766, 547)

        self.gara_accettata = False

        layout = QVBoxLayout()

        self.label_gara = QLabel(f"Gara Assegnata: {gara}", self)
        self.label_gara.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_gara)

        self.accept_button = QPushButton("Accetta Gara", self)
        self.accept_button.clicked.connect(self.accetta_gara)
        layout.addWidget(self.accept_button)

        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self.gara_accettata:
            painter.setBrush(QColor("green"))
        else:
            painter.setBrush(QColor("red"))

        painter.drawEllipse(150, 100, 50, 50)

    def accetta_gara(self):
        self.gara_accettata = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gara_assegnata = "Nome della gara assegnata"
    window = VisualizzaGara(gara_assegnata)
    window.show()
    sys.exit(app.exec())

# Il bottone rosso è spostato, poi vedi te come posizionarlo meglio