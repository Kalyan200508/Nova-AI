import requests


class InternetProvider:

    def search(self, query: str):

        url = "https://api.duckduckgo.com/"

        params = {
            "q": query,
            "format": "json",
            "no_html": 1,
            "skip_disambig": 1,
        }

        try:
            response = requests.get(
                url,
                params=params,
                timeout=10,
            )

            response.raise_for_status()

            data = response.json()

            if data.get("AbstractText"):
                return data["AbstractText"]

            related = data.get("RelatedTopics", [])

            for item in related:

                if isinstance(item, dict):

                    if item.get("Text"):
                        return item["Text"]

            return None

        except Exception as e:

            print(e)

            return None


provider = InternetProvider()