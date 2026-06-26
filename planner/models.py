from dataclasses import dataclass
from typing import Optional


@dataclass
class Command:

    action: str

    target: Optional[str] = None

    query: Optional[str] = None