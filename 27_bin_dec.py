# task no 27
# python program to convert binary number to decimal number:
binary = input("ENTER BINARY NUMBER NUMBER YOU WANT TO CONVERT IN DECIMAL:")
dec = 0
power = len(binary) - 1
for i in binary:
    dec += int(i)*2**power
    power = power -1 
print("decimal Number is:",dec)
