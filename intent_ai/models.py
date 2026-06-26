from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AICommand:

    action: str

    target: Optional[str] = None

    query: Optional[str] = None

    count: Optional[int] = None


@dataclass
class AIResponse:

    commands: list[AICommand] = field(default_factory=list)