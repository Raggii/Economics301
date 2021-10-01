def npvValueFinder(annualCashFlow, lengthOfCashFlow):
    # SAME as NPV just to get a starting point
    initialRunningTotal = [];
    
    for i in range(lengthOfCashFlow):
        initialRunningTotal.append(annualCashFlow)  
     
    #print(checkTotal)
    return initialRunningTotal

def changePerYearIrr():
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
    return cashFlowsYearly


def irrFunciton():
    initialInvest = int(input("Enter initial investment: "))
    typeOfInput = int(input("what type of input: Constant over Years '0' or Changing per Year '1': "))

    if(typeOfInput == 0):
        annualCashFlow = int(input("Enter the annual cash flow: "))
        lengthOfCashFlow = int(input("How many years is the cash flow for: "))
    
    rateOfReturn = input("please input the rate of return in percentage: ")
    print("\n")
    
    discountRateIndecimal = float(rateOfReturn)/100
    returnList = []
    checkTotalClosest = 0;
    if(typeOfInput == 0): # now both return the list of cash flows so calc is only needed to be done once
        returnList = npvValueFinder(annualCashFlow, lengthOfCashFlow)
    else:
        returnList = changePerYearIrr()
    
    for i in range(len(returnList)):
        checkTotalClosest += returnList[i]/ ((1 + discountRateIndecimal) ** (i+1) )
    
    checkTotalClosest -= initialInvest
    #print(checkTotalClosest)   
    
    #Now we have to iterate to find value cloest to 0
    iterateValue = 0
    if(checkTotalClosest > 0):
        # we want to iterate downwards
        # moves up or down by 0.1%
        iterateValue = 0.001
    else:
        iterateValue = -0.001
    
    
    
    bestPercentageVal = discountRateIndecimal
    counter = 0
    
    while(True):
        checkTotal = 0
        discountRateIndecimal += iterateValue # moves it down by .1% every iteration
        #print(discountRateIndecimal)
        for i in range(len(returnList)):
            checkTotal += returnList[i]/ ((1 + discountRateIndecimal) ** (i+1) )
        checkTotal -= initialInvest
        #print(checkTotal)
        if(abs(checkTotal) < abs(checkTotalClosest)):
            checkTotalClosest = checkTotal
            bestPercentageVal = discountRateIndecimal
        else:
            break
            
    print("The closest percentage is {}%\n".format(round(bestPercentageVal * 100,2)))  
    
    
while(True):
    irrFunciton()