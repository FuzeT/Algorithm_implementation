#!/usr/bin/env python
# coding : utf8

__author__ = 'Fuze'


# Todo: Print a list as a tree.
def print_full_tree(lis):
    print lis


def heap_adjust(lis, loc):
    if not isinstance(lis, list):
        raise TypeError, "Input should be a list!"
    if not lis:
        return None
    length = len(lis)
    print loc
    tmp = lis[loc]
    child = loc * 2 + 1
    while child < length:
        if child + 1 < length and lis[child] < lis[child + 1]:
            child += 1
        if tmp < lis[child]:
            lis[loc] = lis[child]
            loc = child
            child = child * 2 + 1
        else:
            break
        lis[loc] = tmp
    return lis


def init_heap(lis):
    length = len(lis)
    for i in range(length / 2, -1, -1):
        heap_adjust(lis, i)
        print '-' * 20 + str(lis)
    return lis


def heap_sort(lis):
    output = []
    length = len(lis)
    lis = init_heap(lis)
    for i in range(length):
        output.append(lis[0])
        lis[0] = lis[-1]
        lis.pop()
        lis = heap_adjust(lis, 0)
        print '*' * 20
        print lis
        print output
    return output


if __name__ == '__main__':
    heap_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])