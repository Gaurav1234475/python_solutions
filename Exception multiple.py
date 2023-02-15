mylist = [-1, 2, 0, 4, 0]

for i in mylist:
    # Python catch multiple exceptions
    try:
        print("thedivision is:", 10/i)

    except:
        # raise an error
        print("Error occurs while dividing")