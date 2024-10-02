import random
import time
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            addition = random.randint(50, 500)
            self.balance += addition
            print(f'Пополнение: {addition}. Баланс: {self.balance}.')
            time.sleep(0.0001)

    def take(self):
        for i in range(100):
            deduction = random.randint(50, 500)
            print(f'Запрос на {deduction}')
            if deduction <= self.balance:
                self.balance -= deduction
                print(f'Снятие: {deduction}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств.')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
