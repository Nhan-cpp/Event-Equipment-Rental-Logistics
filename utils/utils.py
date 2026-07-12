# def validate_ID(ID):
#     if not ID:
#         return False

#     for character in ID:
#         if not character.isalnum():
#             return False

#     return True

# def validate_positiveValue(value, fieldName):
#     if value <= 0:
#         print(f"{fieldName} must be greater than 0")
#         return False

#     return True

# def validate_expectedReturnTime(startTime, expectedReturnTime):
#     if expectedReturnTime <= startTime:
#         print("Expected return time must be after start time")
#         return False

#     return True


def input_value(message, converter, validator, fieldName):
    while True:
        try:
            value = input(f"{message} {fieldName}: ",end = "")
            value = converter(value)

            if validator(value):
                return value

        except ValueError:
            print("Invalid input format")

from datetime import datetime

def input_startTime():
    while True:
        try:
            print("Enter start time (dd/mm/yyyy HH:MM): ", end="")
            value = input()
            startTime = datetime.strptime(value, "%d/%m/%Y %H:%M")
            return startTime

        except ValueError:
            print("Invalid date and time format")

from datetime import datetime

def input_expectedReturnTime(startTime):
    while True:
        try:
            print("Enter expected return time (dd/mm/yyyy HH:MM): ", end="")
            value = input()
            expectedReturnTime = datetime.strptime(value, "%d/%m/%Y %H:%M")

            if validate_expectedReturnTime(startTime, expectedReturnTime):
                return expectedReturnTime

        except ValueError:
            print("Invalid date and time format")


