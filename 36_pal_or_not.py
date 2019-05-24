# TASK NO 36
# PYTHON PROGRAM TO CHECK WHETHER GIVEM INPUT IS PALINDROME OR NOT
user_input=input("enter the string here:")
input_user =user_input[::-1]
if user_input == input_user:
    print("IT IS PALINDROME!")
else:
    print("IT IS NOT PALINDROME!")    