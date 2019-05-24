# TASK NO 38
# PYTHON PROGRAM TO GET FIBONACCI SERIES ...
n=int(input("ENTER AN INTEGER TO WHICH FIBONACCI SERIES ARE TO BE GENERATED:")) 
a=0
b=1
if  n  <=  0:
    print("PLEASE ENTER A NUMBER  GREATER  THAN ZERO!")
elif n  == 1:
    print(a)
else:
    print("-------------fibonacci series-----------------------")
    print(a)
    print(b)
    for  i in range(2,n):
        c = a+b
        a = b  
        b = c
        print(c)