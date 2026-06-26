from memory.session import session


class Context:

    def set_app(self, app):
        session.set("active_app", app)

    def get_app(self):
        return session.get("active_app")

    def set_project(self, project):
        session.set("active_project", project)

    def get_project(self):
        return session.get("active_project")

    def set_task(self, task):
        session.set("active_task", task)

    def get_task(self):
        return session.get("active_task")


context = Context()
