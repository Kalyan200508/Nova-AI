from dataclasses import dataclass, field

from skills.models import Command


@dataclass
class Plan:

    commands: list[Command] = field(default_factory=list)

    def add(self, command: Command):
        self.commands.append(command)

    @property
    def empty(self):
        return len(self.commands) == 0