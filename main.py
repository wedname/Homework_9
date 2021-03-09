"""
Задание 1
Напишите функцию, вычисляющую произведение
элементов списка целых. Список передаётся в качестве па-
раметра. Полученный результат возвращается из функции.
"""


def product_of_numbers(list):
    result = 1
    for i in list:
        result *= i
    return result


list_of_integer = [1, 2, 3, 4, 5, 6]
task_1 = product_of_numbers(list_of_integer)
print(f"Произведение всех элементов списка {list_of_integer}: {task_1}")

"""
Задание 2
Напишите функцию для нахождения минимума в
списке целых. Список передаётся в качестве параметра.
Полученный результат возвращается из функции.
"""


def find_minimal(list):
    minimum = list[0]
    for i in range(0, len(list)):
        if list[i] < minimum:
            minimum = list[i]
    return minimum


list_for_minimum = [4, 9, 5, 2, 7, 3]
minimum_result = find_minimal(list_for_minimum)
print(f"Минимльное значение в списке {list_for_minimum}: {minimum_result}")

"""
Задание 3
Напишите функцию, определяющую количество про-
стых чисел в списке целых. Список передаётся в качестве
параметра. Полученный результат возвращается из функции.
"""


def find_prime_numbers(list):
    # prime_numbers = []
    count = 0
    for i in list:
        for j in range(2, i):
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            # prime_numbers.append(i)
            count += 1
    return count


list_for_search_prime_numbers = [10, 2, 5, 7, 12, 25, 67]
print(f"Простых чисел в списке {list_for_search_prime_numbers}: {find_prime_numbers(list_for_search_prime_numbers)}")

"""
Задание 4
Напишите функцию, удаляющую из списка целых
некоторое заданное число. Из функции нужно вернуть
количество удаленных элементов.
"""


def delete_numbers(list, delete_list):
    count = 0
    for i in range(len(list)-1, -1, -1):
        if list[i] in delete_list:
            list.pop(i)
            count += 1
    return list


list_of_numbers = input("Введите числа (через запятую): ").split(', ')
delete = input("Введите числа, которые хотите удалить (через запятую): ").split(', ')
print(f"Количество удаленных элементов в {list_of_numbers}: {delete_numbers(list_of_numbers, delete)}")

"""
Задание 5
Напишите функцию, которая получает два списка в
качестве параметра и возвращает список, содержащий
элементы обоих списков.
"""


def combining_list(list1, list2):
    return list1 + list2


first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9, 0]
print(combining_list(first_list, second_list))

"""
Задание 6
Напишите функцию, высчитывающую степень каждого
элемента списка целых. Значение для степени передаётся
в качестве параметра, список тоже передаётся в качестве
параметра. Функция возвращает новый список, содержа-
щий полученные результаты.
"""


def exponentiation_list(list, degree):
    from math import pow
    for i in range(0, len(list)):
        list[i] = pow(list[i], degree)
    return list


list_for_exponentiation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
degree_for_exponentiation = 2
print(f"Список {list_for_exponentiation} в степени {degree_for_exponentiation}: "
      f"{exponentiation_list(list_for_exponentiation, degree_for_exponentiation)}")
