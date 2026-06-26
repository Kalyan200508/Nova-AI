from skills.filesystem import filesystem

print(filesystem.create_folder("Nova_Test"))

print(filesystem.create_file("Nova_Test/readme.txt"))

print(filesystem.rename(
    "Nova_Test/readme.txt",
    "Nova_Test/info.txt"
))

print(filesystem.open_folder("Nova_Test"))