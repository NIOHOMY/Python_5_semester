import random
from profile_decorator import ProfileDecorator
from factorial import nonRecursiveFactorial, recursiveFactorial, threadedFactorial, calculate_factorial
from bubble_sort import bubbleSort, bubbleSortMultipleTimes
from tools import generateRandomList,  getIntegerInput


""" Пахомова Полина
    Лаболаторная 2. 
    Напишите потокобезопасный профиль класса-декоратора, 
    который будет вычислять время выполнения функции и количество вызовов для функции пузырьковой сортировки. 
    
    Измерьте время выполнения многопоточной программы из упражнений 1-6 с помощью профиля-декоратора. 
    Сравните это время с временем выполнения однопоточной функции большого факториала.
"""


def print_menu():
    print("Меню:")
    print("1. Вычислить факториал (рекурсивно)")
    print("2. Вычислить факториал (нерекурсивно)")
    print("3. Вычислить факториал с использованием потоков")
    print("4. Запустить сортировку пузырьком")
    print("5. Выход")


if __name__ == '__main__':

    choice = '0'
    while choice != '5':
        print_menu()
        choice = input("Выберите функцию: ")

        if choice == '1':
            n = getIntegerInput("Введите положительное число не превышающее 300 для рекурсивного вычисления факториала: ")
            while n<0 or n > 300 :
                print("Число должно быть положительным и не больше 300. Попробуйте ещё раз.")
                n = getIntegerInput("")
            
            calculate_factorial(recursiveFactorial,n, ())
        elif choice == '2':
            n = getIntegerInput("Введите положительное целое число для нерекурсивного вычисления факториала: ")
            while n<0:
                print("Число должно быть положительным. Попробуйте ещё раз.")
                n = getIntegerInput("")
                   
            calculate_factorial(nonRecursiveFactorial,n, ())
        elif choice == '3':
            n = getIntegerInput("Введите положительное целое число для параллельного вычисления факториала: ")
            while n<0:
                print("Число должно быть положительным. Попробуйте ещё раз")
                n = getIntegerInput("")
                
            numThreads = getIntegerInput("Введите количество потоков: ")
            while (numThreads<=0):
                print("Число должно быть положительным. Попробуйте ещё раз")
                numThreads = getIntegerInput("")
                
            calculate_factorial(threadedFactorial,n, (numThreads,))
        elif choice == '4':
            size = getIntegerInput("Введите количество чисел в списке: ")
            while (size<=0):
                size = getIntegerInput("Число должно быть целым положительным. Попробуйте ещё раз. ")
                
            start = getIntegerInput("Введите начало диапазона: ")
            end = getIntegerInput("Введите конец диапазона: ")
            my_list = generateRandomList(size, start, end)
            
            num_times = getIntegerInput("Введите количество запусков сортировки пузырьком: ")
            while (num_times<=0):
                num_times = getIntegerInput("Число должно быть целым положительным. Попробуйте ещё раз. ")
            
            bubbleSortMultipleTimes(my_list, num_times)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз。")
