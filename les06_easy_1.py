# easy 1/2
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class Car:
    def __init__(self, max_car_speed, car_color, car_name, car_is_police):
        self.max_speed = max_car_speed
        self.color = car_color
        self.name = car_name
        self.police = bool(car_is_police)
        print('Машина цвета \"' + car_color + '\", марки \"' + car_name + \
              '\" запустила двигатель.')
        if self.police:
            print('Преступники, будьте осторожны!')

    def go(self):
        print('Машина \"' + self.name + '\" поехала с максимальной возможной скоростью ' + \
              str(self.max_speed))

    def stop(self):
        print('Машина \"' + self.name + '\" остановилась')

    def turn(self, direction):
        print('Машина повернула ' + direction)


class TownCar(Car):
    def __init__(self, car_color, car_name):
        super().__init__(90, car_color, car_name, False)


class SportCar(Car):
    def __init__(self, car_color, car_name):
        super().__init__(220, car_color, car_name, False)


class WorkCar(Car):
    def do_something(self):
        print('чё-то делает')


class PoliceCar(Car):
    def __init__(self, car_speed, car_color, car_name):
        super().__init__(car_speed, car_color, car_name, True)


town_car = TownCar("зелёный", "chevrolet")
town_car.go()
town_car.turn("налево")
town_car.stop()

work_car = WorkCar(10, 'green', 'nissan', False)
work_car.do_something()