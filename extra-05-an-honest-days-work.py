# James has a can of leftover paint, containing p litres
# When a bottlecap is covered with b litres of paint, 
# it turns into a Pokémon league-certified gym badge
# Each badge sells for d
# Output a single integer, the amount of money which 
# James will make (in Pokédollars).

# DMOJ wc18c3j1

# money = d * (p / b)

# DMOJ submission (accepted):

p = int(input())
b = int(input())
d = int(input())
remaining_paint_income = p % b

badges = p // b
badges_income = badges * d

total_income = remaining_paint_income + badges_income

print(total_income)
