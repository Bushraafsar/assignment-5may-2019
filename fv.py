# TASK NO 15
# PYTHON PROGRAM TO CALCULATE FUTURE VALUE:
pv = int(input("ENTER PRINCIPAL VALUE:"))
r =float(input("ENTER RATE OF INTEREST:"))
n =int(input("ENTER NO. OF YEARS:")) 
future_value = pv*((1+(0.01*r))**n)
print("FUTURE VALUE IS =",future_value)
