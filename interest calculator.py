# calculator to evaluate interest gained yearly

initialInvestment = float(input(print("Enter initial investment amount")))
rate = float(input(print("enter interest rate"))) / 100
rate2 = rate * 100
yearsInvested = float(input(print("how many years will interest be earned for?")))
currYear = 0
currTotal = 0
interest = 0
# calculations begin

while True:
    if yearsInvested >= currYear:
        currYear = currYear + 1
        interest = initialInvestment * rate
        currTotal = initialInvestment + interest

        print("$", initialInvestment, " with an interest rate of ", rate2, " % over ", currYear, " year(s) "
                                                                                                "= $", currTotal)
        initialInvestment = currTotal
    else:
        input(print("Press 'enter' to exit"))
        break


