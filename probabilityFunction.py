from cal import PLEcalculator
from generateNext import nextPossibleSet, validateSet

if __name__ == "__main__":
    # configuration
    FIELD_SIZE = 2
    NUMBER_OF_TOTAL_TRANSMISSION = 10
    NUMBER_OF_RECEIVERS = 5
    NUMBER_OF_SYMBOLS = 10
    ERROR_RATE = 0.01
    errorSet = [ ERROR_RATE for i in range (0,NUMBER_OF_RECEIVERS)]
    tempstate = [NUMBER_OF_SYMBOLS for i in range(0,NUMBER_OF_RECEIVERS)]
    CURRENT_STATE_OF_RECEIVERS= 
