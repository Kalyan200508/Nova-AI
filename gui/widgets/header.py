from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel


class Header(QLabel):

    def __init__(self):
        super().__init__()

        self.setText("NOVA AI")

        self.setAlignment(Qt.AlignCenter)

        self.setFont(QFont("Segoe UI", 28, QFont.Bold))

        self.setStyleSheet("""
            QLabel{
                color:white;
                padding:20px;
                background:transparent;
            }
        """)