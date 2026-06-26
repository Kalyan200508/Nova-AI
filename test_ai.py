from ai.openai_client import openai_client
from intent_ai.prompt import SYSTEM_PROMPT

reply = openai_client.ask(
    prompt="Could you please open Chrome and Gmail?",
    system_prompt=SYSTEM_PROMPT,
    temperature=0,
)

print(reply)