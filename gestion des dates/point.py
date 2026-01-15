class Point2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def translation(self,a,b):
        self._x += a
        self._y += b
    def __eq__(self, o):
        if isinstance(o,Point2D):
            return self._x==o._x and self._y==o._y
    def __str__(self):
        return f"X:{self._x}\t{self._y}"
class POINT3D(Point2D):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z=z
    def translation(self, a, b,c):
         super().translation(a, b)
         self.z+=c
    def __eq__(self, o):
        return super().__eq__(o) and self.z==o.z
    def __str__(self):
        return super().__str__() + f"Z:{self.z}"
if __name__=='__main__':
    p0=POINT3D(1,5,-3)
    p=POINT3D(1,5,-3)
    print(p)
    print(p==p0)
    
    p.translation(0,-2,1)
    print(p)
    print(p0==p)
