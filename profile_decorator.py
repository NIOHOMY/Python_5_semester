import time
from threading import Lock


class ProfileDecorator:
    """
    Декоратор класса для измерения времени выполнения функции и подсчета количества вызовов функции.
    Обеспечивает безопасность выполнения в многопоточной среде.
    """
    def __init__(self, func):
        self.func = func
        self.calls = 0
        self.total_time = 0.0
        self.lock = Lock()

    def __call__(self, *args, **kwargs):
        # Подсчет количества вызовов функции
        with self.lock:
            self.calls += 1

        # Измерение времени выполнения
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        # Подсчет общего времени выполнения
        execution_time = end_time - start_time
        with self.lock:
            self.total_time += execution_time

        return result

    def reset_time(self):
        """
        Сброс значения общего времени выполнения функции.
        """
        with self.lock:
            self.total_time = 0.0
            
    def reset_calls(self):
        """
        Сброс значения количества вызовов функции.
        """
        with self.lock:
            self.calls = 0
            
    def get_stats(self):
        """
        Получение статистических данных.
        """
        with self.lock:
            return f"Total calls: {self.calls}, Total execution time: {self.total_time:.16f} seconds"
