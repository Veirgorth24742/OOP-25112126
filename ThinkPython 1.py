#thinkpython, Exercise 1.2
#1. How many seconds are there in 42 minutes 42 seconds?
mins = 42
secs = 42
sec_total = mins * 60 + secs
print("1. There are",sec_total,"seconds in 42 minutes 42 seconds.")

#2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
kms = 10
miles = 10/1.61
print("2. There are",miles,"miles in 10 kilometers.")

#3. If you run a 10 kilometers in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
min_total = secs / 60 + mins
hour_total = sec_total / 3600
pace_avg_mins = min_total / miles
pace_avg_secs = sec_total / miles
speed_avg_hour = miles / hour_total
print("3.1. The average pace - minutes per mile and second per mile are:",pace_avg_mins,"mins/mile and",pace_avg_secs,"secs/mile")
print("3.2. The average speed - miles per hour is",speed_avg_hour,"miles/hr")
