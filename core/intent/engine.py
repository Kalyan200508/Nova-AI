from dataclasses import dataclass
import re


@dataclass
class Intent:

    domain: str
    action: str
    target: str | None = None
    value: str | None = None
    query: str |None = None


class IntentEngine:

    def detect(self, text):

        lower = text.lower().strip()

        # ---------------------------------
        # Browser Search
        # ---------------------------------

        if lower.startswith("search "):

            return Intent(
                domain="browser",
                action="search",
                query=text,
            )

        # ---------------------------------
        # Open Commands
        # ---------------------------------

        if re.match(r"^(open|launch|start|run)\s+", lower):

            target = re.sub(
                r"^(open|launch|start|run)\s+",
                "",
                lower,
            ).strip()

            websites = {
                "google",
                "youtube",
                "gmail",
                "github",
                "chatgpt",
                "facebook",
                "instagram",
                "linkedin",
                "reddit",
                "stackoverflow",
                "twitter",
                "x",
            }

            if target in websites:

                return Intent(
                    domain="browser",
                    action="open",
                    target=target,
                )

            return Intent(
                domain="launcher",
                action="open",
                target=target,
            )

        # ---------------------------------
        # System Commands
        # ---------------------------------

        if re.search(
            r"(volume|battery|screen ?shot|screenshot|lock|shutdown|restart|sleep|mute|unmute)",
            lower,
        ):

            return Intent(
                domain="system",
                action="system",
                target=text,
            )

        # ---------------------------------
        # AI
        # ---------------------------------

        return Intent(
            domain="ai",
            action="chat",
            query=text,
        )


intent_engine = IntentEngine()