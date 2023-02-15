try:
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    print("Result of Division: " + str(a/b))
# except block handling division by zero
except(ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")
# except block handling wrong value type
except(ValueError):
    print("You must enter integer value")
# generic except block
except:
    print("Oops! Something went wrong!")