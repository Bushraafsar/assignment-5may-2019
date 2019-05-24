# task no 37
# PYTHON PROGRAM TP REVERSE THE DIGITS OF A GIVEN NO AND ADD IT TO THE ORIGINAL ,IF THE SUM IS NOT IS PALINDRPME REPEAT THE PROGRAM:
num = input("ENTER A NUMBER:")
num1 = num[::-1]
sum1 = int(num)+ int(num1)
sum1 = str(sum1)
if sum1 == sum1[::-1]:
    print("it is palindrome !")
else:
    print("it is not a palindrome!")    
 