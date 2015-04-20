#!/usr/bin/env python
# coding: utf8
__author__ = 'Fuze'


def bubble_sort(list_of_number):
    times = 0
    length = len(list_of_number)
    for i in range(length):
        print '*' * 20 + '%dth loop' % i + '*' * 20
        for j in range(length - i - 1):
            times += 1
            print '-' * 20 + '%dth compare' % j + '-' * 20
            if list_of_number[j] > list_of_number[j + 1]:
                list_of_number[j], list_of_number[j + 1] = list_of_number[j + 1], list_of_number[j]
            else:
                continue
            print list_of_number
    print "Total compare %d times" % times


if __name__ == '__main__':
    bubble_sort([49, 38, 65, 97, 76, 13, 27, 49, 5, 04])