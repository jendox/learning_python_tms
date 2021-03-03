class Car:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = 0

    def increase_speed(self):
        self._speed += 5

    def reduce_speed(self):
        if self._speed > 0:
            self._speed -= 5
        else:
            self._speed = 0
            self.show_speed()

    def stop_car(self):
        self._speed = 0

    def show_speed(self):
        print(f'Speed of the car is {self._speed} km/h')

    def change_speed(self):
        self._speed *= -1

car = Car('BMW','i312','1991')
car.show_speed()
car.increase_speed()
car.show_speed()
car.increase_speed()
car.increase_speed()
car.show_speed()
car.reduce_speed()
car.change_speed()
car.show_speed()