import os
from datetime import datetime
import types

# Задание 3 Часть 1

def logger(old_function):

    def new_function(*args, **kwargs):
        with open('main.log', 'a') as log_file:
            log_file.write(f"Время: {datetime.now()} Имя функции: '{old_function.__name__}' Аргументы при вызове. args: {args}, kwargs: {kwargs} ")
        result = old_function(*args, **kwargs)
        with open('main.log', 'a') as log_file:
            log_file.write(f'Результат: {result}' + '\n')
        return result
    return new_function


class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.row_index = 0
        self.col_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.row_index >= len(self.list_of_lists):
            raise StopIteration

        sublist = self.list_of_lists[self.row_index]
        if self.col_index >= len(sublist):
            self.row_index += 1
            self.col_index = 0
            return next(self)

        item = sublist[self.col_index]
        self.col_index += 1
        return item
@logger
def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



if __name__ == '__main__':
    test_1()
