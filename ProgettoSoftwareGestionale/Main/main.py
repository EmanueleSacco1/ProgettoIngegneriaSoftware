import sys

from PyQt6.QtWidgets import QApplication
from ProgettoSoftwareGestionale.View import vistahome

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = vistahome()
    vista_home.show()
    sys.exit(app.exec())