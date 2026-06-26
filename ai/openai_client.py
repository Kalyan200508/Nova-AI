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

    def ask(
        self,
        prompt,
        system_prompt=None,
        temperature=0.7,
    ):

        if self.client is None:
            return None

        if system_prompt is None:

            system_prompt = (
                "You are Nova, a friendly, intelligent desktop AI assistant. "
                "Be concise, accurate, and conversational."
            )

        try:

            response = self.client.chat.completions.create(

                model="gpt-4.1-mini",

                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],

                temperature=temperature,

            )

            return response.choices[0].message.content

        except Exception as e:

            print(f"OpenAI Error: {e}")

            return None


openai_client = OpenAIClient()