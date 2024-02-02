"""
Write a program that reads in three weights and prints out 
the weight of Mama Bear's bowl. You may assume all weights 
are positive integers less than 100
"""

# DMOJ ccc07j1

# DMOJ submission (accepted):

bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

bowls = [bowl1, bowl2, bowl3]

bowls.sort()

print(bowls[1])
