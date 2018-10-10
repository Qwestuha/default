from itertools import *

""" 
itertools.takewhile(<Функция>, <Последовательность>)

возвращает итератор, в каждой итерации возвращает элемент последовательности, 
пока не встретится элемент, для которой функция, указанная в превом параметре вернет значение False
"""

def more():
    return x > 2

list(itertools.takewhile(more, [3, 4, 6, 9, 1, 2, 5, 7]))
#    Выдаст [3, 4, 6, 9]


list(itertools.takewhile(lambda x: x > 2, [3, 4, 6, 9, 1, 2, 5, 7]))
#    Выдаст [3, 4, 6, 9]
