from planner.models import Plan
from planner.parser import parser


class Planner:

    def plan(self, text):

        result = parser.parse(text)

        if result is None:
            return Plan()

        if isinstance(result, list):
            return Plan(commands=result)

        return Plan(commands=[result])


planner = Planner()