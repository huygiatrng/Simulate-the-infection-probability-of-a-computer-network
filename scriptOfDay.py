import numpy as np
import distributions
import random


def spreadingVirus(array,infectedprob,nOfRun, nComp): #Attention!!!
    nInfected = 0
    nUninfected = 0
    #count number of infected computers and uninfected
    for i in range(nComp):
        if array[i]==1:
            array[i]=2
        elif array[i]==0:
            nUninfected+=1
    for i in range(nComp):
        if array[i]==2:
            nInfected += 1
    for infected in range(nInfected):
        for i in range(nComp):
            if array[i] == 0:
                if distributions.MyBernoulli(infectedprob)==1:
                     array[i]=1
    return array

def gettingFixed(array,nFixed,nOfRun,nComp):
    nInfected = 0
    nUninfected = 0
    # count number of infected computers and uninfected
    for i in range(nComp):
        if array[i] == 0:
            nUninfected += 1
        elif array[i] == 2:
            nInfected += 1
    if nInfected <nFixed:
        nFixed = nInfected
    #Random pick number of infected to fixed
    indexToFixed=random.sample(range(0, nInfected), nFixed)
    indexToFixed.sort()
    count = 0
    index = 0
    for i in range(nComp):
        if array[i]==2:
            if index >=nFixed:
                break
            elif count == indexToFixed[index]:
                index+=1
                array[i]=0
            count+=1
    return array
