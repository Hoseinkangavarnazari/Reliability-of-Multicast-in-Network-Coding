def reducedStateGenerator(List, TOTAL_NUMBER):
    '''Generate all possible Share (not final set or final state for PLE)'''

    answerSets = []
    if(len(List) == 1):
        # make 10 array and each array fill with 0 to total transmissions
        # [[0], [1], [2], [3]]
        for i in range(TOTAL_NUMBER+1):
            answerSets.append([i])

    for i in range(TOTAL_NUMBER+1):
        CurrentState = [i]
        allPossibleSet = reducedStateGenerator(
            List[0:len(List)-1], TOTAL_NUMBER - i)
        
        for tempSet in allPossibleSet:
            answerSets.append(tempSet + CurrentState)
            
    return [[],[]]


if __name__ == "__main__":
    pass
