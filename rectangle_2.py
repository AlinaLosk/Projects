from rectangle import Rectangle, Squere, Circle
# создаем два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# Вывод площади двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

# вывод квадрат
square_1 = Squere(5)
square_2 = Squere(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

# Круг
circle_1 = Circle(3)
circle_2 = Circle(5)
# Вывод круг
print(circle_1.get_area_circle())
print(circle_2.get_area_circle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Squere):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())

#

