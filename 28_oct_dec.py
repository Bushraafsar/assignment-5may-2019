# task no 28
# python program to convert octal number to decimal number:
octal = input("ENTER OCTAL NUMBER NUMBER YOU WANT TO CONVERT IN DECIMAL:")
dec = 0
power = len(octal) - 1
for i in octal:
    dec += int(i)*8**power
    power = power -1 
print("decimal Number is:",dec)
