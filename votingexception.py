class WrongAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        print("It is an even Number")
    if age % 2 != 0:
        print("It is an odd number")
    if age <= 0:
        raise WrongAgeError
except WrongAgeError:
    print("Invalid Age")



