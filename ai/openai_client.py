import os
from dotenv import load_dotenv

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

load_dotenv()


class OpenAIClient:

    def __init__(self):

        self.api_key = os.getenv("NVIDIA_API_KEY")

        if OpenAI is None:
            print("OpenAI package is not installed.")
            self.client = None
            return

        if not self.api_key:
            print("NVIDIA_API_KEY not found.")
            self.client = None
            return

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=self.api_key,
        )

    def ask(
        self,
        prompt: str,
        system_prompt: str = "You are Nova, an intelligent desktop AI assistant.",
        temperature: float = 0.3,
        model: str = "meta/llama-3.3-70b-instruct",
        max_tokens: int = 1024,
    ):

        if self.client is None:
            return None

        try:

            response = self.client.chat.completions.create(
                model=model,
                temperature=temperature,
                top_p=0.7,
                max_tokens=max_tokens,
                stream=False,
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
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"[NVIDIA API ERROR] {e}")
            return None


openai_client = OpenAIClient()