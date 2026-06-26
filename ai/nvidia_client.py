import os

from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()


class NVIDIAClient:

    def __init__(self):

        api_key = os.getenv("NVIDIA_API_KEY")

        if not api_key:
            self.client = None
            print("NVIDIA_API_KEY not found.")
            return

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key,
        )

        self.model = "meta/llama-3.3-70b-instruct"

    def ask(
        self,
        prompt,
        system_prompt="You are Nova, a helpful desktop AI assistant.",
        temperature=0.2,
        max_tokens=1024,
    ):

        if self.client is None:
            return None

        try:

            response = self.client.chat.completions.create(
                model=self.model,
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
                top_p=0.7,
                max_tokens=max_tokens,
                stream=False,
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print("NVIDIA Error:", e)
            return None


nvidia_client = NVIDIAClient()