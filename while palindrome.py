num = int(input('Enter the number: '))

rev = 0
number = num
while(num != 0):
   rem = num % 10
   rev = rev * 10 + rem
   num = int(num / 10)

if(number == rev):
   print(number,'is a Palindrome')
else:
   print(number,'is not a Palindrome')