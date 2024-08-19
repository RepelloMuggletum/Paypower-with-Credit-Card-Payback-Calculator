spend = float(input("How much you will approxiamatly to reload the PayPower Card per month?"))

AMF = 12.99 #American Express Cobalt® card monthly fee
PMF = 4.95 # PayPower reloadable monthly maintenance fee
RLF = 6.95 # PayPower reload fee per time 
BPF = 1.95 # PayPower bill payment fee per time

if spend <= 30000/12: #AMEX Cobalt Cap is $30000 per year

    cost_fix = AMF + PMF # Monthly fix cost to hold two accounts 
    cost_var = RLF * spend/500 +BPF * spend/1000 # Monthly Variable cost to reload and pay the 3rd Credit Card bill
    cost = cost_fix + cost_var

    AMEX_value = float(input("What is your estimate value for one AMEX Cobalt point Value in CAD cents ?"))/100

    AMEX_return = AMEX_value * spend * 5

    Other_return = float(input("What is your normal spend credit card return percentage? All bills is paid by PayPower bill payment."))/100 * spend

    CC_return = AMEX_return + Other_return

    Total_return = CC_return - cost

    print("Your mounthy return apporixmately ", Total_return , "CAD" )

else:
    cost_fix = AMF + PMF # Monthly fix cost to hold two accounts 
    cost_var = RLF * spend/500 +BPF * spend/1000 # Monthly Variable cost to reload and pay the 3rd Credit Card bill
    cost = cost_fix + cost_var

    AMEX_value = float(input("What is your estimate value for one AMEX Cobalt point Value in CAD cents ?"))/100

    AMEX_return = AMEX_value * (spend-30000/12) + AMEX_value * (30000/12) *5

    Other_return = float(input("What is your normal spend credit card return percentage? All bills is paid by PayPower bill payment."))/100 * spend

    CC_return = AMEX_return + Other_return

    Total_return = CC_return - cost

    print("Your mounthy return apporixmately ", Total_return , "CAD" )   
                        
                    
