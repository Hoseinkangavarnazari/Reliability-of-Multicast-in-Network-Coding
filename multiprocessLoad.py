# importing the multiprocessing module
import logging
import multiprocessing
import time
from console_progressbar import ProgressBar
from cal import PLEcalculator
from generateNext import nextPossibleSet, validateSet


''' the logger configuration steps'''
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="./log.out",
                    level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


def calculationSegment(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION, NUMBER_OF_RECEIVERS,
                       NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER):

    filename = ".\multiProcessorResult\Receivers_" + \
        str(NUMBER_OF_RECEIVERS)+"_errorRate_"+str(ERROR_RATE) + \
        "_processNumber_"+str(PROCESS_NUMBER)+".txt"
    f = open(filename, "w+")
    # NoTT iterates between elements of the Number of total transmission for example [7,9]
    for NoTT in NUMBER_OF_TOTAL_TRANSMISSION:

        tempAnswer = coreCalculation(FIELD_SIZE, NoTT, NUMBER_OF_RECEIVERS,
                                     NUMBER_OF_SYMBOLS, ERROR_RATE)
        print("Process ", PROCESS_NUMBER, "Finished NoTT",
              NoTT, " Output:", tempAnswer)
        f.write("[" + str(NoTT) +
                ","+str(tempAnswer) + "]" + "\n")
    f.close()

    print("Process ", PROCESS_NUMBER, "Finished the job.")

    return


def coreCalculation(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION, NUMBER_OF_RECEIVERS,
                    NUMBER_OF_SYMBOLS, ERROR_RATE):

    ''' Making valid sets for each transmission'''

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
    pb = ProgressBar(total=100, prefix='Here', suffix='Now',
                     decimals=3, length=50, fill='X', zfill='-')
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
    # configuration
    FIELD_SIZE = 2
    # NUMBER_OF_TOTAL_TRANSMISSION_SET = [[5,11,12], [6,9,15], [7,10,14], [8,13]]
    NUMBER_OF_TOTAL_TRANSMISSION_SET = [
        [5, 11, 12], [6, 10, 14], [7, 9, 13], [8, 15]]
    NUMBER_OF_RECEIVERS = 15
    NUMBER_OF_SYMBOLS = 5
    ERROR_RATE = 0.1
    PROCESS_NUMBER = [1, 2, 3, 4]

    processStrings = "Process {} started"
    # creating processes
    p1 = multiprocessing.Process(target=calculationSegment, args=(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION_SET[0], NUMBER_OF_RECEIVERS,
                                                                  NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER[0],))
    p2 = multiprocessing.Process(target=calculationSegment, args=(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION_SET[1], NUMBER_OF_RECEIVERS,
                                                                  NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER[1],))
    p3 = multiprocessing.Process(target=calculationSegment, args=(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION_SET[2], NUMBER_OF_RECEIVERS,
                                                                  NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER[2],))
    p4 = multiprocessing.Process(target=calculationSegment, args=(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION_SET[3], NUMBER_OF_RECEIVERS,
                                                                  NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER[3],))

    # starting process 1
    logger.info(processStrings.format(1))
    p1.start()
    # starting process 2

    logger.info(processStrings.format(2))
    p2.start()

    # starting process 3
    logger.info(processStrings.format(3))
    p3.start()

    # starting process 4
    logger.info(processStrings.format(4))
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
