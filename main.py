import os
import scriptOfDay
from matplotlib import pyplot as plt
import statistics
import graphdata
import basicFunc


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
print("Default:\n     number of computers:20, percentage of computer infected:10%, number of computers repaired daily:5, number of literations: 10000\n     (*)You can use default values by entering 0 as their inputs.\n-----------------------------------------------------------------------------------------------------")
ncomp,prob,nFixed,nOfRun = basicFunc.enterInput()
cls()
print("\n")

#Create a list has nOfRun of numperOfComputer (nComp)
#Let 0= uninfected, 1 = infected

dayToFinish = []
expectedInfectedComputerList = []
sumLoopEachCompInfectedAtLeastOnce = 0

print("Simulating...")

for loop in range(nOfRun):
    list = [0] * ncomp
    list[0] = 1
    #print("Iteration:",loop)
    beInfectedAtLeastOnce = [0] * ncomp
    daycount = 0
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
    if beInfectedAtLeastOnce.count(1)==ncomp:
        sumLoopEachCompInfectedAtLeastOnce +=1
    expected = statistics.mean(countInfectedPerday)
    expectedInfectedComputerList.append(expected)
    dayToFinish.append(daycount)
    #Print time to finish in this loop
    #print("Finished in ",daycount," days.")
    #Print unusual cases:

    if daycount > 1000:
        print("Iteration:",loop)
        print("Finished in ",daycount," days.")

cls()
#Print the results
print("\nA. Average day to fix all:", statistics.mean(dayToFinish), " day(s).")
print("B. Probability that each computer gets infected at least once: ",sumLoopEachCompInfectedAtLeastOnce/nOfRun)
print("C. The expected number of computers that get infected:", statistics.mean(expectedInfectedComputerList))

#Show the histogram of days to finish of literations.
graphdata.histogramData(dayToFinish,0)
