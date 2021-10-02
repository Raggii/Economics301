def finalValue():
    print("Are you using real or nominal percentages!! \n")
    discountRate = input("What is the discount rate in percentage: ")
    discountDecimal = float(discountRate)/100
    runningTotalList = [];
    runningTotal = 0;
    while(True):
        cashFlowVal = input("input cash flow: ")
        if(cashFlowVal == 'q'):
            break
        else:
            runningTotalList.append(int(cashFlowVal))
        
    for i in range(len(runningTotalList)):
        runningTotal += runningTotalList[i] * ((1 + discountDecimal) ** (len(runningTotalList) - (i+1)))
    
    print(runningTotal)

print("Remember when the payments start!!!!\n")
while(True):
    finalValue()