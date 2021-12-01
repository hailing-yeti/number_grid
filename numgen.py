# The Objective: Build a number grid where no value between 1 and 9 appears more than twice.
# Grid size 4 x 4

import random
import math

# Set starting values and boundaries
gridCol = int(input("Let's define a grid, please enter a number for the width:"))
gridRow = int(input("Let's define a grid, please enter a number for the length:"))

#grid = int(input("Let's define a grid, please enter a number for the length and width:"))
#take input, square for number range, then halve so we see duplication in numbers
seed = math.ceil((gridCol*gridRow)/2)
numlist = []
# rowlist = "" #unused code bit 

def new_number (seed):
  #generate a series of new numbers to the limits of the grid-size
  for i in range(seed*2):
    n = random.randint(1,seed)
    if len(numlist) < seed*2 and numlist.count(n) < 2:
      numlist.append(n)

# regenerate missing elements from the list  
  if seed*2 - len(numlist) > 0: # should equal itself out
    new_number(seed)

new_number(seed) #future change, check to see if this should be Seed*2 or just Seed
print("The number list is: ", numlist)

#build a grid, row by row
for x in range(gridCol):
  for y in range(gridRow):
    print(f"{numlist[-1]}", end=" ")
    del numlist[-1] #trimming used numbers
  print("")
