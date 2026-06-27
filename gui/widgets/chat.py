from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QFrame,
)

from gui.widgets.message import MessageBubble


class ChatWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("ChatWidget")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setFrameShape(QFrame.NoFrame)

        self.container = QWidget()

        self.chat_layout = QVBoxLayout(self.container)
        self.chat_layout.setContentsMargins(10, 10, 10, 10)
        self.chat_layout.setSpacing(12)

        # Push messages to the top
        self.chat_layout.addStretch()

        self.scroll.setWidget(self.container)

        self.main_layout.addWidget(self.scroll)

        self.setStyleSheet("""
        QWidget#ChatWidget{
            background:#10141c;
        }

        QScrollArea{
            border:none;
            background:#10141c;
        }

        QScrollBar:vertical{
            width:8px;
            background:#10141c;
        }

        QScrollBar::handle:vertical{
            background:#3c4b63;
            border-radius:4px;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical{
            height:0px;
        }
        """)

    def add_user_message(self, text):

        bubble = MessageBubble("You", text)

        self.chat_layout.insertWidget(
            self.chat_layout.count() - 1,
            bubble,
        )

        self.scroll.verticalScrollBar().setValue(
            self.scroll.verticalScrollBar().maximum()
        )

    def add_nova_message(self, text):

        bubble = MessageBubble("Nova", text)

        self.chat_layout.insertWidget(
            self.chat_layout.count() - 1,
            bubble,
        )

        self.scroll.verticalScrollBar().setValue(
            self.scroll.verticalScrollBar().maximum()
        )

    def clear_chat(self):

        while self.chat_layout.count() > 1:

            item = self.chat_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()