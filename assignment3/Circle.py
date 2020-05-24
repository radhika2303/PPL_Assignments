import turtle
class Circle:
    def __init__(self, r = 0):
        self.__radius = r
    def set_radius(self, r):
        self.radius = r
    def get_radius(self):
        return (self.radius)
    def find_area(self):
        pi = 3.14
        a = pi * self.radius * self.radius
        return (pi * self.radius * self.radius)
    def draw(self):
        t = turtle.Turtle()
        t.circle(self.radius)
        turtle.done()
c = Circle()
c.set_radius(100)
c.draw()
