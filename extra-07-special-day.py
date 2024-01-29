# The input consists of two integers each on a separate line
# These integers represent a date in 2015
# The first line will contain the month, which will be an 
# integer in the range from 1 (indicating January) to 12 
# (indicating December)
# The second line will contain the day of the month, which 
# will be an integer in the range from 1 to 31 . You can 
# assume that the day of the month will be valid for the 
# given month

# DMOJ ccc15j1

# DMOJ submission (accepted):

month = int(input())
day = int(input())

if month == 2 and day == 18:
    print('Special')
elif month == 2 and day < 18:
    print('Before')
elif month == 2 and day > 18:
    print('After')
elif month < 2:
    print('Before')
else:
    print('After')
