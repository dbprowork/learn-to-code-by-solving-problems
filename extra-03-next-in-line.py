# The difference in ages between the middle child and youngest 
# child is the same as the difference in ages between the oldest
# child and the middle child.
# Given the ages of the youngest and middle children, what is 
# the age of the oldest child?

# DMOJ ccc13j1

# DMOJ submission (accepted):

x = int(input())
y = int(input())

d = y - x

o = y + d

print(o)
