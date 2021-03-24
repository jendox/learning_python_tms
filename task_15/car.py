# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0)
# Методы: увеличить скорость (скорость + 5), уменьшение скорости (скорость -5)
# стоп (сброс скорости на 0), отображение скорости, разворот
# Все атрибуты приватные

class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0

    def speed_increase(self):
        if self.__speed > 220:
            raise ValueError(f'{self.__speed} - max speed of car')
        self.__speed += 5

    def speed_decrease(self):
        if self.__speed - 5 < 0:
            raise Exception(f'Speed lower than 0 km/h')
        self.__speed -=5

    def speed_show(self):
        print(f'Speed = {self.__speed} km/h')

    def stop_car(self):
        self.__speed = 0

# print(
#     f'1 - show speed of car\n'+
#     f'2 - stop car\n'+
#     f'+ - increase speed\n'+
#     f'- - decrease speed\n'+
#     f'0 - exit')
#
# m_car = Car('BMW', 'X3', 2012)
#
# choice = {
#     '1': m_car.speed_show,
#     '2': m_car.stop_car,
#     '+': m_car.speed_increase,
#     '-': m_car.speed_decrease
# }
#
# while True:
#     try:
#         i = input()
#         if i == '0':
#             exit(0)
#         choice[i]()
#     except Exception as e:
#         print(f'Invalid input {e}')
