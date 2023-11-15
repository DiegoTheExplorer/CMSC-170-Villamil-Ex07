from decimal import *
from math import sqrt

def sort_key(nghbr):
  return nghbr[1]

kn = 4
kNearest = []
diabetes = []
input = []
distList = []
output = []

fp = open("diabetes.csv", "r")
for line in fp: #Read the data from diabetes .csv
  temp = line.split(",")
  temp = list(map(Decimal,temp))
  diabetes.append(temp)
fp.close()

#prints the data in diabetes
# for row in diabetes:
#   for val in row:
#     print(val, " ", end="")
#   print("\n")

fp = open("input.in", "r")
for line in fp: #Read the data from input.in
  temp = line.split(",")
  temp = list(map(Decimal,temp))
  input.append(temp)

#prints the data in input
# for row in input:
#   for val in row:
#     print(val, " ", end="")
#   print("\n")

dlen = len(diabetes)
inplen = len(input)

for i in range(0,inplen): #Loop through each feature vector in input
  distList.clear()
  kNearest.clear()
  kn = 4
  diabetic = 0
  nondiabetic = 0

  for j in range(0,dlen): #Loop through each feature vector in diabetes
    dist = 0
    for k in range(0,(len(input[0]) - 1)): # Calculate the distance of feature vector input[i] to diabetes[j]
      dist += sqrt(abs(input[i][k] - diabetes[j][k]) ** 2)
    distList.append((j,dist))
  
  distList.sort(key = sort_key)

  for k in range(0,k):
    if (diabetes[distList[k][0]][8] == 0):
      nondiabetic += 1
    else:
      diabetic += 1

  while(diabetic == nondiabetic): #Breaking ties by looking at the next nearest neighbor
    if (diabetes[kn][8] == 0):
      nondiabetic += 1
    else:
      diabetic += 1
    kn += 1

  if(diabetic > nondiabetic):
    temp = input[i].copy()
    temp.append(1)
  elif(nondiabetic > diabetic):
    temp = input[i].copy()
    temp.append(0)
  
  output.append(temp)
  diabetes.append(output[i])
  
for row in output:
  for val in row:
    print(val," ", end="")
  print("\n")