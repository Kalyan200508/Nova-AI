from memory.session import session

session.set("browser", "chrome")
session.set("project", "Nova")

print(session.get("browser"))
print(session.get("project"))
print(session.all())
