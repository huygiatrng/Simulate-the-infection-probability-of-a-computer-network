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
    while ncomp < 0:
        print("Please enter a valid number of computer!")
        ncomp = enterAndCheckInput(1)
    if ncomp == 0:
        ncomp = 20
    prob = float(enterAndCheckInput(2))/100
    while prob < 0:
        print("Please enter a valid percentage of computer infected!")
        prob = float(enterAndCheckInput(2))/100
    if prob == 0:
        prob = 0.1
    nFixed = enterAndCheckInput(3)
    while nFixed < 0:
        print("Please enter a valid number of computers repaired daily!")
        nFixed = enterAndCheckInput(3)
    if nFixed == 0:
        nFixed = 5
    nOfRun = enterAndCheckInput(4)
    while nOfRun < 0:
        print("Please enter a valid number of iterations!")
        nOfRun = enterAndCheckInput(4)
    if nOfRun == 0:
        nOfRun = 10000
    return [ncomp,prob,nFixed,nOfRun]

