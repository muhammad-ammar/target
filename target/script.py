def calculate_area(width, height, unit):
    result = width * height
    print(f"The area is {result} {unit}")
    return

class geometry:
    def __init__(self, shape_type):
        self.shape = shape_type

    def print_shape(self):
        print("The shape is: " + self.shape)

    def calculate_square_area(self, side):
        return side * side

circle = geometry("circle")
circle.print_shape()

def unused_function():
    pass

def inconsistent_naming_style_function():
    return 42

PI = 3.14159
radius = 5
circle_area = PI * radius * radius
print("Circle area",circle_area)
