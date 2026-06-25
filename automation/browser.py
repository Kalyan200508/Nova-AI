import webbrowser


class Browser:

    WEBSITES = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "whatsapp": "https://web.whatsapp.com",
        "linkedin": "https://www.linkedin.com",
        "x": "https://x.com",
        "twitter": "https://x.com",
    }

    def open(self, name):

        name = name.lower().strip()

        if name not in self.WEBSITES:
            return False

        webbrowser.open(self.WEBSITES[name])
        return True


browser = Browser()