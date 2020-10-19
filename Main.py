import sys
from PyQt5.QtWidgets import QApplication
from texteditorWindow import EditorWindow
from PyQt5.QtWidgets import QStyleFactory
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor

qApp = QApplication(sys.argv)
#qApp.setStyle(QStyleFactory.create("Fusion"))
#pal = QPalette()
#pal.setColor(QPalette.Window, QColor(53,53,53))
#pal.setColor(QPalette.Button, QColor(53,53,53))
#pal.setColor(QPalette.Highlight, QColor(142,45,197))
#pal.setColor(QPalette.ButtonText, QColor(255,255,255))
#pal.setColor(QPalette.WindowText, QColor(255,255,255))
#qApp.setPalette(pal)
textEditor = EditorWindow()
qApp.exec()