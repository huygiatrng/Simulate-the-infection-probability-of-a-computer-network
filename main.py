import distributions
import os
import numpy as np
import random
import scriptOfDay
from matplotlib import pyplot as plt

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def enterAndCheckInput(n):
    checkInput = True
    while checkInput == True:
        if n==1:
            data = input("Enter number of computers ")
        elif n==2:
            data = input("Enter percentage of computer infected:(%)")
        elif n==3:
            data = input("Enter number of computers repaired daily:")
        try:
            returndata = int(data)
            checkInput = False
        except ValueError:
            print("Invalid value!")
    return returndata

def enterInput():

    ncomp = enterAndCheckInput(1)
    if ncomp == 0:
        ncomp = 20
    prob = float(enterAndCheckInput(2))/100
    if prob == 0:
        prob = 0.1
    nFixed = enterAndCheckInput(3)
    if nFixed == 0:
        nFixed = 5
    return [ncomp,prob,nFixed]

cls()
print("Default:\n     number of computers:20, percentage of computer infected:10%, number of computers repaired daily:5\n     (*)You can use default values by entering 0 as their inputs.\n-----------------------------------------------------------------------------------------------------")
arrayInput = enterInput()
print(arrayInput)
cls()
#Number of run:
nOfRun = 10000
print("\n")

#Create a array has nOfRun of numperOfComputer (nComp)
#Let 0= uninfected, 1 = will infected, 2 = infected
array_2d = np.zeros((nOfRun, arrayInput[0]))
for i in range(nOfRun):
    array_2d[i][0]=2
#print(array_2d)

checkAllofArray = np.count_nonzero(array_2d ==0)
#print(checkAllofArray)
dayCount = 0
dayToFinishFullFix = np.zeros((nOfRun,1))
countFinished = 0
while checkAllofArray<arrayInput[0]*nOfRun:
    checkNUninfected = np.count_nonzero(array_2d ==0, axis=1)
    dayCount+=1
    print("\nDay: ",dayCount," -----------------")
    for i in range(nOfRun):
        if checkNUninfected[i]!=arrayInput[0]:
            #Now run everyday script
            array_2d[i] = scriptOfDay.spreadingVirus(array_2d[i],arrayInput[1],nOfRun,arrayInput[0])
            array_2d[i] = scriptOfDay.gettingFixed(array_2d[i], arrayInput[2], nOfRun, arrayInput[0])
        else:
            if dayToFinishFullFix[i]==0:
                countFinished +=1
                dayToFinishFullFix[i] = dayCount
                #print(dayToFinishFullFix[i])
                print(countFinished)
    checkAllofArray = np.count_nonzero(array_2d == 0)

plt.hist(dayToFinishFullFix)
plt.show()

print("Average day to fix all:",np.mean(dayToFinishFullFix))