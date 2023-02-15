tup = tuple()
num = int(input("total numbers : "))
for y in range(num):
    x = input("enter numbers : ")
    tup = tup + (x,)
    
print("maximum value : " , max(tup))
print("minimum value : " , min(tup))
