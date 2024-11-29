class Rectangle:
    def draw(self):
        print("Drawing a Rectangle")
class Circle:
    def draw(self):
        print("Drawing a Circle")

def draws(shapes):
    for i in shapes:
        i.draw()

shapes=[Rectangle(),Circle(),Rectangle(),Circle()]
draws(shapes)