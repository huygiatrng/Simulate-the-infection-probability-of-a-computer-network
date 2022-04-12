import distributions
import random


def spreadingVirus(list,infectedprob, nComp):
    nInfected = list.count(1)
    for infected in range(nInfected):
        for i in range(nComp):
            if list[i] == 0:
                if distributions.MyBernoulli(infectedprob)==1:
                    list[i]=1
    return list

def gettingFixed(list,nFixed,nComp):
    nInfected = list.count(1)
    for i in range(nComp):
        if list[i] == 2:
            nInfected += 1
    if nInfected <nFixed:
        nFixed = nInfected
    #Random pick number of infected to fixed
    indexToFixed = random.sample(range(0, nInfected), nFixed)
    indexToFixed.sort()
    count = 0
    index = 0
    for i in range(nComp):
        if list[i]==1:
            if index >=nFixed:
                break
            elif count == indexToFixed[index]:
                index+=1
                list[i]=0
            count+=1
    return list

def beInfectedAtleastOnceList(list,answer):
    for i in range(len(list)):
        if list[i]==1:
            answer[i]=1
    return answer

