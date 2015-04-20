#!/usr/bin/env python

__author__ = 'fuze'

def InsertSort(number_list):
    if not isinstance(number_list, list):
        return "Input should be a list of number"
    lenth = len(number_list)
    for i in xrange(1, lenth):
        if number_list[i]<number_list[i-1]:
            temp = number_list[i]
            number_list[i] = number_list[i-1]
            pos = i-1
            while(number_list[pos]>temp and pos>-1):
                number_list[pos+1] = number_list[pos]
                pos -= 1
            number_list[pos+1] = temp
        print str(i) + ' : ' + str(number_list)

if __name__=='__main__':
    NumberList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print "0 : " + str(NumberList)
    InsertSort(NumberList)


