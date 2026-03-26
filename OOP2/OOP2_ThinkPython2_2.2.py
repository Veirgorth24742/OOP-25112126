import math

# The volume of a sphere with radius r is 4/3 * π * r^3. What is the volume of a sphere with radius 5?
def sphere_volume(r):

    volume = (4/3) * math.pi * (r ** 3)
    return volume

print("The volume of a sphere with radius 5 is", sphere_volume(5))

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?
def wholesale_cost(coverPrice: float, discount: float, shippingFirstCopy: float, 
                   shippingAddCopy: float, copies: int):
    
    discPrice = coverPrice * (1 - discount)
    total = (discPrice * copies) + shippingFirstCopy + (shippingAddCopy * (copies - 1))
    return total

print("The total wholesale cost for 60 copies is", wholesale_cost(24.95, 0.4, 3, 0.75, 60))

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
def time_total(startTime: str, ePace: str, tPace: str, eMiles: int, tMiles: int):
    startHour, startMin = map(int, startTime.split(':'))
    ePaceMin, ePaceSec = map(int, ePace.split(':'))
    tPaceMin, tPaceSec = map(int, tPace.split(':'))

    ePaceTime = (ePaceMin * 60 + ePaceSec) * eMiles
    tPaceTime = (tPaceMin * 60 + tPaceSec) * tMiles
    totalSec = ePaceTime + tPaceTime

    endHour = startHour + (totalSec // 3600)
    endMin = startMin + ((totalSec % 3600) // 60)

    if endMin >= 60:
        endHour += 1
        endMin -= 60

    return f"{endHour}:{endMin:02d}"

print("The time getting home for breakfast is", time_total("6:52", "8:15", "7:12", 2, 3))
