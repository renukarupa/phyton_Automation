# Area and Perimeter
class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**3.141

    def perimeter(self):
        return 2*self.radius*3.141

NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())