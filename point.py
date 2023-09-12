class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other_object: object) -> bool:
        return self.x == other_object.x and self.y == other_object.y

    def __add__(self, other_object: object) -> object:
        new_x = self.x + other_object.x
        new_y = self.y + other_object.y
        return Point(new_x, new_y)


def main():
    point_obj_1 = Point(2, 4)
    point_obj_2 = Point(2, 4)
    print(point_obj_1 == point_obj_2)
    print(point_obj_1)
    print(point_obj_2)
    print(point_obj_2 + point_obj_1)

if __name__ == "__main__":
    main()