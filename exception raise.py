try:
    k = int(input("Enter Marks: "))
    if(not(k>=0 and k<=100)):
        raise Exception('Invalid Marks: Must Be Between 0 and 100')
    print("your Marks: ",k)
except Exception as e:
    print(e)