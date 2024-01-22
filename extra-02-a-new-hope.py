# Output on a single line the appropriate sentence with far 
# repeated N times. It must match the correct answer exactly!

# DMOJ wc15c2j1

# DMOJ submission (accepted):

x = int(input())
print('A long time ago in a galaxy' + ' far,' * (x - 1) + ' far' + ' away...')
