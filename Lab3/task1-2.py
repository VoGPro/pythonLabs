import math
import random
import string
# Вариант 6. Написать программу, демонстрирующую работу с объектами
# двух типов T1 и T2, для чего создать систему соответствующих классов.
# Каждый объект должен иметь идентификатор (в виде произвольной строки
# символов) и одно или несколько полей для хранения состояния (текущего
# значения) объекта.
# Перечень типов объектов: Треугольник (Triangle), Четырёхугольник
# (Tetragon).
# Перечень дополнительных методов:
# move() переместить объект на плоскости;
# compare(T1 t1, T2 t2) сравнение объектов по площади.
# Необходимо предусмотреть генерацию и обработку
# исключений для возможных ошибочных ситуаций.

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def move(self, x, y):
        self.__x += x
        self.__y += y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def distance(self, other):
        return math.sqrt((other.x - self.__x)**2 + (other.y - self.__y)**2)


class Triangle:
    __name = "треугольник"

    def __init__(self, a, b, c):
        self.__id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.__a = a
        self.__b = b
        self.__c = c
        self.__area = self.__find_area()

    def __find_area(self):
        ab = self.__a.distance(self.__b)
        bc = self.__b.distance(self.__c)
        ac = self.__a.distance(self.__c)
        semi_p = (ab + bc + ac) / 2
        return round(math.sqrt(semi_p * (semi_p - ab) * (semi_p - bc) * (semi_p - ac)), 2)

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def area(self):
        return self.__area

    def move(self, x, y):
        self.__a.move(x, y)
        self.__b.move(x, y)
        self.__c.move(x, y)

    def compare(self, shape):
        area_diff = self.__area - shape.area
        if area_diff > 0:
            print(f"Площадь {self.__name}а с id={self.__id} больше площади {shape.name}а с id={shape.id} на {area_diff}.")
        elif area_diff < 0:
            print(f"Площадь {shape.name}а с id={shape.id} больше площади {self.__name}а с id={self.__id} на {abs(area_diff)}.")
        else:
            print(f"Площади {self.__name}а с id={self.__id} и {shape.name}а с id={shape.id} равны.")

    def __str__(self):
        return (f"{self.name.capitalize()} (id={self.id})\n"
                f"Точка A: ({self.__a.x}, {self.__a.y})\n"
                f"Точка B: ({self.__b.x}, {self.__b.y})\n"
                f"Точка C: ({self.__c.x}, {self.__c.y})\n"
                f"Площадь: {self.area}")


class Tetragon:
    __name = "четырёхугольник"

    def __init__(self, a, b, c, d):
        self.__id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__area = self.__find_area()

    def __find_area(self):
        ab = self.__a.distance(self.__b)
        bc = self.__b.distance(self.__c)
        cd = self.__c.distance(self.__d)
        ad = self.__a.distance(self.__d)
        semi_p = (ab + bc + cd + ad) / 2
        return round(math.sqrt((semi_p - ab) * (semi_p - bc) * (semi_p - cd) * (semi_p - ad)), 2)

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def area(self):
        return self.__area

    def move(self, x, y):
        self.__a.move(x, y)
        self.__b.move(x, y)
        self.__c.move(x, y)
        self.__d.move(x, y)

    def compare(self, shape):
        area_diff = round(self.__area - shape.area, 2)
        if area_diff > 0:
            print(f"Площадь {self.__name}а с id={self.__id} больше площади {shape.name}а с id={shape.id} на {area_diff}.")
        elif area_diff < 0:
            print(f"Площадь {shape.name}а с id={shape.id} больше площади {self.__name}а с id={self.__id} на {abs(area_diff)}.")
        else:
            print(f"Площади {self.__name}а с id={self.__id} и {shape.name}а с id={shape.id} равны.")

    def __str__(self):
        return (f"{self.name.capitalize()} (id={self.id})\n"
                f"Точка A: ({self.__a.x}, {self.__a.y})\n"
                f"Точка B: ({self.__b.x}, {self.__b.y})\n"
                f"Точка C: ({self.__c.x}, {self.__c.y})\n"
                f"Точка D: ({self.__d.x}, {self.__d.y})\n"
                f"Площадь: {self.area}")


triangle1 = Triangle(Point(0, 0), Point(5, 3), Point(2, 6))
triangle2 = Triangle(Point(-7, -9), Point(-10, -6), Point(-12, -12))
tetragon1 = Tetragon(Point(3, 2), Point(5, 3), Point(6, 6), Point(2, 5))
tetragon2 = Tetragon(Point(13, 22), Point(35, 23), Point(36, 57), Point(12, 54))
print("\nСозданы следующие геометрические фигуры:\n")
print(triangle1)
print()
print(triangle2)
print()
print(tetragon1)
print()
print(tetragon2)

xTe2 = 10
yTe2 = -12
print(f"\nПередвинем четырёхугольник с id={tetragon2.id} на ({xTe2}, {yTe2}) значений по x и по y:")
tetragon2.move(xTe2, -yTe2)
print(tetragon2)

print("\nСравним площади фигур:")
tetragon2.compare(triangle1)
tetragon1.compare(triangle1)
triangle1.compare(triangle2)