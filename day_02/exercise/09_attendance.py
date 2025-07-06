attendee_names = []

attendee_count = int(input("Attendee count: "))

for count in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.append(attendee_name)

print(attendee_names)

name = input("What is your name?: ")
print("You are no.: ", attendee_names.index(name))

attendee_names.remove("Jayson")
print(attendee_names)

late_attendee = attendee_names.pop(attendee_count-2)
print("Late attendee is: ", late_attendee)
print(attendee_names)

