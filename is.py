# TASK NO 8
# PYTHON PROGRAM TO GET A NEW STRING FROM GIVEN STRING IF IT WAS NOT BEGINNED WITH "IS"!
given_string = input("please enter string here :")
con = "is"
if (given_string[:2]==con):
    print("the given string remains unchanged!")
else:
    new_string = con + " "+ given_string
    print("the new string is =",new_string,"!" )    