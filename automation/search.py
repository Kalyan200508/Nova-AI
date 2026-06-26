import urllib.parse
import webbrowser


class Search:

    ENGINES = {
        "google": "https://www.google.com/search?q={}",
        "youtube": "https://www.youtube.com/results?search_query={}",
        "github": "https://github.com/search?q={}",
        "wikipedia": "https://en.wikipedia.org/wiki/Special:Search?search={}",
    }

    def search(self, engine: str, query: str):

        engine = engine.lower().strip()

        if engine not in self.ENGINES:
            return False

        query = urllib.parse.quote_plus(query)

        url = self.ENGINES[engine].format(query)

        webbrowser.open(url)

        return True


search = Search()