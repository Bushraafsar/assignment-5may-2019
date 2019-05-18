#task no 16
#python program to compute distance between two points:
import math
x1 = int(input("ENTER VALUE OF X1:"))
y1 = int(input("ENTER VALUE OF y1:"))
x2 = int(input("ENTER VALUE OF x2:"))
y2 = int(input("ENTER VALUE OF y2:"))
dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print("DISTANCE BETWEEN TWO POINTS IS =",dis)

