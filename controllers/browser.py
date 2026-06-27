from browser.web import browser


class BrowserController:

    def handle(self, text):

        lower = text.lower().strip()

        # Open websites
        if lower.startswith("open "):

            site = lower.replace("open ", "", 1).strip()

            reply = browser.open(site)

            if reply:
                return reply

        # Google Search
        if lower.startswith("search google for "):

            query = text[len("search google for "):]

            return browser.search_google(query)

        # YouTube Search
        if lower.startswith("search youtube for "):

            query = text[len("search youtube for "):]

            return browser.search_youtube(query)

        # GitHub Search
        if lower.startswith("search github for "):

            query = text[len("search github for "):]

            return browser.search_github(query)

        # StackOverflow Search
        if lower.startswith("search stackoverflow for "):

            query = text[len("search stackoverflow for "):]

            return browser.search_stackoverflow(query)

        return None


browser_controller = BrowserController()