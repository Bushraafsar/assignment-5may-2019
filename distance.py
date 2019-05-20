#TASK19
#PYTHON PROGRAM TO CONVERT DISTANCE IN FEET TO YARDS,INCHES OR MILES:
distance = float(input("ENTER THE DISTANCE IN FEET:"))
distance_inches = distance*12 
print("DISTANCE IN INCHES IS:",distance_inches)
distance_yards = distance/3
print("DISTANCE IN YARDS IS:",distance_yards)
distance_miles = distance/5820
print("DISTANCE IN MILES IS:",distance_miles)    