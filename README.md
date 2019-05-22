### The implementation of Reliability of Multicast under RLNC

There are two methods to calculate the reliability (Single and Multiprocess Method)
- Multi processor model
- Single processor model


#### Single processor model
for receivers less than 6 it's better to use the probabilityFunction method.

#### Multi processor Model
If you want to calculate more than 10 receivers it's better to use the Multiprocessor method. open the 
multiprocessor.py and change the configuration in the main section

 ```
  if __name__ == "__main__":
    # configuration
    FIELD_SIZE = 2
    NUMBER_OF_TOTAL_TRANSMISSION_SET = [[5,11,12], [6,10,14], [7,9,13], [8,15]]
    NUMBER_OF_RECEIVERS = 6
    NUMBER_OF_SYMBOLS = 5
    ERROR_RATE = 0.1
    PROCESS_NUMBER = [1,2,3,4]
  ```

  
  if your CPU has less than 4 core change the number of the processors:
  
```

p1 = multiprocessing.Process(target=calculationSegment, args=(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION_SET[0], NUMBER_OF_RECEIVERS,
                                                            NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER[0],))
p2 = multiprocessing.Process(target=calculationSegment, args=(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION_SET[1], NUMBER_OF_RECEIVERS,
                                                            NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER[1],))
p3 = multiprocessing.Process(target=calculationSegment, args=(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION_SET[2], NUMBER_OF_RECEIVERS,
                                                            NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER[2],))
p4 = multiprocessing.Process(target=calculationSegment, args=(FIELD_SIZE, NUMBER_OF_TOTAL_TRANSMISSION_SET[3], NUMBER_OF_RECEIVERS,
                                                            NUMBER_OF_SYMBOLS, ERROR_RATE, PROCESS_NUMBER[3],))
```
