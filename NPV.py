def npvFunction():
    initialCost = input("please input the initial cost of the project: ")
    discountRate = input("please input the discount rate in percentage: ")
    discountRateIndecimal = float(discountRate)/100
    cashFlowsYearly = []
    runningTotal = 0;
    print("If a value has () brackets around it its a negitive value \n")
    while(True):
        tempYearVal = input("please input the {}st/nd/rd year: ".format(len(cashFlowsYearly)))
        if(tempYearVal == 'q'):
            break
        else:       
            tempValNumber = int(tempYearVal)
            cashFlowsYearly.append(tempValNumber)
    
    for i in range(len(cashFlowsYearly)):
        runningTotal += cashFlowsYearly[i]/ ((1 + discountRateIndecimal) ** (i+1) )
    
    npvValue = round(runningTotal - int(initialCost),2)        
    print("NPV is equal to ${}".format(npvValue))
    if(npvValue > 0):
        print("\nUSE THIS VALUE")
    else:
        print("\nDONT USE THIS VALUE")
    print("\n")
                          

while(True):
    
    npvFunction()