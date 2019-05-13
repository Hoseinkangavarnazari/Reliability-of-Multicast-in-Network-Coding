from cal import PLEcalculator
from generateNext import nextPossibleSet, validateSet
# from drawplot import makePlot

if __name__ == "__main__":
    # configuration
    FIELD_SIZE = 2
    # NUMBER_OF_TOTAL_TRANSMISSION = 6
    NUMBER_OF_RECEIVERS = 10
    NUMBER_OF_SYMBOLS = 5
    ERROR_RATE = 0.01
    # INITIALSTATE = [NUMBER_OF_SYMBOLS for i in range(0, NUMBER_OF_RECEIVERS)]
    INITIALSTATE = [5,5]
    CURRENT_STATE_OF_RECEIVERS = INITIALSTATE 


    while(NUMBER_OF_RECEIVERS < 30):
        filename = "Receivers"+str(NUMBER_OF_RECEIVERS)+"errorRate"+str(ERROR_RATE)+".txt"
        f = open(filename, "w+")

        for NUMBER_OF_TOTAL_TRANSMISSION in range(NUMBER_OF_SYMBOLS, 15+1):

            currentState = [NUMBER_OF_SYMBOLS for i in range(0, NUMBER_OF_RECEIVERS)]
            print(currentState)
            tempAnswer = 0
            while(currentState != False):

                if(validateSet(NUMBER_OF_SYMBOLS, currentState)):
                    # print(temp)
                    # run Thatapp
                    VALID_CURRENT_STATE_OF_RECEIVERS = currentState

                    # add the answer
                    tempAnswer += PLEcalculator(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION, NUMBER_OF_RECEIVERS,
                                                NUMBER_OF_SYMBOLS, ERROR_RATE, VALID_CURRENT_STATE_OF_RECEIVERS)

                    currentState = nextPossibleSet(
                    # print(currentState)
                        NUMBER_OF_TOTAL_TRANSMISSION, currentState)
                else:
                    # print(temp)
                    currentState = nextPossibleSet(
                        NUMBER_OF_TOTAL_TRANSMISSION, currentState)


            print(tempAnswer)
            f.write("[" + str(NUMBER_OF_TOTAL_TRANSMISSION) +
                    ","+str(tempAnswer) + "]" + "\n")
        f.close() 
        NUMBER_OF_RECEIVERS +=10
    # we want to calculate it for
    # for each NUMBER_OF_TOTAL_TRANSMISSION [5:15] make a point and push it in to the array
    # push it into the array
    # give that array and make the plot here
