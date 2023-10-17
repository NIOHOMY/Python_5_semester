import random
import time
from functools import wraps
from threading import Thread
import threading

""" Пахомова Полина
Упражнение 1-1. Напишите простую игру "Угадай число".
Программа будет случайным образом выбирать число в заданном диапазоне и ждать, пока пользователь введет его.
Если число меньше или больше того, которое выбрала программа, то система сообщает об этом пользователю.
Если угаданное число правильное, то игра заканчивается, и программа выводит на экран количество итераций.
Упражнение 1-2. Напишите рекурсивную функцию, которая вычисляет факториал
Упражнение 1-3. Напишите функцию, вычисляющую среднее значение от произвольного числа аргументов. 
Упражнение 1-4. Напишите функцию, складывающую два числа следующим образом: add(1)(2) == 3
Упражнение 1-5. Напишите декоратор, который вычисляет время выполнения декорированной функции.
Упражнение 1-6. Напишите функцию, которая вычисляет большой факториал с использованием нескольких потоков, используя функции из 2
"""





# Задание 1: Игра "Угадай число"
def guess_the_number(start, end):
    """Функция для игры "Угадай число".
    
    Args:
        start (int): Начало диапазона.
        end (int): Конец диапазона.
    """
    if start>end:
        start,end = end, start;
    target = random.randint(start, end)
    attempts = 0

    while True:
        try:
            guess = int(input("Введите число: "))
            attempts += 1

            if guess < start or guess > end:
                print(f"Пожалуйста, введите число в диапазоне от {start} до {end}")
                continue

            if guess < target:
                print("Загаданное число больше")
            elif guess > target:
                print("Загаданное число меньше")
            else:
                print(f"Поздравляю! Вы угадали число {target} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

# Задание 2: Рекурсивная функция для вычисления факториала
def factorial(n, stop=1):
    """Функция для вычисления факториала числа.
    
    Args:
        n (int): Число, для которого нужно вычислить факториал.
        stop (int): Число, до которого будет вычисляться часть факториала (используется в многопоточности, по умолчанию 1).
    
    Returns:
        int: Факториал числа n.
    """
    if n == 0 or n == 1 or n == stop-1:
        return 1
    else:
        return n * factorial(n - 1, stop)

# Задание 3: Функция для вычисления среднего значения
def compute_average(*args):
    """Функция для вычисления среднего значения списка чисел.
    
    Args:
        args (float): Список чисел.
    
    Returns:
        float: Среднее значение чисел.
    """
    if len(args) == 0:
        return None
    return sum(args) / len(args)

# Задание 4: Функция сложения двух чисел через каррирование
def add(x):
    """Функция каррирования для сложения чисел.
    
    Args:
        x (float): Первое число.
    
    Returns:
        float: Результат сложения двух чисел.
    """
    def inner(y):
        return x + y
    return inner

# Задание 5: Декоратор для вычисления времени выполнения функции
def execution_time(func):
    """Декоратор для измерения времени выполнения функции.
    
    Args:
        func (function): Декорируемая функция.
    
    Returns:
        function: Обернутая функция с добавленным измерением времени выполнения.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time} секунд.")
        return result
    return wrapper

# Задание 6: Функция для вычисления большого факториала с использованием многопоточности
def threaded_factorial(n, num_threads):
    """Вычисляет большой факториал с использованием нескольких потоков и функции задания 2.
    
    Args:
        n (int): Число, для которого нужно вычислить факториал.
        num_threads (int): Количество потоков для распараллеливания вычислений.
    
    Returns:
        int: Факториал числа n.
    """
    chunk_size = n // num_threads
    threads = []
    results = []
    lock = threading.Lock()
    
    def factorial_helper(start, end):
        local_result = 1
        local_result *= factorial(end, start)
        with lock:
            results.append(local_result)
    
    # Создание потоков и распределение работы
    for i in range(num_threads):
        start = i * chunk_size + 1
        end = start + chunk_size - 1 if i < num_threads - 1 else n
        thread = threading.Thread(target=factorial_helper, args=(start, end))
        threads.append(thread)
        thread.start()
    
    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()
    
    # Объединение результатов
    result = 1
    for res in results:
        result *= res
    
    return result


# Функция для округления числа до ближайшего значения с точностью до 0.001
def round_to_0_001(num):
    return round(num * 1000) / 1000

# Функция интерфейса и обработки выбора пользователя
def main_menu():
    """
    Функция для вывода интерфейса и обработки выбора пользователя.
    """
    while True:
        print("""
        Меню:
        1. Угадай число
        2. Вычислить факториал
        3. Вычислить среднее значение
        4. Сложить два числа
        5. Вычислить время выполнения функции 6
        6. Вычислить большой факториал (многопоточность)
        0. Выход
        """)

        choice = input("Выберите функцию (введите номер): ")

        if choice == '1':
            while True:
                try:
                    start = int(input("Введите начало диапазона: "))
                    end = int(input("Введите конец диапазона: "))
                    guess_the_number(start, end)
                    break
                except ValueError:
                    print("Пожалуйста, введите целые числа.")
        elif choice == '2':
            while True:
                try:
                    n = int(input("Введите число для вычисления факториала: "))
                    print(factorial(n,1))
                    break
                except ValueError:
                    print("Пожалуйста, введите целое число.")
        elif choice == '3':
            while True:
                try:
                    print("Дробная часть через точку, точность 0.001")
                    nums = input("Введите числа через пробел для вычисления среднего значения: ").split()
                    nums = [(float(num)) for num in nums]
                    print(round_to_0_001(compute_average(*nums)))
                    break
                except ValueError:
                    print("Пожалуйста, введите действительные числа, разделенные пробелами.")
        elif choice == '4':
            while True:
                try:
                    print("Дробная часть через точку, точность 0.001")
                    x = (float(input("Введите первое число: ")))
                    y = (float(input("Введите второе число: ")))
                    print(round_to_0_001(add(x)(y)))
                    break
                except ValueError:
                    print("Пожалуйста, введите действительные числа.")
        elif choice == '5':
            while True:
                try:
                    n = int(input("Введите число для вычисления большого факториала: "))
                    num_threads = int(input("Введите количество потоков: "))

                    @execution_time
                    def dummy_function():
                        threaded_factorial(n, num_threads)

                    dummy_function()
                    break
                except ValueError:
                    print("Пожалуйста, введите целые числа.")
        elif choice == '6':
            while True:
                try:
                    n = int(input("Введите число для вычисления большого факториала: "))
                    num_threads = int(input("Введите количество потоков: "))
                    print(threaded_factorial(n, num_threads))
                    break
                except ValueError:
                    print("Пожалуйста, введите целые числа.")
        elif choice == '0':
            break
        else:
            print("Недопустимый выбор. Попробуйте ещё раз.")

# Начало программы
main_menu()
