from itertools import *
ОПА ОПА ЛЯЛЯЛА Я СЛОМАЛ ТВОЮ ПРОГУ
""" 
itertools.takewhile(<Функция>, <Последовательность>)

возвращает итератор, в каждой итерации возвращает элемент последовательности, 
пока не встретится элемент, для которой функция, указанная в превом параметре вернет значение False
"""

def more():
    return x > 2

list(takewhile(more, [3, 4, 6, 9, 1, 2, 5, 7]))
#    Выдаст [3, 4, 6, 9]


list(takewhile(lambda x: x > 2, [3, 4, 6, 9, 1, 2, 5, 7]))
#    Выдаст [3, 4, 6, 9]
