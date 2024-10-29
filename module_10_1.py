from threading import Thread
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


def time_dec(func):
    def wrapper(*args, **kwargs):
        started_at = time()
        func(*args, **kwargs)
        ended_at = time()
        work_time = round(ended_at - started_at, 6)
        print(f'\33[31mРабота потоков: {work_time} сек.\33[0m')

    return wrapper


@time_dec
def start_func():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')


@time_dec
def start_thread():
    thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
    thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
    thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
    thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()


print('\33[35mЗапуск функций с аргументами:\33[0m')
start_func()
print()
print('\33[32mСоздание и запуск потоков с аргументами:\33[0m')
start_thread()
