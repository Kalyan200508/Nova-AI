import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class JarvisWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JARVIS AI")
        self.resize(900, 600)

        self.setStyleSheet("""
            QWidget{
                background-color:#10141c;
                color:white;
            }

            QTextEdit{
                background:#1a1f2b;
                border-radius:10px;
                padding:10px;
                font-size:15px;
            }

            QPushButton{
                background:#00BFFF;
                color:white;
                border:none;
                border-radius:10px;
                padding:12px;
                font-size:16px;
            }

            QPushButton:hover{
                background:#009ACD;
            }
        """)

        layout = QVBoxLayout()

        title = QLabel("JARVIS")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 30))

        layout.addWidget(title)

        self.status = QLabel("Status : Ready")
        self.status.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.status)

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        layout.addWidget(self.chat)

        self.button = QPushButton("🎤 Speak")

        layout.addWidget(self.button)

        self.setLayout(layout)


def start_gui():
    app = QApplication(sys.argv)

    window = JarvisWindow()

    window.show()

    sys.exit(app.exec())