from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name_: str, power: int):
        self.name_ = name_
        self.power = power
        self.enemies = 100
        self.days = 0
        super().__init__()

    def run(self):
        print(f'{self.name_}, на нас напали!')
        while self.enemies > 0:
            sleep(1)
            self.days += 1
            self.enemies -= self.power
            print(f'{self.name_} сражается {self.days} дней, осталось {self.enemies} воинов')
        print(f'{self.name_} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
