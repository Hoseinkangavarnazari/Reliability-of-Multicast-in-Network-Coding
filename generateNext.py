

def nextPossibleSet(totalTransmition, stateSet):
    #numberOfReceivers
    L = len(stateSet)
    N = totalTransmition
    flag = False
    i = 0
    while True:
        if(stateSet[i] < N):
            flag = True
            stateSet[i] += 1
            
            # if you want to remove lots of states easily 
            # instead zeroing elemets, make them symbol size
            for j in range(0, i):
                stateSet[j] = 0
            break
        else:
            if(i<L-1):
                i += 1
            else:
                break

    if flag == True:
        return stateSet
    else:
         return False

def validateSet(numberOfSymbols,nextSet):
    for i in range (0,len(nextSet)):
        if(nextSet[i] < numberOfSymbols):
            return False
    return True

if __name__ == "__main__":
    print(nextPossibleSet(5,[5]))

    totalTransmition = 10
    numberOfSymbols = 10
    numberOfReceivers = 5
    currentState = [numberOfSymbols for i in range(0,numberOfReceivers)]
    answer = 10

    while(currentState != False):
        temp = nextPossibleSet(totalTransmition,currentState)
        if(validateSet(numberOfSymbols,temp)):
            print(temp)
            #run Thatapp

            # add the answer
            a = 2
        else:
            print(temp)
            currentState = temp

    