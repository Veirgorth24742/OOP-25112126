import math
class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

class Rectangle:
    def __init__(self, corner: Point, width: float, height: float):
        self.corner = corner
        self.width = width
        self.height = height

def rectangle_corners(rect: Rectangle) -> list[Point]:
    c = rect.corner
    return [
        Point(c.x,                c.y               ),
        Point(c.x + rect.width,   c.y               ),
        Point(c.x,                c.y + rect.height ),
        Point(c.x + rect.width,   c.y + rect.height )
    ]

def distance_circle(point1: Point, point2: Point) -> float:
    d = math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    return d

def point_in_circle(circle: Circle, point: Point) -> bool:
    return distance_circle(circle.center, point) <= circle.radius

def rect_in_circle(circle: Circle, rect: Rectangle) -> bool:
    return all(point_in_circle(circle, p) for p in rectangle_corners(rect))
    
def rect_circle_overlap(circle: Circle, rect: Rectangle) -> bool:
    return any(point_in_circle(circle, p) for p in rectangle_corners(rect))

circle = Circle(Point(150,100),75)
point1 = Point(50,100)
point2 = Point(30,60)
rect = Rectangle(Point(50,80),60,90)

print(f"Điểm 1 trong vòng tròn: {point_in_circle(circle,point1)}")
print(f"Điểm 2 trong vòng tròn: {point_in_circle(circle,point2)}")
print(f"Tứ giác nằm trong vòng tròn: {rect_in_circle(circle, rect)}")
print(f"Tứ giác giao với vòng tròn: {rect_circle_overlap(circle, rect)}")
