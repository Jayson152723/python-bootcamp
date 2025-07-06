with open("test.txt", "w") as file:

    names = ["Mia Anderson\n", "Ethan Roberts\n", "Liam Johnson\n", "Sophia Martinez\n", "Olivia Davis\n", "Noah Thompson\n"]
    for name in names:
        file.write(name)

    file.write("Alex Freze")


