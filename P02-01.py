# # Task 1:
# """
# Вычисление суммы первых n целых чисел
# """
#
# def get_sum_1(n):
#     """
#     В основе идеи алгоритма - переменная-счетчик, инициализируемая нулем
#     и к которой в процессе решения задачи прибавляются числа, перебираемые в цикле
#     :param n:
#     :return:
#     """
#     res = 0
#     for i in range(1, n + 1):
#         res = res + i
#     return res
#
#
# print(get_sum_1(10))
#
#
# def get_sum_2(obj):
#     """
#     Текущее решение является неудачным из-за избыточного присваивания,
# а также неудачного выбора имен переменных
#     :param obj:
#     :return:
#     """
#     var = 0
#     for part in range(1, obj + 1):
#         dec = part
#         var = var + dec
#     return var
#
#
# print(get_sum_2(10))
#
# #Task 2:
# """
# Проведение сравнительных замеров
# """
#
# import time
#
# def check_1(n):
#     """
#     Фиксируем отсечки времени до и после выполнения основной логики
#     :param n:
#     :return: кортеж из результата ф-ции и затраченного времени
#     """
#
#     start_val = time.time()
#     res = 0
#
#     for i in range(1, n + 1):
#         res = res + i
#
#     end_val = time.time()
#
#     return res, end_val - start_val
#
#
# # результат хорошо повторяем
# # для n = 10000
# # затрачивается примерно 0.000979 сек
# for i in range(5):
#     print(f'Операция заняла {check_1(10000)[1]} сек')
#
# print()
# # для n = 100000
# # затрачивается примерно 0.005877 сек
# for i in range(5):
#     print(f'Операция заняла {check_1(100000)[1]} сек')
#
# print()
# # для n = 100000
# # затрачивается примерно 0.065629 сек
# for i in range(5):
#     print(f'Операция заняла {check_1(1000000)[1]} сек')
#
# """
# На различных итерациях цикла даже на одной и той же машине
# мы получаем различные результаты. Почему?
#
# Влияют многие факторы:
# 1) версия интерпретатора
# 2) разрядность ОС
# 3) текущая нагрузка процессора
# """
#
# # Получается абсолютные цифры различаются и на что же ориентироваться?
# # Можно выполнить подсчет средней величины времени
# # Хотя есть еще один вариант оценки, не привязанный к абсолютным цифрам
# # Но об этом позже
#
# #Task 3:
# """
# Теперь воспользуемся формулой (n*(n+1))/2
# """
#
# import time
#
#
# def check_3(n):
#
#     start_val = time.time()
#
#     end_val = time.time()
#
#     return (n*(n+1))/2, end_val - start_val
#
#
# print(check_3(10))
#
#
# for i in range(5):
#     print(f'Операция заняла {check_3(10000)[1]} сек')
#
# """
# Стоит обратить внимание, что какое бы значение n мы не передали в функцию,
# итоговое время окажется экстремальном малым
#
# Намного эффективнее других вариантов, не правда ли?
#
# Давайте выявим некоторые особенности первых двух решений.
# 1) Они итеративные, а такие решения из-за повторения некоторого набора шагов потребуют больше времени.
# 2) Также мы заметили, что время итеративного решения увеличивается с ростом входного значения n
#
# Вроде все понятно. Нужно использовать третий вариант. Но и здесь оказывается не все так просто.
# Если запустить третью ф-цию на разных машинах или реализовать алгоритм этой ф-ции на других языках программирования,
# то результаты скорее всего не будут идентичными. Чем старше будет машина, тем больше потребуется времени.
#
#
# Теперь понятно, что получать оценку времени в цифровом выражении не так уж хорошо, ведь это время зависит от конкретной машины, программы, времени дня, компилятора и языка программирования.
# Было бы хорошо подобрать характеристику, не зависящую от этих параметров, но дающую понятные результаты.
#
# Чтобы мы могли бы применить эту характеристику для оценки алгоритма самого по себе
# и сравнения одного алгоритма с другими.
# """
#
# # Task 4:
# """Проверка сложности"""
#
# # первые три присваивания - это константа (3)
# VAL_A = 5 # O(1)
# VAL_B = 6
# VAL_C = 10
#
# # три присваивания выполняются n2 раз внутри вложенной итерации (3n^2)
# n = 10
# for i in range(n):
#     for j in range(n):
#         x = i * i
#         y = j * j
#         z = i * j
#
# # два присваивания, повторяющиеся n раз (2n)
# for k in range(n):
#     w = VAL_A*k + 45
#     v = VAL_B*VAL_B
#
# # последний оператор присваивания (1)
# VAL_D = 33
#
# # T(n)=3+3n**2+2n+1=3n**2+2n+4
# # O(n**2)
#
# # Task 5:
#
# """
# Сложность: O(1)
# Название: постоянное время (сложность - константа)
#
# Время работы алгоритма не зависит от объема входящих данных
# """
#
#
# first_lst = ["one", "two", "three", "four"]
# second_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
#
# def get_lst_func(lst):
#     length = len(lst) # O(1)
#     return length # O(1)
#
#
# print(get_lst_func(first_lst))
# print(get_lst_func(second_lst))
#
#
# # Task 6:
#
# """
# Сложность: O(log n) (основанием здесь можно пренебречь)
# Название: логарифмическое время
#
# Яркий пример – двоичный (бинарный) поиск
#
# В отсортированном наборе данных выбирается серединный элемент и
# сравнивается с искомым значением.
# Если значение совпадает, поиск завершен.
#
# Если искомое значение больше, чем значение серединного элемента,
# нижняя половина набора данных (все элементы с меньшими значениями,
# чем у нашего серединного элемента) отбрасывается и
# дальнейший поиск ведется тем же способом в верхней половине.
#
# Если искомое значение меньше, чем значение серединного элемента,
# дальнейший поиск ведется в нижней половине набора данных.
#
# Эти шаги повторяются, при каждой итерации отбрасывая половину элементов,
# пока не будет найдено искомое значение или пока оставшийся набор
# данных станет невозможно разделить напополам:
# """
#
#
# def binary_search(lst, number):
#     start = 0
#     end = len(lst) - 1
#
#     while start <= end:
#         mid = int((start + end) / 2)
#         if lst[mid] == number:
#             return True
#         elif lst[mid] < number:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return False
#
#
# def find_number(lst, number):
#     flag = 0
#     for el in lst:
#         if binary_search(el, number):
#             flag += 1
#     if flag == 0:
#         return "Искомое число не найдено"
#     else:
#         return f"Искомое число встречается в {flag} коллекциях"
#
#
#
# number_lst = [[1, 3, 4, 2, 5, 7, 6, 8, 9], [1, 3, 4, 2, 5, 7, 6, 8, 9], [
#     1, 3, 4, 2, 5, 7, 6, 8, 9], [1, 3, 4, 2, 7, 6, 8, 9]]
# searched_number = 5
#
# print(find_number(number_lst, searched_number))
#
#
# # Task 7:
#
# """
# Сложность: O(n)
# Название: линейная сложность
#
# Время возрастает линейно и прямо пропорционально количеству передаваемых данных
# """
#
#
# first_lst = ["one", "two", "three", "four"]
# second_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
#
# def get_lst_func(lst):
#     for el in lst:
#         print(el)
#
#
# get_lst_func(first_lst)
# print()
# get_lst_func(second_lst)
#
#
# # Task 8:
#
# """
# Сложность: O(n^2)
# Название: квадратичная сложность
#
# Квадратичное время представляет алгоритм,
# производительность которого прямо пропорциональна квадрату размера входящих данных
#
# Распространенный пример такого алгоритма — цикл, вложенный в другой цикл.
# По мере увеличения вложенности растет и временная сложность (O(n^3), O(n^4) и т. д.).
# """
#
#
# obj_lst = [[1, 'one'], [2, 'two'], [3, 'three'], [4, 'four']]
#
#
# def get_lst_func(lst):
#     for el_lst in lst:
#         for el in el_lst:
#             print(el)
#
#
# get_lst_func(obj_lst)
#
#
# # Task 9:
#
# """
# Сложность: O(2^n)
# Название: экспоненциальная
#
# Время работы такого алгоритма удваивается с
# каждым очередным дополнением к набору данных
# Кривая роста этой функции экспоненциальная:
# сначала она очень пологая, а затем стремительно поднимается вверх.
#
# Примером алгоритма с экспоненциальной сложностью может послужить рекурсивный расчет чисел Фибоначчи
# """
#
#
# def fibo_recur(number):
#     if number <= 1:
#         return number
#     return fibo_recur(number - 2) + fibo_recur(number - 1)
#
#
# print(fibo_recur(6))
#
# # для number = 6 результат 8 - 0, 1, 1, 2, 3, 5, 8
#
# # Task 10:
#
# """
# Сложность: O(n!) (основанием здесь можно пренебречь)
# Название: факториальное время
#
# Яркий пример: Задача коммивояжера
#
# Это факториальная временная сложность.
# Каждое действие требует вычисления всех перестановок в коллекции
# и итоговое время выполнения действия вычисляется как факториал исходной коллекции
# Это очень большое расчетное время и неоптимальный алгоритм
#
# Рассмотрим пример, в котором выводятся все возможные комбинации элементов списка
# В основе алгоритма выбор на каждом этапе пары элементов,
#  чтобы выполнить каждую замену этих элементов только один раз
#
# Итоговое время будет расти факториальным образом,
# в зависимости от размера входных данных, поэтому мы можем сказать,
# что алгоритм имеет факторную сложность времени O(n!).
# """
#
#
# def func_calc(lst, n):
#     if n == 1:
#         print(lst)
#         return
#
#     for i in range(n):
#         func_calc(lst, n - 1)
#         if n % 2 == 0:
#             lst[i], lst[n - 1] = lst[n - 1], lst[i]
#         else:
#             lst[0], lst[n - 1] = lst[n - 1], lst[0]
#
#
# lst = [1, 2, 3]
# func_calc(lst, len(lst))
#
# # Task 11:
#
# """Пример создания стека через ООП"""
#
#
# class StackClass:
#     def __init__(self):
#         self.elems = []
#
#     def is_empty(self):
#         return self.elems == []
#
#     def push_in(self, el):
#         """Предполагаем, что верхний элемент стека находится в конце списка"""
#         self.elems.append(el)
#
#     def pop_out(self):
#         return self.elems.pop()
#
#     def get_val(self):
#         return self.elems[len(self.elems) - 1]
#
#     def stack_size(self):
#         return len(self.elems)
#
#
# SC_OBJ = StackClass()
#
# print(SC_OBJ.is_empty())  # -> стек пустой
#
# # наполняем стек
# SC_OBJ.push_in(10)
# SC_OBJ.push_in('code')
# SC_OBJ.push_in(False)
# SC_OBJ.push_in(5.5)
#
# # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
# print(SC_OBJ.get_val())  # -> 5.5
#
# # узнаем размер стека
# print(SC_OBJ.stack_size())  # -> 4
#
# print(SC_OBJ.is_empty())  # -> стек уже непустой
#
# # кладем еще один элемент в стек
# SC_OBJ.push_in(4.4)
#
# # убираем элемент с вершины стека и возвращаем его значение
# print(SC_OBJ.pop_out())  # -> 4.4
#
# # снова убираем элемент с вершины стека и возвращаем его значение
# print(SC_OBJ.pop_out())  # -> 5.5
#
# # вновь узнаем размер стека
# print(SC_OBJ.stack_size())  # -> 3
#
# # Task 12:
#
# """Пример создания стека через ООП"""
#
#
# class StackClass:
#     def __init__(self):
#         self.elems = []
#
#     def is_empty(self):
#         return self.elems == []
#
#     def push_in(self, el):
#         """Предполагаем, что верхний элемент стека находится в начале списка"""
#         self.elems.insert(0, el)
#
#     def pop_out(self):
#         return self.elems.pop(0)
#
#     def get_val(self):
#         return self.elems[0]
#
#     def stack_size(self):
#         return len(self.elems)
#
#
# SC_OBJ = StackClass()
#
# print(SC_OBJ.is_empty())  # -> стек пустой
#
# # наполняем стек
# SC_OBJ.push_in(10)
# SC_OBJ.push_in('code')
# SC_OBJ.push_in(False)
# SC_OBJ.push_in(5.5)
#
# # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
# print(SC_OBJ.get_val())  # -> 5.5
#
# # узнаем размер стека
# print(SC_OBJ.stack_size())  # -> 4
#
# print(SC_OBJ.is_empty())  # -> стек уже непустой
#
# # кладем еще один элемент в стек
# SC_OBJ.push_in(4.4)
#
# # убираем элемент с вершины стека и возвращаем его значение
# print(SC_OBJ.pop_out())  # -> 4.4
#
# # снова убираем элемент с вершины стека и возвращаем его значение
# print(SC_OBJ.pop_out())  # -> 5.5
#
# # вновь узнаем размер стека
# print(SC_OBJ.stack_size())  # -> 3
#
# # Task 13:
#
# #from task_11 import StackClass (это если все задания в отдельных файлах) или копируем и вставляем из Task 11:
#
# class StackClass:
#     def __init__(self):
#         self.elems = []
#
#     def is_empty(self):
#         return self.elems == []
#
#     def push_in(self, el):
#         """Предполагаем, что верхний элемент стека находится в конце списка"""
#         self.elems.append(el)
#
#     def pop_out(self):
#         return self.elems.pop()
#
#     def get_val(self):
#         return self.elems[len(self.elems) - 1]
#
#     def stack_size(self):
#         return len(self.elems)
#
# def divide_by_two(dec_number):
#     sc_obj = StackClass()
#
#     while dec_number > 0:
#         res = dec_number % 2
#         sc_obj.push_in(res)
#         dec_number = dec_number // 2
#
#     bin_string = ""
#     while not sc_obj.is_empty():
#         bin_string = bin_string + str(sc_obj.pop_out())
#
#     return bin_string
#
#
# print(divide_by_two(233)) # перевод в двоичную систему числа 233
#
# # Task 14:
#
# class QueueClass:
#     def __init__(self):
#         self.elems = []
#
#     def is_empty(self):
#         return self.elems == []
#
#     def to_queue(self, item):
#         self.elems.insert(0, item)
#
#     def from_queue(self):
#         return self.elems.pop()
#
#     def size(self):
#         return len(self.elems)
#
#
# if __name__ == '__main__':
#     qc_obj = QueueClass()
#     print(qc_obj.is_empty())  # -> True. Очередь пустая
#
#     # помещаем объекты в очередь
#     qc_obj.to_queue('my_obj')
#     qc_obj.to_queue(4)
#     qc_obj.to_queue(True)
#
#     print(qc_obj.is_empty())  # -> False. Очередь пустая
#
#     print(qc_obj.size())  # -> 3
#
#     print(qc_obj.from_queue())  # -> my_obj
#
#     print(qc_obj.size())  # -> 2
#
# # Task 15:
#
# # from task_14 import QueueClass (это если все задания в отдельных файлах) или копируем и вставляем из Task 14:
#
# class QueueClass:
#     def __init__(self):
#         self.elems = []
#
#     def is_empty(self):
#         return self.elems == []
#
#     def to_queue(self, item):
#         self.elems.insert(0, item)
#
#     def from_queue(self):
#         return self.elems.pop()
#
#     def size(self):
#         return len(self.elems)
#
#
# def hot_potato(names_lst, num):
#     queue_obj = QueueClass()
#     for name in names_lst:
#         queue_obj.to_queue(name)
#
#     while queue_obj.size() > 1:
#         for i in range(num):
#             queue_obj.to_queue(queue_obj.from_queue())
#
#         queue_obj.from_queue()
#
#     return queue_obj.from_queue()
#
#
# print(hot_potato(["Вася", "Петя", "Света", "Жанна", "Катя", "Лена"], 7))
#
# # Task 16:
#
# class DequeClass:
#     def __init__(self):
#         self.elems = []
#
#     def is_empty(self):
#         return self.elems == []
#
#     def add_to_front(self, elem):
#         self.elems.append(elem)
#
#     def add_to_rear(self, elem):
#         self.elems.insert(0, elem)
#
#     def remove_from_front(self):
#         return self.elems.pop()
#
#     def remove_from_rear(self):
#         return self.elems.pop(0)
#
#     def size(self):
#         return len(self.elems)
#
#
# dc_obj = DequeClass()
# print(dc_obj.is_empty())  # -> True
#
# # добавить элементы в хвост
# dc_obj.add_to_rear(10)
# dc_obj.add_to_rear('my_str')
#
# # добавить элементы в голову
# dc_obj.add_to_front(None)
# dc_obj.add_to_front(True)
#
# # размер дека
# print(dc_obj.size())  # -> 4
# print(dc_obj.is_empty())  # -> False
#
# # добавить элемент в хвост
# dc_obj.add_to_rear(3.3)
#
# print(dc_obj.remove_from_rear())  # -> 3.3
# print(dc_obj.remove_from_front())  # -> True
#
# # Task 17:
#
# # from task_16 import DequeClass (это если все задания в отдельных файлах) или копируем и вставляем из Task 16:
#
# class DequeClass:
#     def __init__(self):
#         self.elems = []
#
#     def is_empty(self):
#         return self.elems == []
#
#     def add_to_front(self, elem):
#         self.elems.append(elem)
#
#     def add_to_rear(self, elem):
#         self.elems.insert(0, elem)
#
#     def remove_from_front(self):
#         return self.elems.pop()
#
#     def remove_from_rear(self):
#         return self.elems.pop(0)
#
#     def size(self):
#         return len(self.elems)
#
#
# def pal_checker(string):
#     dc_obj = DequeClass()
#
#     for el in string:
#         dc_obj.add_to_rear(el)
#
#     still_equal = True
#
#     while dc_obj.size() > 1 and still_equal:
#         first = dc_obj.remove_from_front()
#         last = dc_obj.remove_from_rear()
#         if first != last:
#             still_equal = False
#
#     return still_equal
#
#
# print(pal_checker("топот"))