import json

from ai.openai_client import openai_client
from intent_ai.prompt import SYSTEM_PROMPT
from intent_ai.models import AICommand, AIResponse


class AIIntentEngine:

    def detect(self, text: str):

        if not text:
            return None

        reply = openai_client.ask(
            prompt=text,
            system_prompt=SYSTEM_PROMPT,
            temperature=0,
        )

        if not reply:
            return None

        try:

            data = json.loads(reply)

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

            return AIResponse(commands)

        except Exception as e:

            print("AI Intent Error:", e)
            print(reply)

            return None


intent_engine = AIIntentEngine()