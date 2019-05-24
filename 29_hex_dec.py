# TASK NO 29
# PYTHON PROGRAM TO CONVERT HEXADECIMAL NUMBER TO DECIMAL NO:
hexadecimal = input("ENTER DECIMAL NUMBER YOU WANT TO CONVERT IN DECIMAL:")
dec = 0
power = len(hexadecimal)-1
for i in range(len(hexadecimal)):
    if hexadecimal[i] == "A":
        dec  = dec + 10*16**power
    elif hexadecimal[i] == "B":
        dec  = dec + 11*16**power
    elif hexadecimal[i] == "C":
        dec = dec+12*16**power
    elif hexadecimal[i]  == "D" :
        dec = dec+13*16**power
    elif hexadecimal[i] == "E":
        dec = dec + 14*16**power
    elif hexadecimal[i] == "F" :
        dec = dec + 15*16**power
    else:
        dec = dec+int(hexadecimal[i])*16**power
    power = power -1
print("DECIMAL NUMBER OF",hexadecimal,"IS",dec)           

    

    

    