# TASK  NO 25 
# PYTHON PROGRAM TO CONVERT DECIMAL TO BINARY,OCTAL AND HEXADECIMAL:
print("---------------DECIMAL TO BINARY--------------------------------")
decimal = int(input("ENTER THE DECIMAL NO. YOU WANT TO CONVERT IN BINARY EQUIALENT:"))
binary = ""
while decimal > 0:
        rem = decimal % 2
        decimal = decimal//2
        binary = str(rem) + binary
print("binary no. is",binary)
print("----------------DECIMAL TO OCTAL-------------------------------")
decimal = int(input("ENTER THE DECIMAL NO. YOU WANT TO CONVERT IN OCTAL EQUIALENT:"))
octal  = ""
while decimal > 0:
        rem = decimal % 8
        decimal = decimal//8
        octal  = str(rem) + octal
print("octal number is",octal)
print("----------------DECIMAL TO HEXADECIMAL-------------------------------")
decimal = int(input("ENTER THE DECIMAL NO. YOU WANT TO CONVERT IN HEXADECIMAL EQUIALENT:"))
lst = "0123456789ABCDEF"
hexadecimal = ""
while decimal > 0 :
    rem = decimal % 16
    decimal = decimal // 16
    hexadecimal = str(lst[rem]) + hexadecimal
print("hexadecimal no. is",hexadecimal)    

