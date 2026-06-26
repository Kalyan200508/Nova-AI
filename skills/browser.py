import webbrowser


class BrowserSkill:

    URLS = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
        "wikipedia": "https://wikipedia.org",
        "linkedin": "https://linkedin.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "x": "https://x.com",
    }

    def open(self, website):

        website = website.lower().strip()

        if website not in self.URLS:
            return None

        try:

            webbrowser.open(self.URLS[website])

            return f"Opening {website.title()}."

        except Exception as e:

            return str(e)

    def google_search(self, query):

        try:

            url = (
                "https://www.google.com/search?q="
                + query.replace(" ", "+")
            )

            webbrowser.open(url)

            return f"Searching Google for {query}."

        except Exception as e:

            return str(e)

    def youtube_search(self, query):

        try:

            url = (
                "https://www.youtube.com/results?search_query="
                + query.replace(" ", "+")
            )

            webbrowser.open(url)

            return f"Searching YouTube for {query}."

        except Exception as e:

            return str(e)


browser = BrowserSkill()