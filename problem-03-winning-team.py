"""
Count number of successful three-point (inputs 1 and 4), 
two-point (inputs 2 and 5), and one-point plays 
(inputs 3 and 6) to get a total for each team 
(based on 6 total inputs)
Team with the highest points wins the game
"""

# DMOJ ccc19j1

# DMOJ submission (accepted):

tA3p = int(input()) * 3
tA2p = int(input()) * 2
tA1p = int(input())
tB3p = int(input()) * 3
tB2p = int(input()) * 2
tB1p = int(input())

tAt = tA3p + tA2p + tA1p
tBt = tB3p + tB2p + tB1p

if tAt > tBt:
    print('A')
elif tBt > tAt:
    print('B')
else:
    print('T')
