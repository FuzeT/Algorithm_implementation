#!/usr/bin/env python
# coding: utf8

__author__ = 'Fuze'


def quick_sort(list_of_number, start, end):
    if start < end:
        flag = list_of_number[start]
        pos = start
        phase = 0
        for i in range(start + 1, end):
            if list_of_number[i] < flag:
                list_of_number[pos] = list_of_number[i]
                for j in range(phase):
                    list_of_number[i - j] = list_of_number[i - j - 1]
                pos += 1
            else:
                phase += 1
        list_of_number[pos] = flag
        print list_of_number
        quick_sort(list_of_number, start, pos)
        quick_sort(list_of_number, pos + 1, end)
    else:
        return list_of_number


if __name__ == '__main__':
    to_test = [49, 38, 65, 97, 76, 13, 27, 49, 5, 04]
    quick_sort(to_test, 0, len(to_test))