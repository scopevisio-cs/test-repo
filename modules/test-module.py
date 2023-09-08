

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -")

    def __str__(self):
        return f"({self.x}, {self.y})"


def main():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    result_add = v1 + v2
    print("Addition:", result_add)

    result_sub = v1 - v2
    print("Subtraction:", result_sub)


if __name__ == '__main__':
    main()