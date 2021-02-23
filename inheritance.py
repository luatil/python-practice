class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:

    def __init__(self, length) -> None:
        super.__init__(length, length)

class Polygon:

    def __init__(self, number_of_sides) -> None:
        self.num = number_of_sides
        self.relevant = []

    def get_number_of_sides(self) -> int:
        return self.num

    def get_relevant(self) -> list:
        return self.relevant

class Triangle(Polygon):

    def __init__(self) -> None:
        super().__init__(3)
        self.relevant = ["asdf", "asdf"]