from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Command:

    action: str

    target: Optional[str] = None

    query: Optional[str] = None


@dataclass
class Plan:

    commands: list[Command] = field(default_factory=list)