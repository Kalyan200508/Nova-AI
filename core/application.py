from gui.main_window import start_gui


class NovaApplication:

    def __init__(self):

        print("=" * 50)
        print("Starting Nova AI...")
        print("=" * 50)

    def start(self):

        print("✓ GUI")

        start_gui()


app = NovaApplication()