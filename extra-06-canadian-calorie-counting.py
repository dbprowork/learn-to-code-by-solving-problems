"""
The program should input a number for each type of item then 
calculate and display the Calorie total. The first line will 
be the customer's choice of burger, the second will be the 
choice of side, then drink, then dessert. You may assume that 
each input will be a number from 1 to 4. That is, each 
customer has to pick exactly one number from each of the four 
options out of each of the four categories.
"""

# DMOJ ccc06j1

# DMOJ solution (accepted):

burger = {1: 461,
          2: 431,
          3: 420,
          4: 0}

drink = {1: 130,
         2: 160,
         3: 118,
         4: 0}

side = {1: 100,
        2: 57,
        3: 70,
        4: 0}

dessert = {1: 167,
           2: 266,
           3: 75,
           4: 0}

b = int(input())
s = int(input())
dr = int(input())
de = int(input())

print(f'Your total Calorie count is {burger[b] + side[s] + drink[dr] + dessert[de]}.')
