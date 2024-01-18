"""
The first line of input contains the integer N
The second and third lines of input contain N characters each
The second line of input records the information about 
yesterday's parking spaces, and the third line of input 
records the information about today's parking spaces. Each 
of these 2 N characters will either be C to indicate an 
occupied space or to indicate it was an empty parking space
"""

# DMOJ ccc18j2

# DMOJ submission (accepted):

# spots = int(input())
# day1 = input().upper()
# day2 = input().upper()

# same = 0

# for s in range(spots):
#     if day1[s] == 'C':
#         if day1[s] == day2[s]:
#             same += 1

# print(same)

# Improved version

spots = int(input())
day1 = input().upper()
day2 = input().upper()

same = 0

for s in range(spots):
    if day1[s] == 'C' and day2[s] == 'C':
        same += 1

print(same)
