def compound_calculator(principle,rate,time):
  
  Amount=principle*(pow((1+rate/100),time))
  Comp_interest=Amount-principle
  print("Compound interest is:",Comp_interest)
    
principle=int(input("Enter the Principle number:"))
rate=int(input("Enter the rate of interest:"))
time=int(input("Enter the time in year:"))

compound_calculator(principle, rate, time)
  