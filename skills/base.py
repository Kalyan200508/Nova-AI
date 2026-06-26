from abc import ABC, abstractmethod


class Skill(ABC):

    name = ""

    @abstractmethod
    def can_handle(self, command):
        pass

    @abstractmethod
    def execute(self, command):
        pass