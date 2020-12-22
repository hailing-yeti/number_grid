import random

seed = 16
grid = 4
numlist = []
rowlist = ""

def new_number (repeat):
  #generate a series of new numbers
  for n in range(repeat):
    numlist.append(random.randint(1,9))
  
  for r in numlist:
    #check for and remove duplicate numbers
    if numlist.count(r) > 2:
      #print(r, "appears", numlist.count(r), "times.")
      #print("removing extra")
      numlist.remove(r)
  
  if seed - len(numlist) > 0:
    new_number(seed-len(numlist))

new_number(seed)
print("")
print("The number list is: ", numlist)

#build a grid, row by row
for x in range(grid):
  global rowlist
  rowlist += "{}"
  print(rowlist.format(numlist[:grid]))
  del numlist[:grid] #trimming used numbers