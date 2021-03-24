import unittest
from car import Car

class TestCar(unittest.TestCase, Car):

    def test_speed_decrease(self):
        car_ = Car('Mercedes','C200',1995)
        print('-' * 10 + 'BEGIN' + '-' * 10)
        the_exc = self.assertRaises(Exception, car_.speed_decrease)
        print('-'*11+'END'+'-'*11)

