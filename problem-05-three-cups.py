"""
Output the index of the cup under which the ball is: 1 if it 
is under the left cup, 2 if it is under the middle cup or 3 
if it is under the right cup
"""

# DMOJ coci06c5p1

# DMOJ submission (accepted):

pos = ['x', 'o', 'o']

pattern = input().upper()

for i in pattern:
    if i == 'A':
        pos[0], pos[1] = pos[1], pos[0]
    if i =='B':
        pos[1], pos[2] = pos[2], pos[1]
    if i =='C':
        pos[0], pos[2] = pos[2], pos[0]

print(pos.index('x') + 1)
