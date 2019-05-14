# how to calculate mean from the list by using for loop and random,randint!
import random
arr = []
for i in range(100):
     arr.append(random.randint(1,100))
     print(arr)
sum_of_obs =0
for num in arr:
     sum_of_obs += num
print("SUM OF OBSERVATION=",sum_of_obs)
no_of_obs = len(arr) 
print("NO.OF OBSERVVATION=",no_of_obs) 
print("formula:") 
print("Mean=sum of obseravation/no of observation")  
mean =sum_of_obs/no_of_obs
print("MEAN =",mean)
# how to calculate minimum and maximum value by looping!
#MINIMUM VALUE:
min_value = arr[0]
max_value = arr[0]
for a in range(len(arr)):
    if min_value> arr[a]:
        min_value = arr[a]
        minimum_ind_position = a
# MAXIMUM VALUE:
    elif max_value<arr[a]:
        max_value = arr[a] 
        maximum_ind_position = a
 # RESULT:       
print("MAXIMUM VALUE OF THE LIST IS =",max_value) 
print("INDEX POSITION OF MAX VALUE IN THIS LIST IS =",maximum_ind_position)
print("MINIMUM VALUE OF THE LIST IS =",min_value) 
print("INDEX POSITION OF MAX VALUE IN THIS LIST IS =",minimum_ind_position) 