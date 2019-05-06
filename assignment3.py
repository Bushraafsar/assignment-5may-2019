English = int(input( "Enter Marks of English: "))
Pst = int(input( "Enter Marks of Pst: "))
Chemistry = int(input( "Enter Marks of Chemistry: "))
Sindhi = int(input( "Enter Marks of Sindhi: "))
Computer_Science = int(input( "Enter Marks of Computer Science: "))
Marks_Obtained = English + Pst + Chemistry + Sindhi + Computer_Science
print(Marks_Obtained)
Percentage = (Marks_Obtained/500*100)
print(Percentage)
if (Percentage >= 85) :
   print("Grade A+1")
elif (Percentage >= 70) : 
   print("Grade A")
elif (Percentage >= 60) :
   print("Grade B") 
elif (Percentage >= 50) :
   print("Grade C") 
elif (Percentage >= 40 ) : 
   print("Grade D") 
else :
   print("Fail")