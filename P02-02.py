# ############# 11111111111111111
#
# """Сравним цикл и рекурсию"""
#
#
# def get_sum_1(lst_obj):
#     """Простой цикл"""
#
#     res = 0
#     for el in lst_obj:
#         res = res + el
#     return res
#
#
# def get_sum_2(lst_obj):
#     """Простая рекурсия"""
#     # базовый случай!!!
#     if len(lst_obj) == 1:
#         return lst_obj[0]
#     else:
#         # шаг рекурсии
#         return lst_obj[0] + get_sum_2(lst_obj[1:])
#
#
# print(get_sum_1([1, 3, 5, 7, 9]))
# print(get_sum_2([1, 3, 5, 7, 9]))
#
#
# # 1 + get_sum(3, 5, 7, 9)
# # 3 + get_sum(5, 7, 9)
# # 5 + get_sum(7, 9)
# # 7 + get_sum(9)
# # get_sum(9) = 9 - длина равна 1 -> завершаем рекурсивные вызовы
# # и начинаем возвраты
# # 9
# # 7 + 9
# # 5 + 16
# # 3 + 21
# # 1 + 24
# # и получаем 25 и выполняем возврат в главную ветку программы
#
#
# ############ 22222222222222
#
# """Рекурсия против цикла
# Вывод чисел по убыванию, начиная с текущего и до нуля
# """
#
#
# def count_cycle(i):
#     """Цикл"""
#     while i >= 0:
#         print(i)
#         i -= 1
#
#
# count_cycle(3)
#
#
# def count_recur(i):
#     """Рекурсия"""
#     print(i)
#     # базовый случай (шаг завершения рекурс. вызовов)
#     if i <= 0:
#         return
#     # рекурсивный случай (вызов ф-ции из себя)
#     count_recur(i-1)
#
#
# count_recur(3)
#
# """
# 1. Написать базовый случай
# 2. Написать шаг рекурсии
# 3. ПРАВИЛЬНО! определить как изменятся входные аргументы в рекурсивных вызовах
# """
#
# ################ 33333333333333333333333
#
# """Изменение значений переменных"""
#
#
# def recursion(a, b):
#     """Рекурсия"""
#     # базовый случай
#     # последний шаг рекурсии
#     if a == b:
#         return str(a)
#     # шаг рекурсии
#     # рекурсивное условие
#     elif a > b:
#         return f'{a} {recursion(a - 1, b)}'
#     # шаг рекурсии
#     # рекурсивное условие
#     elif a < b:
#         return f'{str(a)} {recursion(a + 1, b)}'
#
#
# print(recursion(20, 15))
# print(recursion(10, 15))
#
# ####################### 4444444444444444444444
#
# """Конвертация"""
#
# import sys
#
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1000000000)
# print(sys.getrecursionlimit())
#
#
# def convert_to_str(n, base_val):
#     convert_str = "0123456789ABCDEF"
#     # Базовый случай, в котором n должно быть меньше,
#     # чем основание, по которому мы конвертируем
#     if n < base_val:
#         return convert_str[n]
#     # Здесь выполняются 2-й и 3-й законы рекурсии
#     # выполняется рекурсивный вызов и происходит
#     # уменьшение размера задания с помощью деления
#     else:
#         return convert_to_str(n // base_val, base_val) + convert_str[n % base_val]
#
#
# print(convert_to_str(5, 2))
# print(convert_to_str(10, 16))
#
# # convert_to_str(5, 2)
# # convert_to_str(2, 2) + 1
# # convert_to_str(1, 2) + 0
# # convert_to_str(1, 2) -> 1
#
# # все!
#
# # 1 + 0
# # 1 + 0 + 1
# # 101
#
# ##################### 5555555555555555555555
#
# """Конвертация в двоичную и 16-ричную системы"""
#
#
# from stack import StackClass
#
# sc_obj = StackClass()
#
#
# def convert_to_str(n, base_val):
#     convert_str = "0123456789ABCDEF"
#
#     while n > 0:
#         if n < base_val:
#             sc_obj.push_in(convert_str[n])
#         else:
#             sc_obj.push_in(convert_str[n % base_val])
#         # стек пополняется и достигает длины 4
#         print(sc_obj.stack_size())
#         n = n // base_val
#
#     res = ""
#     while not sc_obj.is_empty():
#         res = res + str(sc_obj.pop_out())
#     return res
#
#
# print(convert_to_str(5, 2))
# # здесь стек уже пустой. все возвраты выполнены
# print(sc_obj.stack_size())
#
# print(convert_to_str(10, 16))
#
# ############### 6666666666666666666
#
# """Факториал через рекурсию"""
#
# import sys
#
# # print(sys.getrecursionlimit())
# sys.setrecursionlimit(100000)
# # print(sys.getrecursionlimit())
#
#
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(1000))
# # print(factorial(1000))
#
# """
# Рекурсивные функции используют так называемый «Стек вызовов».
# Когда программа вызывает функцию, функция отправляется на верх стека вызовов.
# Это похоже на стопку книг, вы добавляете одну вещь за одни раз.
# Затем, когда вы готовы снять что-то обратно, вы всегда снимаете верхний элемент.
# """
#
# '''
# 0 шаг. Вызов функции: fac(5)
# 1. fac(5) возвращает fac(4) * 5
# 2. fac(4) => fac(3) * 4
# 3. fac(3) => fac(2) * 3
# 4. fac(2) => fac(1) * 2
# 5. fac(1) => fac(0) * 1 (завершение рекурсивных вызовов)
# 6. 1 * 1 - возврат в вызов fac(1) (fac(0) * 1 -> 1 * 1)
# 6. 1 * 2 - fac(2)
# 7. 2 * 3 - fac(3)
# 8. 6 * 4 - fac(4)
# 9. 24 * 5 – fac(5)
# 10. Возврат в основную ветку программы значения 120
# '''
#
# ################## 777777777777777777
#
# """Числа Фибоначчи"""
# import sys
#
#
# sys.setrecursionlimit(10000)
#
#
# def fib(n, summ):
#     if n < 1:
#         return summ
#     return fib(n-1, summ+n)
#
#
# c = 998
# # c = 998 - уже не работает
# # необузданная рекурсия вызывает переполнение стека
# print(fib(c, 0))
#

# ##################### 8888888888888888888
#
#
# import os # тут нужно папки подтягивать из материалов преподавателя
#
#
# def get_directory_files(path):
#     """Функция вывода содержимого директории"""
#     struct = []
#     for file_or_directory in os.listdir(path):
#         full_name = os.path.join(os.path.abspath(path), file_or_directory)
#         if os.path.isfile(full_name):
#             struct.append((os.path.abspath(path), file_or_directory))
#         else:
#             struct.extend(get_directory_files(full_name))
#     return struct
#
#
# my_res = get_directory_files('mainapp')
# print(my_res)
# 
# 
# ###################### 99999999999999999
# 
# """Определение НОД"""
# 
# 
# def first_method(a, b):
#     """Цикл"""
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     print(a)
# 
# 
# first_method(36, 60)
# 
# 
# def second_method(a, b):
#     """Рекурсия"""
#     if b == 0:
#         return a
#     return second_method(b, a % b)
# 
# 
# print(second_method(36, 60))
# 
# 
# def third_method(a, b):
#     """Тоже цикл"""
#     while b != 0:
#        a, b = b, a % b
#     return a
# 
# 
# print(third_method(36, 60))
