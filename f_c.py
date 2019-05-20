#TASK NO  23
#PYTHON PROGRAM TO CONVERT TEMPERATURE TO  AND FROM CELSIUS  ,FAHRENHEIT:
temp= float(input("ENTER THE TEMPERATURE  YOU WANT TO CONVERT:"))
a= (input("ENTER THE DEGREE F FOR FAHRENHEIT or C FOR CELCIUS:"))
if a ==  'F':
    temp_farhenient  =  (temp * 9/5)+32
    print("TEMPERATURE IN FAHRENHEIT =",temp_farhenient,"F")
elif a == 'C':
    temp_celcius =  (temp-32) *5/9 
    print("TEMPERATURE IN CELCIUS =",temp_celcius,"C")
else:
    print("you enter wrong syntax!")