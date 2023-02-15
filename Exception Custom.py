class InvalidError(Exception):
    pass
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidError
    else:
        print("Eligible to Vote")
        
except InvalidError:
    print("Exception occurred: Invalid Age")