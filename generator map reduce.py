#Map_Function

def squared(num):
  return num**2

num_list = [1,2,3,4,5,6]

# using the map function to create this new list of squared values
square = list(map(squared, num_list))
  
print(square)

#Filter_Function

def is_even(num):
  return num % 2 == 0


nums = [1,2,3,4,5,6]

# new list that will contain only the even numbers from list_of_nums
even = list(filter(is_even, nums))

print(even)