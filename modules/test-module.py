

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

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        else:
            raise ValueError("Division by zero or unsupported operand type")

    def __str__(self):
        return f"({self.x}, {self.y})"


def main():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    result_add = v1 + v2
    print("Addition:", result_add)

    result_sub = v1 - v2
    print("Subtraction:", result_sub)

    result_mul = v1 * 2
    print("Scalar Multiplication:", result_mul)

    result_div = v1 / 2
    print("Scalar Division:", result_div)


if __name__ == '__main__':
    main()