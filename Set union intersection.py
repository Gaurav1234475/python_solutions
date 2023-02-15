Set1 = {2, 4, 6, 8}
Set2 = {1, 2, 5, 9, 6}
 
# find the union and intersection of two arrays 
#using bitwise operators

x = list(set(Set1) | set(Set2))
y= list(set(Set1) & set(Set2))
 

print('Union of the arrays:',x)
print('intersection of the arrays:',y)