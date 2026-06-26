import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class OpenAIClient:

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

        if OpenAI is not None and self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None

    def ask(self, prompt):

        if self.client is None:
            return None

        try:

            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are Jarvis, an intelligent personal AI assistant.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
            )

            return response.choices[0].message.content

        except Exception as e:
            print(e)
            return None


openai_client = OpenAIClient()
