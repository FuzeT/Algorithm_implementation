#!/usr/bin/env python
# coding : utf8

__author__ = 'Fuze'


# Todo: Print a list as a tree.
def print_full_tree(list_of_number):
    print list_of_number


def heap_adjust(list_of_number, loc):
    if not isinstance(list_of_number, list):
        raise TypeError, "Input should be a list!"
    if not list_of_number:
        return None
    length = len(list_of_number)
    print loc
    tmp = list_of_number[loc]
    child = loc * 2 + 1
    while child < length:
        if child + 1 < length and list_of_number[child] < list_of_number[child + 1]:
            child += 1
        if tmp < list_of_number[child]:
            list_of_number[loc] = list_of_number[child]
            loc = child
            child = child * 2 + 1
        else:
            break
        list_of_number[loc] = tmp
    return list_of_number


def init_heap(list_of_number):
    length = len(list_of_number)
    for i in range(length / 2, -1, -1):
        heap_adjust(list_of_number, i)
        print '-' * 20 + str(list_of_number)
    return list_of_number


def heap_sort(list_of_number):
    output = []
    length = len(list_of_number)
    list_of_number = init_heap(list_of_number)
    for i in range(length):
        output.append(list_of_number[0])
        list_of_number[0] = list_of_number[-1]
        list_of_number.pop()
        list_of_number = heap_adjust(list_of_number, 0)
        print '*' * 20
        print list_of_number
        print output
    return output


if __name__ == '__main__':
    heap_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])