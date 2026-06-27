from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class StatusWidget(QLabel):

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)

        self.set_status("Ready")

        self.setStyleSheet("""
            QLabel{
                color:#00BFFF;
                font-size:18px;
                padding:10px;
                background:transparent;
            }
        """)

    def set_status(self, status):

        icons = {
            "Ready": "🟢",
            "Listening": "🎤",
            "Thinking": "🤔",
            "Speaking": "🗣",
            "Sleeping": "💤",
            "Error": "⚠",
        }

        icon = icons.get(status, "🟢")

        self.setText(f"{icon} {status}")