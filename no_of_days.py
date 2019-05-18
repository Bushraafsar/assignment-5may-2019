# TASK NO 5
# PYTHON PROGRAM TO CALCULATE DAYS BETWEEN TWO DATES!
from datetime import date
print("WRITE THE DATE IN THIS  FORMAT:DD,MM,YYYY")
d1,m1,y1 = (input("ENTER  FIRST DATE:")).split(",")
d2,m2,y2 =(input("ENTER SECOND DATE:")).split(',')
d1 = int(d1)
m1 = int(m1)
y1 = int(y1)
d2 = int(d2)
m2 = int(m2)
y2 = int(y2)
date1= date(y1,m1,d1)
date2 = date(y2,m2,d2)
period = date1-date2
print("DAYS BETWEEN TWO DATES IS:",period.days)