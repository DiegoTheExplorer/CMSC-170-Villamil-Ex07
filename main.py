#Name: Diego Miguel M. Villamil
#Section: CMSC 170 WX-3L

from decimal import *
from math import sqrt

def sort_key(nghbr):
  return nghbr[1]

def sort_class(fv):
  return fv[len(fv) - 1]

kinp = int(input("Please enter the value for k: "))
kNearest = []
dataset = []
input = []
distList = []
output = []

fpDb = open("debug.txt", "w")
temp = "Value for k: " + str(kinp) + "\n"
fpDb.write(temp)
fpDb.close()

fp = open("diabetes.csv", "r")
for line in fp: #Read the data from dataset .csv
  temp = line.split(",")
  temp = list(map(Decimal,temp))
  dataset.append(temp)
fp.close()

dataset.sort(key = sort_class, reverse = True)
numClasses = int(dataset[0][len(dataset[0]) - 1] + 1)

fp = open("input.in", "r")
for line in fp: #Read the data from input.in
  temp = line.split(",")
  temp = list(map(Decimal,temp))
  input.append(temp)

dlen = len(dataset)
inplen = len(input)

for i in range(0,inplen): #Loop through each feature vector in input
  distList.clear()
  kNearest.clear()
  kn = kinp
  classes = []
  for j in range(0,numClasses):
    classes.append(0)

  for j in range(0,dlen): #Loop through each feature vector in dataset
    dist = 0
    for k in range(0,(len(input[0]))): # Calculate the distance of feature vector input[i] to dataset[j]
      dist += abs(input[i][k] - dataset[j][k]) ** 2
    dist = sqrt(dist)
    distList.append((j,dist)) #appends a tupple where (index in dataset, distance to feat vector input[i])
  
  distList.sort(key = sort_key) 

  fpDb = open("debug.txt", "a") 
  temp = "input feature vector: " + str(tuple(list(map(float, input[i])))) + "\n"
  fpDb.write(temp)#Writes the current feature vector from input being classified
  for k in range(0,kn):
    temp = str(tuple(list(map(float,dataset[distList[k][0]]))))
    txtOut = temp + ", distance: " +  str(distList[k][1]) + "\n"
    fpDb.write(txtOut)#Writes the kth nearest to input [i]

    for j in range(0,numClasses):
      if(dataset[distList[k][0]][8] == j):
        classes[j] += 1
    classSet = set(classes)

  if(len(classes) != len(classSet)): #Breaking ties by looking at the next nearest neighbor
    temp = str(tuple(list(map(float,dataset[distList[k][0]]))))
    txtOut = temp + ", distance: " +  str(distList[k][1]) + "\n"
    fpDb.write(txtOut)

    for j in range(0,numClasses):
      if(dataset[distList[kn][0]][8] == j):
        classes[j] += 1
    
    classSet = set(classes)
    kn += 1
    
  temp = input[i].copy()
  temp.append(classes.index(max(classes)))
  
  fpDb.close()
  
  output.append(temp)
  dataset.append(output[i])
  

fp = open("output.txt", "w") #write the data in output to output.txt
for i in range(0, len(output)):
  for j in range(0, len(output[0]) - 1):
    temp = str(output[i][j]) + ","
    fp.write(temp)
  temp = str(output[i][len(output[0]) - 1]) + "\n"
  fp.write(temp)
fp.close()