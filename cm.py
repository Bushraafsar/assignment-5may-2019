# task no 17
# python program to covert height(in feet amd inches) to ventimeter:
height_ft = int(input("ENTER YOUR HEIGHT IN FEET="))
height_inch = int(input("ENTER YOUR HEIGHT IN INCH="))
a = height_inch*2.54
b = height_ft*30.48
height_cm =round (a + b)
print("height in cm =",height_cm)
