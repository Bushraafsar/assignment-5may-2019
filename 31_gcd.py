#TASK NO 31
# PYTHON PROGRAM TO CALCULATE GCD OF TWO POSITIVE INTEGER:
num1 = int(input("PLEASE ENTER FIRST POSITIVE INTEGER:"))
num2 = int(input("PLEASE ENTER SECOND POSITIVE INTEGER:"))
while num1 % num2 != 0:
    rem = num1 % num2
    num1 = num2
    num2 = rem
print("HCF OR GCD OF THESE INTEGERS IS:",num2)

