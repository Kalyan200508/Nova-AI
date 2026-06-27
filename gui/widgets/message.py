from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class MessageBubble(QFrame):

    def __init__(self, sender, message):
        super().__init__()

        self.setFrameShape(QFrame.NoFrame)

        layout = QVBoxLayout()

        self.sender = QLabel(sender)
        self.sender.setFont(QFont("Segoe UI", 10, QFont.Bold))

        self.message = QLabel(message)
        self.message.setWordWrap(True)
        self.message.setTextInteractionFlags(Qt.TextSelectableByMouse)

        layout.addWidget(self.sender)
        layout.addWidget(self.message)

        self.setLayout(layout)

        if sender.lower() == "you":

            self.setStyleSheet("""
                QFrame{
                    background:#1E3A5F;
                    border-radius:12px;
                    padding:10px;
                }

                QLabel{
                    color:white;
                    background:transparent;
                }
            """)

        else:

            self.setStyleSheet("""
                QFrame{
                    background:#202A36;
                    border-radius:12px;
                    padding:10px;
                }

                QLabel{
                    color:white;
                    background:transparent;
                }
            """)