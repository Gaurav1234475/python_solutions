num = int(input("Enter the number: "))
fact = 1
for i in range (1, num+1):
    fact = fact*i

print ("Factorial of the number %d is %d" %(num, fact))