#first calc the NPV of a system

initialCost = int(input("What is the initial cost: "))
workingLifeTime = int(input("How many years: "))
annualMatenance = int(input("How much does it cost to run per year: "))
percentageOppCost = int(input("Opportunity cost: "))
decimalOppCost = float(percentageOppCost)/100

# initial + annuity
annuityVal = annualMatenance*((1/percentageOppCost - (1/(percentageOppCost*(1+percentageOppCost)**workingLifeTime))))

print(annuityVal + initialCost)

#WORK IN PROGRESS