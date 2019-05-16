# importing the multiprocessing module
import multiprocessing
import time
from console_progressbar import ProgressBar
from cal import PLEcalculator
from generateNext import nextPossibleSet, validateSet


def calculationSegment(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION, NUMBER_OF_RECEIVERS,
                                                NUMBER_OF_SYMBOLS, ERROR_RATE, VALID_CURRENT_STATE_OF_RECEIVERS):

    filename = "/multiProcessorResult/Receivers_" + \
        str(NUMBER_OF_RECEIVERS)+"_errorRate_"+str(ERROR_RATE)+".txt"
    f = open(filename, "w+")
    # NoTT iterates between elements of the Number of total transmission for example [7,9]
    for NoTT in NUMBER_OF_TOTAL_TRANSMISSION:

        tempAnswer=coreCalculation(FIELD_SIZE, NoTT, NUMBER_OF_RECEIVERS,
                                                NUMBER_OF_SYMBOLS, ERROR_RATE, VALID_CURRENT_STATE_OF_RECEIVERS)
        print(tempAnswer)
        f.write("[" + str(NUMBER_OF_TOTAL_TRANSMISSION) +
                ","+str(tempAnswer) + "]" + "\n")
    f.close() 
    return
    
def coreCalculation(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION, NUMBER_OF_RECEIVERS,
                                                NUMBER_OF_SYMBOLS, ERROR_RATE, VALID_CURRENT_STATE_OF_RECEIVERS):

    currentState = [NUMBER_OF_SYMBOLS for i in range(0, NUMBER_OF_RECEIVERS)]
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
    return tempAnswer


def print_square(num):
    # while True:
    #     a = 12
    #     b = a**a ** a
    #     a = b
    #     a = 0
    print(num)
    pb = ProgressBar(total=100,prefix='Here', suffix='Now', decimals=3, length=50, fill='X', zfill='-')
    pb.print_progress_bar(2)
    time.sleep(1)
    pb.print_progress_bar(25)
    time.sleep(1)
    pb.print_progress_bar(50)
    time.sleep(5)
    pb.print_progress_bar(95)
    time.sleep(5)
    pb.print_progress_bar(100)


if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(11, ))
    p2 = multiprocessing.Process(target=print_square, args=(12, ))
    p3 = multiprocessing.Process(target=print_square, args=(13, ))
    p4 = multiprocessing.Process(target=print_square, args=(14, ))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # starting process 3
    p3.start()
    # starting process 4
    p4.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
    # wait until process 3 is finished
    p3.join()
    # wait until process 4 is finished
    p4.join()

    # both processes finished
    print("Done!")
