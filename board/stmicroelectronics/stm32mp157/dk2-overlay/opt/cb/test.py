import sys
import serial
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
print('Hello World')

if __name__ == '__main__':
        app = QApplication(sys.argv)
        w = QWidget()
        w.setWindowTitle('Simple')
        w.show()
        sys.exit(app.exec_())


