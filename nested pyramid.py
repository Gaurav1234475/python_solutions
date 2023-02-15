print("Pyramid Pattern of Stars (*): ")
for i in range(10):
    for s in range(-11, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()