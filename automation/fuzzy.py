from difflib import get_close_matches


class FuzzyMatcher:

    APPS = [
        "chrome",
        "edge",
        "notepad",
        "calculator",
        "paint",
        "vscode",
        "github",
        "youtube",
        "gmail",
        "google",
        "whatsapp",
        "instagram",
        "facebook",
        "linkedin",
    ]

    def match(self, word: str):

        word = word.lower().strip()

        if word in self.APPS:
            return word

        match = get_close_matches(
            word,
            self.APPS,
            n=1,
            cutoff=0.55,
        )

        if match:
            return match[0]

        return word


fuzzy = FuzzyMatcher()