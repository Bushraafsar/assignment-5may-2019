# TASK NO 21
# PYTHON PROGRAM TO CONVERT SECONDS TO DAYS HOURS MINUTES AND SECONDS:
time_sec = int(input("ENTER THE TIME IN SECONDS :"))
time_days = time_sec*1/86400
print("TIME IN DAYS:",time_days)
time_hrs = time_sec*1/3600
print("TIME IN HOURS:",time_hrs)
time_min = time_sec/60
print("TIME N MINUTES:",time_min)