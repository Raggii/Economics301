def payBackFunction():
    initialCost = input("please input the initial cost of the project: ")
    amountOfYears = 0;
    runningTotal = int(initialCost);
    print("Continue to input the cash flows the program will stop automatically")
    
    while(True):
        tempYearVal = float(input("please input the cash flow: "))
        
        if((runningTotal - tempYearVal) < 0):
            
            break
        else:       
            runningTotal -= int(tempYearVal)
            print(runningTotal)
            amountOfYears += 1
    
    totalYears = amountOfYears + runningTotal/tempYearVal
    print(round(totalYears,2))
    print("\n")
    
while(True):
    
    payBackFunction()