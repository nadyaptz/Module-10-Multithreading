from threading import Thread
import queue
from time import sleep
from random import randint


class Table:  # Table - стол, хранит информацию о находящемся за ним гостем (Guest).
    def __init__(self, table_number):
        self.table_number = table_number
        self.guest = None


class Guest(Thread):
    def __init__(self, guest_name):
        self.guest_name = guest_name
        super().__init__()

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def check_if_any_table_is_empty(self):  # проверяем, есть ли пустой стол в кафе.
        table_empty = True  # если есть пустой, то возвращаем его номер
        for t in self.tables:  # если нет пустого - возвращаем None
            if t.guest is None:
                return t
            else:
                table_empty = False
        if not table_empty:
            return None

    def all_tables_are_empty(self):  # проверяем, все ли столы пустые
        for t in self.tables:  # если хоть один занят - возвращаем False
            if t.guest is not None:
                return False
        return True  # если все перебрали и гостей нет, то возвращаем True

    def guest_arrival(self, *guests):
        for g in guests:
            if self.check_if_any_table_is_empty():  # если находим пустой стол
                t = self.check_if_any_table_is_empty()  # возвращаем его номер
                t.guest = g.guest_name  # за стол сажаем гостя
                print(f'{t.guest} сел(-а) за стол номер {t.table_number}')
                g.start()  # стартуем поток этого гостя
            else:
                self.queue.put(g)  # если нет пустого стола - ставим гостя в очередь
                print(f'{g.guest_name} в очереди')

    def serve_guests(self):
        while not self.queue.empty() or not self.all_tables_are_empty():  # пока очередь не пуста и хотя бы один стол не пустой
            for t in tables:        # перебираем столы
                for g in guests:    # перебираем гостей
                    if t.guest is not None and t.guest == g.guest_name and not g.is_alive(): # если за столом есть гость и он закончил свой поток
                        print(f'{t.guest} покушал(-а) и ушёл(ушла)')    # то освобождаем стол
                        print(f'Стол номер {t.table_number} свободен')
                        t.guest = None
                    if not self.queue.empty() and t.guest is None:      # если находим пустой стол и очередь не пуста
                        guest = self.queue.get()                        # берем гостя из очереди
                        t.guest = guest.guest_name
                        print(f'{guest.guest_name} вышел(-ла) из очереди и сел(-а) за стол номер {t.table_number}')
                        guest.start()                                      # сажаем за стол и начинаем поток этого гостя


# Создание столов
tables = [Table(number) for number in range(1, 6)]
print(tables)
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.serve_guests()
