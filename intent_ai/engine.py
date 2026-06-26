import json

from ai.openai_client import openai_client
from intent_ai.prompt import SYSTEM_PROMPT
from intent_ai.models import AICommand, AIResponse


class AIIntentEngine:

    def detect(self, text: str):

        if not text:
            return None

        response = openai_client.ask(
            prompt=text,
            system_prompt=SYSTEM_PROMPT,
            temperature=0,
        )

        if not response:
            return None

        try:

            data = json.loads(response)

            commands = []

            for item in data.get("commands", []):

                commands.append(
                    AICommand(
                        action=item.get("action"),
                        target=item.get("target"),
                        query=item.get("query"),
                        count=item.get("count"),
                    )
                )

            return AIResponse(commands=commands)

        except Exception as e:

            print(f"[AI Intent] {e}")

            print(response)

            return None


intent_engine = AIIntentEngine()