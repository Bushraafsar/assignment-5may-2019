# task no 32
# python program to calculate lcm of two numbers:
num1 = int(input("PLEASE ENTER FIRST POSITIVE INTEGER:"))
num2 = int(input("PLEASE ENTER FIRST SECOND INTEGER:"))
for m in range (1,num1*num2+1):
    if m % num1 == 0 and m % num2 == 0:
        lcm = m
        print("LCM OF TWO NUMBERS IS:",lcm)
        break