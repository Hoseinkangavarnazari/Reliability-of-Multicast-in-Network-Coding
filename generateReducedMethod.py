def reducedStateGenerator(List, TOTAL_NUMBER):
    '''Generate all possible Share (not final set or final state for PLE)'''

    ''' if multiprocessing is needed must be start at here, each round must be done with one processor'''
    counter = 0 
    if(TOTAL_NUMBER == 12):
        counter +=1
        print("Number {}".format(counter))
    
    answerSets = []
    if(len(List) == 1):
        answerSets.append([TOTAL_NUMBER])
    else:
        for i in range(TOTAL_NUMBER+1):
            CurrentState = [i]
            allPossibleSet = reducedStateGenerator(
                List[0:len(List)-1], TOTAL_NUMBER - i)

            for tempSet in allPossibleSet:
                answerSets.append(tempSet + CurrentState)

    return answerSets


if __name__ == "__main__":
    NUMBER_OF_SYMBOLS = 5
    NUMBER_OF_TOTAL_TRANSMISSION = 19

    NUMBER_OF_RECEIVER = 13
    test = reducedStateGenerator([0 for i in range(
        NUMBER_OF_SYMBOLS, NUMBER_OF_TOTAL_TRANSMISSION + 1)], NUMBER_OF_RECEIVER)
    print("here")
