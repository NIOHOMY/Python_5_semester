from profile_decorator import ProfileDecorator
from threading import Thread, Lock

@ProfileDecorator
def nonRecursiveFactorial(n):
    """
    Вычисление факториала без использования рекурсии.
    Аргументы:
        n (int): Целое число для вычисления факториала.
    Возвращает:
        int: Факториал числа n.
    """
    if (n>=0):
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
    else:
        return -1


@ProfileDecorator
def recursiveFactorial(n, stop=1):
    """Функция задания 1-2 для вычисления факториала числа.
    Args:
        n (int): Число, для которого нужно вычислить факториал.
        stop (int): Число, до которого будет вычисляться часть факториала (используется в многопоточности, по умолчанию 1).
    Returns:
        int: Факториал числа n.
    """
    if (n>=0):
        if n <= stop:
            return 1
        else:
            return n * recursiveFactorial(n - 1, stop)
    else:
        return -1

@ProfileDecorator
def threadedFactorial(n, num_threads):
    """Задание 1-6 Вычисляет большой факториал с использованием нескольких потоков и функции задания 2.
    
    Args:
        n (int): Число, для которого нужно вычислить факториал.
        num_threads (int): Количество потоков для распараллеливания вычислений.
    
    Returns:
        int: Факториал числа n.
    """
    if (n>=0) and (num_threads>0):
        chunk_size = n // num_threads
        threads = []
        results = []
        lock = Lock()
    
        def factorial_helper(start, end):
            local_result = 1
            local_result *= recursiveFactorial(end, start)
            with lock:
                results.append(local_result)
    
        # Создание потоков и распределение работы
        for i in range(num_threads):
            start = i * chunk_size + 1
            end = start + chunk_size - 1 if i < num_threads - 1 else n
            thread = Thread(target=factorial_helper, args=(start, end))
            threads.append(thread)
            thread.start()
    
        # Ожидание завершения всех потоков
        for thread in threads:
            thread.join()
    
        # Объединение результатов
        result = 1
        for res in results:
            result *= res
        
        recursiveFactorial.reset_time();
    
    
        return result
    else:
        return -1


def calculate_factorial(func,n, params):
    """
    Вычисляет факториал числа с использованием указанной функции.
    :param func (callable): Функция для вычисления факториала.
    :param n (int): Число, для которого нужно вычислить факториал.
    :param params (tuple): Дополнительные параметры для передачи в функцию.
    Вывод:
        Выводит результат вычисления факториала и статистику выполнения функции.
    """
    result = func(n, *params)
    stats = func.get_stats()
    print(f"Факториал числа {n}: {result}")
    print(stats)
    func.reset_time()
