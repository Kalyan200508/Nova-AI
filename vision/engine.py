import easyocr

from automation.screen import screen
from ai.openai_client import openai_client
from vision.prompt import VISION_PROMPT


class VisionEngine:

    def __init__(self):

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False,
        )

    def read_screen(self):

        image = screen.screenshot()

        result = self.reader.readtext(image)

        text = []

        for item in result:
            text.append(item[1])

        return "\n".join(text)

    def describe_screen(self):

        text = self.read_screen()

        if not text.strip():
            return "I couldn't detect any text on the screen."

        reply = openai_client.ask(
            prompt=text,
            system_prompt=VISION_PROMPT,
            temperature=0.2,
        )

        return reply


vision = VisionEngine()