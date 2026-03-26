import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d , %d)" % (self.x, self.y)
    
class LineSegment:
    def __init__(self, *args):
        self.__d1 = Point[0]
        self.__d2 = Point[1]

        if len(args) == 0:
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0)
        
        elif len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]

        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        
        elif len(args) == 1:
            if isinstance(args[0], LineSegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)

    def __str__(self):
        return "[(%d , %d), (%d , %d)]" % \
            (self.__d1.x, self.__d1.y, self.__d2.x, self.__d2.y)
    
    def getD1(self):
        return self.__d1
    def getD2(self):
        return self.__d2
    def setD1D2(self, p1, p2):
        self.__d1 = p1
        self.__d2 = p2

if __name__ == "__main__":
    l1 = LineSegment()

    p1 = Point(3, 4)
    p2 = Point(5, 6)

    l2 = LineSegment(p1, p2)
    l3 = LineSegment(5, 6, 7, 8)

    l4 = LineSegment(l1)

    print(l1)
    print(l2)
    print(l3)
    print(l4)