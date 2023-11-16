#Name: Diego Miguel M. Villamil
#Section: CMSC 170 WX-3L

from decimal import *
from math import sqrt

def sort_key(nghbr):
  return nghbr[1]

kinp = int(input("Please enter the value for k: "))
kNearest = []
diabetes = []
input = []
distList = []
output = []

fpDb = open("debug.txt", "w")
temp = "Value for k: " + str(kinp) + "\n"
fpDb.write(temp)
fpDb.close()

fp = open("diabetes.csv", "r")
for line in fp: #Read the data from diabetes .csv
  temp = line.split(",")
  temp = list(map(Decimal,temp))
  diabetes.append(temp)
fp.close()

fp = open("input.in", "r")
for line in fp: #Read the data from input.in
  temp = line.split(",")
  temp = list(map(Decimal,temp))
  input.append(temp)

dlen = len(diabetes)
inplen = len(input)

for i in range(0,inplen): #Loop through each feature vector in input
  distList.clear()
  kNearest.clear()
  kn = kinp
  diabetic = 0
  nondiabetic = 0

  for j in range(0,dlen): #Loop through each feature vector in diabetes
    dist = 0
    for k in range(0,(len(input[0]))): # Calculate the distance of feature vector input[i] to diabetes[j]
      dist += abs(input[i][k] - diabetes[j][k]) ** 2
    dist = sqrt(dist)
    distList.append((j,dist)) #appends a tupple where (index in diabetes, distance to feat vector input[i])
  
  distList.sort(key = sort_key) 

  fpDb = open("debug.txt", "a") 
  temp = "input feature vector: " + str(tuple(list(map(float, input[i])))) + "\n"
  fpDb.write(temp)#Writes the current feature vector from input being classified
  for k in range(0,kn):
    temp = str(tuple(list(map(float,diabetes[distList[k][0]]))))
    txtOut = temp + ", distance: " +  str(distList[k][1]) + "\n"
    fpDb.write(txtOut)#Writes the kth nearest to input [i]

    if (diabetes[distList[k][0]][8] == 0):
      nondiabetic += 1
    else:
      diabetic += 1

  while(diabetic == nondiabetic): #Breaking ties by looking at the next nearest neighbor
    temp = str(tuple(list(map(float,diabetes[distList[k][0]]))))
    txtOut = temp + ", distance: " +  str(distList[k][1]) + "\n"
    fpDb.write(txtOut)
    if (diabetes[kn][8] == 0):
      nondiabetic += 1
    else:
      diabetic += 1
    kn += 1
  
  fpDb.close()

  if(diabetic > nondiabetic): #classifies the current feature vector input[i]
    temp = input[i].copy()
    temp.append(1)
  elif(nondiabetic > diabetic):
    temp = input[i].copy()
    temp.append(0)
  
  output.append(temp)
  diabetes.append(output[i])
  

fp = open("output.txt", "w") #write the data in output to output.txt
for i in range(0, len(output)):
  for j in range(0, len(output[0]) - 1):
    temp = str(output[i][j]) + ","
    fp.write(temp)
  temp = str(output[i][len(output[0]) - 1]) + "\n"
  fp.write(temp)
fp.close()