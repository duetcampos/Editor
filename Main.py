import sys
from PyQt5.QtWidgets import QApplication
from texteditorWindow import EditorWindow

app = QApplication(sys.argv)
textEditor = EditorWindow()
app.exec()