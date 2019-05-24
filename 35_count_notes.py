# TASK NO 35:
# PYTHON PROGRAM TO COUNT NO OF NOTES IN GIVEN AMOUNT:
amount =int (input("ENTER THE AMOUNT IN RUPEES:"))
lst=[10,20,50,100,500,1000]
a = 0
l = len(lst)-1
while amount != 0:
    if  lst[l] <= amount:
        amount = amount - lst[l]
        a += 1
    else :
        l = l-1 
print("NO. OF NOTES:",a)    