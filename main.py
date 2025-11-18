import math

# --- SUPER CLASS ---
class Shape:
    def area(self):
        """Har bir shakl o‘zining area() metodiga ega bo‘lishi kerak."""
        raise NotImplementedError("area() metodi subclasslarda aniqlanishi kerak")

    def perimeter(self):
        """Har bir shakl o‘zining perimeter() metodiga ega bo‘lishi kerak."""
        raise NotImplementedError("perimeter() metodi subclasslarda aniqlanishi kerak")


# --- CIRCLE ---
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# --- RECTANGLE ---
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# --- TRIANGLE ---
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} -> Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
