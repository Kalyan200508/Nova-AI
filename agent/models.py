from dataclasses import dataclass, field


@dataclass
class Task:

    action: str

    target: str = ""

    query: str = ""


@dataclass
class Plan:

    tasks: list[Task] = field(default_factory=list)