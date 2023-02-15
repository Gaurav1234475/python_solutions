X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] * Y[i][j]

for r1 in result:
   print(r1)

for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
    result[i][j] = X[j][i]
for r2 in result:
   print(r2)

for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
    result[i][j] = Y[j][i]
for r3 in result:
   print(r3)
