#!/usr/bin/env python

import copy

__author__ = 'fuze'

def shell_insert(number_list):
    times = 1
    lenth = len(number_list)
    pos_range = lenth/(2**times)
    while (pos_range > 0):
        for group in xrange(0, lenth/(lenth/pos_range)):
            for i in xrange(group + pos_range, lenth, pos_range):
                if number_list[i - pos_range] > number_list[i]:
                    temp_value = number_list[i]
                    number_list[i] = number_list[i - pos_range]
                    pos_now = i - pos_range
                    while(number_list[pos_now] > temp_value and pos_now > -1):
                        number_list[pos_now + pos_range] = number_list[pos_now]
                        pos_now -= pos_range
                    number_list[pos_now + pos_range] = temp_value
            print str(times) + " of group " + str(group) + " : " + str(number_list) + "       pos_range is      " + str(pos_range)
        times += 1
        pos_range = lenth/(2**times)

if __name__ == '__main__':
    to_test = [49, 38, 65, 97, 76, 13, 27, 49, 5, 04]
    print "0 : " + str(to_test)
    shell_insert(to_test)
