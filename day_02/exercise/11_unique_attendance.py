attendee_names = set()

attendee_count = int(input("Attendee count: "))

for count in range(attendee_count):
    name = input("Enter name: ")
    attendee_names.add(name)

print(attendee_names)

attendee_names.discard("Jayson")

print(attendee_names)

print(attendee_names.pop())
