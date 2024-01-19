# DMOJ coci16c1p1

#DMOJ submission (accepted):

MBs = int(input())
months = int(input())

carry = MBs

for i in range(months):
    carry += (MBs - int(input()))

print(carry)
