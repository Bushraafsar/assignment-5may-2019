# TASK NO 40
# PYTHON PROGRAM TO COUNT LETTERS AND DIGITS IN GIVEN STRING:
string = input("ENTER A STRING:")
count_digits = 0
count_letters = 0
count_symbol = 0
for i in string:
    if i.isdigit():
        count_digits += 1
    elif i.isalpha():
        count_letters+=1
    else:
        count_symbol+=1    
print ("THE COUNT OF DIGITS IN GEVIN STRING IS :",count_digits)
print ("THE COUNT OF LETTERS IN GEVIN STRING IS :",count_letters)


            
