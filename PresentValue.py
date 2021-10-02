def presentValue():
    discountRate = input("What is the discount rate in percentage: ")
    discountDecimal = float(discountRate)/100
    runningTotal = 0;
    counter = 0
    while(True):
        cashFlowVal = input("input cash flow: ")
        if(cashFlowVal == 'q'):
            break
        else:
            counter += 1
            runningTotal += (int(cashFlowVal) / ((discountDecimal + 1) ** counter))
            
    
    print(runningTotal)
        
        
while(True):
    presentValue()