import re  
  
# Example String 
s = """hii my name is jack and my number is 7999564 and my email address is jack@gmail.com, check it out check it out http://tinyurl.com"""

lst1 = re.findall('[0-9]+', s)    
lst2 = re.findall('\S+@\S+', s) 
lst3 = re.findall(r'(https?://\S+)', s)

print(lst1)
print(lst2)
print(lst3)