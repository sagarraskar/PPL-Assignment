class Circle(object):
    def __init__(self, radius=1):
        self.radius = radius 
        self.__pi = 3.14
    
    def area(self):
        return self.radius * self.radius * self.__pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

class RegularPolygon:
    def __init__(self, side = 1):
        self.side = side

    def setSide(self, side):
        self.side = side

    def getSide(self):
        return self.side

class Square(RegularPolygon):
    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4


class EquilateralTriangle(RegularPolygon):
    def __init__(self, side):
        RegularPolygon.__init__(self, side)

    def area(self):
        area = ((3**(1/2))/4) * self.side**2
        return area

    def perimeter(self):
        return self.side*3

class Rhombus(RegularPolygon):
    def __init__(self, diagonal1, diagonal2, side = 1):
        RegularPolygon.__init__(self, side)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        Area = 1/2 * self.diagonal1* self.diagonal2
        return Area

    def perimeter(self):
        return self.side * 4

    def setValues(self, side, diagonal1, diagonal2):
        RegularPolygon.setSide(self, side)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2


    def getValues(self):
        values = {}
        values["side"] = RegularPolygon.getSide(self)
        values["diagonal1"] = self.diagonal1
        values["diagonal2"] = self.diagonal2
        return values


class Rectangle:
   def __init__(self, length = 1, breadth = 1):
        self.length = length
        self.breadth = breadth

   def area(self):
        Area = self.length * self.breadth
        return Area

   def perimeter(self):
        Perimeter = 2 * (self.length + self.breadth)
        return Perimeter

   def setValues(self, side1, side2):
        self.length = side1
        self.breadth = side2


   def getValues(self):
        
        return {"length" : self.length, "breadth" : self.breadth}

class Parallelogram:
   def __init__(self, base = 1, heigth = 1, side = 1):
        self.base = base
        self.heigth = heigth
        self.side = side

   def area(self):
        Area = self.base * self.heigth
        return Area

   def perimeter(self):
        Perimeter = 2 * (self.base + self.side)
        return Perimeter

class IsoscelesTriangle:
   def __init__(self, side = 1, base = 1, height = 1):
        self.base = base
        self.height = height
        self.side = side

   def  area(self):
        Area = 1/2 * self.base * self.height
        return Area

   def perimeter(self):
        Perimeter = 2 * self.side + self.base
        return Perimeter

class ScaleneTriangle:
   def __init__(self, side1 = 1,side2 = 1, base = 1, height = 1):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

   def  area(self):
        Area = 1/2 * self.base * self.height
        return Area

   def perimeter(self):
        Perimeter = self.side1 + self.side2 + self.base
        return Perimeter
