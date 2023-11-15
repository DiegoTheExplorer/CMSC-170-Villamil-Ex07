from decimal import *

diabetesFp = open("diabetes.csv", "r")
diabetes = []

for line in diabetesFp:
  temp = line.split(",")
  temp = list(map(Decimal,temp))
  diabetes.append(temp)

for row in diabetes:
  for val in row:
    print(val, " ", end="")
  print("\n")
diabetesFp.close()