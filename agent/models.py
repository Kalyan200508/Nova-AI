from dataclasses import dataclass, field


@dataclass
class Task:

    action: str

    data: dict = field(default_factory=dict)

    status: str = "pending"


@dataclass
class Goal:

    text: str

    tasks: list[Task] = field(default_factory=list)

    completed: bool = False

    def add(self, task: Task):

        self.tasks.append(task)


@dataclass
class Result:

    success: bool

    message: str