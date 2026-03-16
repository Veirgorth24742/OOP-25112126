import math;
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)
    
    def read(self):
        self.x = int(input("Input x: "))
        self.y = int(input("Input y: "))
    
    def distance(self, point):
        d = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return d
    
A = Point(3,4)
print("A Point:", A)

B = Point()
B.read()
print("B Point:", B)

C = Point(-B.x, -B.y)
print("C Point:", C)

O = Point()
print("Distance from B to O:", B.distance(O))

print("Distance from A to B:", A.distance(B))
