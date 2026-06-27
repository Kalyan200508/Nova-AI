import re


class CommandParser:

    def split(self, text):

        text = text.strip()

        parts = re.split(
            r"\s+(?:and then|then|and)\s+",
            text,
            flags=re.IGNORECASE,
        )

        return [
            part.strip()
            for part in parts
            if part.strip()
        ]


command_parser = CommandParser()