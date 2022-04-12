import os
import scriptOfDay
from matplotlib import pyplot as plt
import statistics
import graphdata

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def enterAndCheckInput(n):
    checkInput = True
    while checkInput == True:
        if n==1:
            data = input("Enter number of computers: ")
            while int(data)<0:
                print("Invalid value!")
                data = input("Enter number of computers: ")
        elif n==2:
            data = input("Enter percentage of computer infected(%): ")
            while int(data)<0:
                print("Invalid value!")
                data = input("Enter percentage of computer infected(%): ")
        elif n==3:
            data = input("Enter number of computers repaired daily: ")
            while int(data)<0:
                print("Invalid value!")
                data = input("Enter number of computers repaired daily: ")
        elif n==4:
            data = input("Enter number of iterations: ")
            while int(data)<0:
                print("Invalid value!")
                data = input("Enter number of iterations: ")
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
    nOfRun = enterAndCheckInput(4)
    if nOfRun == 0:
        nOfRun = 10000
    return [ncomp,prob,nFixed,nOfRun]


cls()
print("Default:\n     number of computers:20, percentage of computer infected:10%, number of computers repaired daily:5, number of literations: 10000\n     (*)You can use default values by entering 0 as their inputs.\n-----------------------------------------------------------------------------------------------------")
ncomp,prob,nFixed,nOfRun = enterInput()
cls()
print("\n")

#Create a list has nOfRun of numperOfComputer (nComp)
#Let 0= uninfected, 1 = infected

dayToFinish = []

infectedAtLeastOnceList = []

expectedInfectedComputerList = []

print("Simulating...")

for iters in range(nOfRun):
    list = [0] * ncomp
    list[0] = 1
    #print("Iteration:",iters)
    beInfectedAtLeastOnce = [0] * ncomp
    daycount = 1
    countInfectedPerday = []                        #list of number of computers are infected in everyday.
    while list.count(1)!=0:
        #morning
        list = scriptOfDay.spreadingVirus(list, prob, ncomp)
        # check if computers were infected at least one.
        beInfectedAtLeastOnce = scriptOfDay.beInfectedAtleastOnceList(list, beInfectedAtLeastOnce)
        # compute number of computers are infected:
        countInfectedPerday.append(list.count(1))                       #number of computers are infected.
        #evening
        list = scriptOfDay.gettingFixed(list, nFixed, ncomp)
        daycount += 1
    probInfectedAtLeastOnce = beInfectedAtLeastOnce.count(1)/ncomp
    infectedAtLeastOnceList.append(probInfectedAtLeastOnce)
    expected = statistics.mean(countInfectedPerday)
    expectedInfectedComputerList.append(expected)
    dayToFinish.append(daycount)
    #Print time to finish in this loop
    #print("Finished in ",daycount," days.")

cls()
#Print the results
print("A. Average day to fix all:", statistics.mean(dayToFinish))
print("B. Probability that each computer gets infected at least once: ",statistics.mean(infectedAtLeastOnceList))
print("C. The expected number of computers that get infected:", statistics.mean(expectedInfectedComputerList))


#Show the histogram of days to finish of literations.
graphdata.histogramData(dayToFinish,0)
#-----------------------------------------------------------------------------
#graphdata.histogramData(infectedAtLeastOnceList,1)
#-----------------------------------------------------------------------------
#graphdata.histogramData(expectedInfectedComputerList,2)
