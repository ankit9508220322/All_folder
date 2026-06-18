class Point:
    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y
    
    def __str__(self):
        return '<{},{}>'.format(self.x_cord,self.y_cord)
    
    def euclidean(self,other):
        return ((self.x_cord - other.x_cord)**2+(self.y_cord - other.y_cord)**2)**0.5
    
    def distance_origen(self):
        return self.euclidean(Point(0,0))
p1 = Point(0,0)
p2 = Point(10,10)
px = p1.distance_origen()
print(px)
print(p1.euclidean(p2))
