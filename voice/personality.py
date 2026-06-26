import random
from datetime import datetime


class Personality:

    def format(self, text: str):

        if not text:
            return text

        lower = text.lower().strip()

        # -----------------------------
        # Greetings
        # -----------------------------

        if lower.startswith("hello"):

            hour = datetime.now().hour

            if hour < 12:
                return random.choice([
                    "Good morning, Kalyan! I'm Nova. How can I help you today?",
                    "Morning, Kalyan! Ready to begin your day?",
                ])

            elif hour < 18:
                return random.choice([
                    "Good afternoon, Kalyan! What can I do for you?",
                    "Hello, Kalyan! How's your day going?",
                ])

            else:
                return random.choice([
                    "Good evening, Kalyan. It's nice to hear from you.",
                    "Welcome back, Kalyan. What shall we do tonight?",
                ])

        # -----------------------------
        # Opening Apps
        # -----------------------------

        if lower.startswith("opening"):

            app = text.replace("Opening", "").replace(".", "").strip()

            return random.choice([
                f"Sure! Opening {app} for you.",
                f"Absolutely! Launching {app}.",
                f"Done! Opening {app}.",
                f"No problem. Starting {app}.",
            ])

        # -----------------------------
        # Search
        # -----------------------------

        if lower.startswith("searching"):

            return random.choice([
                text,
                "Sure! " + text,
                "Absolutely! " + text,
                "One moment. " + text,
            ])

        # -----------------------------
        # Time
        # -----------------------------

        if lower.startswith("the current time"):

            return text.replace(
                "The current time is",
                "It's"
            )

        # -----------------------------
        # Unknown
        # -----------------------------

        if "don't know" in lower:

            return random.choice([
                "I'm not sure about that yet.",
                "I don't know the answer just yet, but I'm learning.",
                "That's something I still need to learn.",
            ])

        return text


personality = Personality()