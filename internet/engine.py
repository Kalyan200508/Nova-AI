from internet.providers import provider


class InternetEngine:

    def search(self, query: str):

        result = provider.search(query)

        if result:
            return result

        return None


internet_engine = InternetEngine()