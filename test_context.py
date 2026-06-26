from memory.context import context

context.set_app("chrome")
context.set_project("Nova")
context.set_task("Coding")

print(context.get_app())
print(context.get_project())
print(context.get_task())