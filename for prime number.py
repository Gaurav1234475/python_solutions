Value1 = int(input ("Enter the Lowest Range Value: "))  
Value2 = int(input ("Enter the Upper Range Value: "))  
  
for number in range (Value1, Value2 + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print ("prime numbers are : " , number) 