# Determine whether a phone number belongs to a telemarketer, 
# and indicate whether we should answer the phone or ignore it.
# A phone number belongs to a telemarketer if its four digits 
# satisfy all three of the following properties:
# The first digit is 8 or 9
# The fourth digit is 8 or 9
# The second and third digits are the same
# 4 inputs (first, second, third and fourth digits of the phone
# number)

# DMOJ ccc18j1

# DMOJ submission (accepted):

one = int(input())
two = int(input())
three = int(input())
four = int(input())

strikes = 0

if one == 8 or one == 9:
    strikes += 1
if four == 8 or four == 9:
    strikes += 1
if two == three:
    strikes += 1

if strikes == 3:
    print('ignore')
else:
    print('answer')

# Learn to Code solution:
    
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
    
# if not ((num1 == 8 or num1 == 9) and
#       (num4 == 8 or num4 == 9) and
#       (num2 == num3)):
#   print('answer')
# else:
#   print('ignore')
