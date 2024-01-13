# Calculate the volume of a right circular cone.

# DMOJ dmopc14c5p1

# Working attempt

pi = 3.141592653589793
r, h = [i.strip() for i in input('Enter r, h values separated by a comma: ').split(',')]
v = (pi * (int(r) ** 2) * int(h)) / 3
print(f'{v:.3f}')

# DMOJ submission (accepted):

pi = 3.141592653589793
r = int(input())
h = int(input())
v = (pi * (int(r) ** 2) * int(h)) / 3
print(v)
