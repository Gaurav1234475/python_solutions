def fibonacciGenerator():
    a=0
    b=1
    for i in range(6):
        yield b
        a,b= b,a+b

obj = fibonacciGenerator()
 
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))