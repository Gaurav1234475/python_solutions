def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string
str = "PythonFreshers"
print("The reverse string is : ", reverse(str))