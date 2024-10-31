import threading
import time
from random import randint
from time import sleep
counter = 0

class Bank:

    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        global counter
        for i in range(100):
            cash = randint(50, 500)
            self.balance += cash
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'\33[32mПополнение: {cash} y.e. Баланс: {self.balance} y.e.\33[0m')
            sleep(0.001)
            counter = i

    def take(self):
        global counter
        for i in range(100):
            cash = randint(50, 500)
            print(f'\33[33mЗапрос на {cash} y.e.\33[0m')
            if self.balance >= cash:
                self.balance -= cash
                print(f'\33[31mСнятие: {cash} y.e. Баланс: {self.balance} y.e.\33[0m')

            else:
                print('\33[34mЗапрос отклонён, недостаточно средств.\33[0m')
                if counter < 99:
                    self.lock.acquire()

            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()


print('___________________________')
print(f'Итоговый баланс: {bk.balance} y.e.')
