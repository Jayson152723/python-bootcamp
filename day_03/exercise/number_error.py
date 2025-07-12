class NotANumber(ValueError):
    pass
class NotPositive(ValueError):
    pass
class NotWithinRange(ValueError):
    pass

user_input = input("Enter a number from 1 to 100: ")

# check if valid number
if not user_input.isnumeric() and not user_input[1:].isnumeric():
    raise NotANumber

# check if positive
number = int(user_input)
if number < 0:
    raise NotPositive()

# check if within range
if not (1 <= number <= 100):
    raise NotWithinRange