from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"Vector and {type(other)}")
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"unsupported operand type(s) for -: "
                            f"Vector and {type(other)}")
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if not isinstance(other, (int, float, Vector)):
            raise TypeError(f"unsupported operand type(s) for *: "
                            f"Vector and {type(other)}")
        if isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x=1 / self.get_length() * self.x,
            y=1 / self.get_length() * self.y
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = abs(self.y) / self.get_length()
        angle = math.degrees(math.acos(cos_a))
        if self.y > 0:
            return round(angle)
        elif self.y < 0:
            return round(180 - angle)
        return 90

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x=(math.cos(radians) * self.x - math.sin(radians) * self.y),
            y=(math.sin(radians) * self.x + math.cos(radians) * self.y)
        )
