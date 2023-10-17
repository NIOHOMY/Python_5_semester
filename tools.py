import random

def generateRandomList(size, start, end):
    """
    Генерирует список случайных целых чисел в указанном диапазоне.
    :param size: Длина списка
    :param start: Начало диапазона (включительно)
    :param end: Конец диапазона (включительно)
    :return: Сгенерированный список целых чисел
    """
    if end < start:
        start, end = end, start
    my_list = [random.randint(start, end) for _ in range(size)]
    return my_list

    
def getIntegerInput(prompt):
    """
    Получает целочисленный ввод от пользователя с указанным приглашением.
    :param prompt (str): Приглашение для ввода.
    :return: int: Целочисленное значение, введенное пользователем.
    Примечание:
        Если пользователь вводит некорректное значение (не являющееся целым числом),
        выводится сообщение об ошибке и запрашивается ввод снова.
    """
    while True:
        try:
            value = int(input(prompt))    
            return value
            
        except ValueError:
            print("Некорректный ввод. Введите целое положительное число.")
