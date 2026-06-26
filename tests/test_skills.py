from skills.models import Command
from skills.registry import registry


print()

reply = registry.execute(
    Command(
        action="OPEN",
        target="notepad",
    )
)

print(reply)

print()

reply = registry.execute(
    Command(
        action="GOOGLE_SEARCH",
        query="python programming",
    )
)

print(reply)

print()

reply = registry.execute(
    Command(
        action="YOUTUBE_SEARCH",
        query="AI tutorial",
    )
)

print(reply)