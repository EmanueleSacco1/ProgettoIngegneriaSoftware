import sys
import pickle
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton


class VisualizzaStoricoGare(QWidget):
    def __init__(self, storico_gare):
        super().__init__()
        self.setWindowTitle("Visualizza Storico Gare")
        self.resize(766, 547)


        layout = QVBoxLayout()

        label = QLabel("Storico Gare:", self)
        layout.addWidget(label)

        for gara in storico_gare:
            label_gara = QLabel(gara, self)
            layout.addWidget(label_gara)

        btn_indietro = QPushButton("Torna Indietro", self)
        btn_indietro.clicked.connect(self.close)
        layout.addWidget(btn_indietro)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #Carica i dati dal file .pickle
    try:
        with open('storico_gare.pickle', 'rb') as file:
            storico_gare = pickle.load(file)
    except FileNotFoundError:
        storico_gare = []

    window = VisualizzaStoricoGare(storico_gare)
    window.show()
    sys.exit(app.exec())
