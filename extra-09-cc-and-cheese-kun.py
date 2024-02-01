# C.C. will be absolutely satisfied if the pizza she gets has a 
# width of 3 units and an extra-cheesiness of at least 95 %
# C.C. will be fairly satisfied if the pizza she gets has a 
# width of 1 unit and an extra-cheesiness of at most 50 %
# C.C. will be very satisfied with any other pizza she receives

# DMOJ dmopc16c1p0

# DMOJ submission (accepted):

width = int(input())
x_cheese = int(input())

if width == 3 and x_cheese >= 95:
    s = 'absolutely'
elif width == 1 and x_cheese <= 50:
    s = 'fairly'
else:
    s = 'very'

print(f'C.C. is {s} satisfied with her pizza.')
