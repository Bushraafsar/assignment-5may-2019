# TASK NO 34:
# PYTHON PROGRAM TO COUNT VOWEL AND CONSONANT:
# by naive method:
user_input = input("ENTER THE STRING HERE:")
count_vowel = 0
coutn_consonant = 0
for l in user_input: 
    if l == "a"or l == "e " or l =="i" or l == "o"or l == "u" or l == "A" or l == "E" or l == "I" or l == "O" or l == "U":
        count_vowel += 1
    else:
        coutn_consonant += 1
print("THE OCCURENCE OF VOWEL IN THE STRING IS:",count_vowel,"times")
print("THE OCCURENCE OF CONSONANT IN THIS STRING IS:",coutn_consonant,"times")            

