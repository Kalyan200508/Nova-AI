import webbrowser
from urllib.parse import quote_plus


class Browser:

    WEBSITES = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "linkedin": "https://www.linkedin.com",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "reddit": "https://www.reddit.com",
        "stackoverflow": "https://stackoverflow.com",
        "x": "https://x.com",
        "twitter": "https://x.com",
    }

    def open(self, website):

        website = website.lower().strip()

        if website not in self.WEBSITES:
            return None

        webbrowser.open(self.WEBSITES[website])

        return f"Opening {website.title()}."

    def search_google(self, query):

        url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        webbrowser.open(url)

        return f"Searching Google for '{query}'."

    def search_youtube(self, query):

        url = (
            "https://www.youtube.com/results?search_query="
            + quote_plus(query)
        )

        webbrowser.open(url)

        return f"Searching YouTube for '{query}'."

    def search_github(self, query):

        url = (
            "https://github.com/search?q="
            + quote_plus(query)
        )

        webbrowser.open(url)

        return f"Searching GitHub for '{query}'."

    def search_stackoverflow(self, query):

        url = (
            "https://stackoverflow.com/search?q="
            + quote_plus(query)
        )

        webbrowser.open(url)

        return f"Searching Stack Overflow for '{query}'."


browser = Browser()