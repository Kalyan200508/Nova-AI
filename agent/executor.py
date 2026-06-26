from agent.models import Result
from skills.filesystem import filesystem


class AgentExecutor:

    def execute(self, goal):

        results = []

        for task in goal.tasks:

            action = task.action

            data = task.data

            try:

                if action == "CREATE_FOLDER":

                    message = filesystem.create_folder(
                        data["name"]
                    )

                elif action == "CREATE_FILE":

                    message = filesystem.create_file(
                        data["path"]
                    )

                else:

                    message = f"Unknown action: {action}"

                task.status = "completed"

                results.append(
                    Result(
                        success=True,
                        message=message,
                    )
                )

            except Exception as e:

                task.status = "failed"

                results.append(
                    Result(
                        success=False,
                        message=str(e),
                    )
                )

        goal.completed = True

        return results


executor = AgentExecutor()