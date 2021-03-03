from classes import Point
from classes import Circle
from classes import Triangle
from classes import Square

if __name__ == '__main__':

    m_circle = Circle(Point(2, 2), 6)
    m_triangle = Triangle(Point(1, 1), Point(3, 4), Point(5, 2))
    m_square = Square(Point(2, 2), Point(5, 5))

    f_list = []
    f_list.append(m_circle)
    f_list.append(m_triangle)
    f_list.append(m_square)
    for i in f_list:
        print(f'Периметр: {i.perimeter}, Площадь: {i.area}')