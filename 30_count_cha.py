# task no 30
# python program to calculate occurence of specifiic character in a given string;
string = input("ENTER THE ANY STRING:")
character = input("ENTER THE CHARACTER YOU WANT TO COUNT IN STRING:")
count = 0
for a in string:
    if a == character:
        count += 1
print("This character occur in String :",count,"times")      
