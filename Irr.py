def npvValueFinder(initialInvest, annualCashFlow, lengthOfCashFlow, discountRateIndecimal):
    # SAME as NPV just to get a starting point
    initialRunningTotal = 0;
    
    for i in range(lengthOfCashFlow):
        initialRunningTotal += annualCashFlow/ ((1 + discountRateIndecimal) ** (i+1) )    
     
    
    checkTotal = round(initialRunningTotal - initialInvest,2)  
    #print(checkTotal)
    return checkTotal


def irrFunciton():
    initialInvest = int(input("Enter initial investment: "))
    annualCashFlow = int(input("Enter the annual cash flow: "))
    lengthOfCashFlow = int(input("How many years is the cash flow for: "))
    
    rateOfReturn = input("please input the rate of return in percentage: ")
    discountRateIndecimal = float(rateOfReturn)/100
    
    checkTotalClosest = npvValueFinder(initialInvest, annualCashFlow, lengthOfCashFlow, discountRateIndecimal)
    
    #Now we have to iterate to find value cloest to 0
    iterateValue = 0
    if(checkTotalClosest > 0):
        # we want to iterate downwards
        # moves up or down by 0.5%
        iterateValue = 0.005
    else:
        iterateValue = -0.005
        
    bestPercentageVal = discountRateIndecimal
    counter = 0;
    while(True):
        discountRateIndecimal += iterateValue # moves it down by 1% every iteration
        checkTotal = npvValueFinder(initialInvest, annualCashFlow, lengthOfCashFlow, discountRateIndecimal)
        if(abs(checkTotal) < abs(checkTotalClosest)):
            checkTotalClosest = checkTotal
            bestPercentageVal = discountRateIndecimal
        else:
            break
            
    print("The closest percentage is {}%\n".format(round(bestPercentageVal * 100,1)))  
    
    
while(True):
    irrFunciton()