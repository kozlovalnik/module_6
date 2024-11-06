
class Figure:
    sides_count = 0
    __sides = []
    __colors = [0, 0, 0]
    filled = False

    def __init__(self):
        self.__sides = []
        self.__colors = [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__colors

    def is_valid_color(self, r: int, g: int, b: int) -> bool:
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            return True
        else:
            return False

    def set_color(self, r: int, g: int, b: int) -> None:
        if self.is_valid_color(r, g, b):
            self.__colors = [r, g, b]

    def __is_valid_sides(self, sides: tuple) -> bool:
        if len(sides) == len(self.__sides):
            for i in range(len(sides)):
                if sides[i] <= 0:
                    return False
            return True

    def fill_sides(self, sides: tuple) -> None:
        if len(sides) == self.sides_count:
            for i in range(self.sides_count):
                self.__sides.append(sides[i])

    def get_sides(self) -> list:
        return self.__sides

    def set_sides(self, new_sides: tuple) -> None:
        if self.__is_valid_sides(new_sides):
            for i in range(len(new_sides)):
                self.__sides[i] = new_sides[i]

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    __radius = 0

    def __init__(self, colors: tuple, perimetr: int) -> None:
        super().__init__()
        self.sides_count = 1
        self.set_color(colors[0], colors[1], colors[2])
        self.fill_sides((perimetr,))
        self.__radius = (perimetr / 3.14) ** 0.5

class Triangle(Figure):
    def __init__(self, colors: tuple, side1: int, side2: int, side3: int) -> None:
        super().__init__()
        self.sides_count = 3
        self.fill_sides((side1, side2, side3))

    def get_square(self):
        side_list = get_sides(self)
        p = (side_list[0] + side_list[1] + side_list[2]) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

class Cube(Figure):
    __side = 0

    def __init__(self, colors: tuple, side: int):
        super().__init__()
        self.sides_count = 12
        self.__side = side
        self.set_color(colors[0], colors[1], colors[2])
        self.fill_sides((side, side, side, side, side, side, side, side, side, side, side, side))

    def get_volume(self) -> int:
        return self.__side ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides((5, 3, 12, 4, 5)) # Не изменится
print(cube1.get_sides())
circle1.set_sides((15,)) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())