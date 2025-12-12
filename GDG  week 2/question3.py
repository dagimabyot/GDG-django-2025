with open("log.txt", "w") as file:
    file.write("User logged in\n")

with open("log.txt", "r") as file:
    print(file.read())
