import re


class CommandParser:

    def split(self, text):

        text = text.strip()

        if not text:
            return []

        separators = (
            r"\s+(?:and then|then|after that|afterwards|and)\s+"
        )

        commands = re.split(
            separators,
            text,
            flags=re.IGNORECASE,
        )

        cleaned = []

        for command in commands:

            command = command.strip()

            if command:
                cleaned.append(command)

        return cleaned


command_parser = CommandParser()