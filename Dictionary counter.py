import collections

myList = [1, 2, 3, 4, 1, 3, 46, 7, 2, 3, 5, 6, 10]
frequencyDict = collections.Counter(myList)
print("Input list is:", myList)
print("Frequency of elements is:")
print(frequencyDict)