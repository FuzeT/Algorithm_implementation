#!/usr/bin/env python
# coding : utf8

__author__ = 'Fuze'


def merge_sort(list_of_number):
    if len(list_of_number) == 1:
        return list_of_number
    else:
        return merge(merge_sort(list_of_number[:len(list_of_number) / 2]),
                     merge_sort(list_of_number[len(list_of_number) / 2:]))


def merge(list_of_number_a, list_of_number_b):
    temp_list = []
    i = j = 0
    while i < len(list_of_number_a) and j < len(list_of_number_b):
        if list_of_number_a[i] < list_of_number_b[j]:
            temp_list.append(list_of_number_a[i])
            i += 1
        elif list_of_number_a[i] > list_of_number_b[j]:
            temp_list.append(list_of_number_b[j])
            j += 1
        else:
            temp_list.append(list_of_number_a[i])
            temp_list.append(list_of_number_b[j])
            i += 1
            j += 1
    temp_list.extend(list_of_number_a[i:])
    temp_list.extend(list_of_number_b[j:])
    return temp_list


if __name__ == '__main__':
    to_test = [49, 38, 65, 97, 76, 13, 27, 49, 5, 04]
    print merge_sort(to_test)
