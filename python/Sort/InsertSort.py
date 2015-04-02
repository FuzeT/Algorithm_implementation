#!/usr/bin/env python

__author__ = 'fuze'

def InsertSort(list_of_number):
    if not isinstance(list_of_number, list):
        return "Input should be a list of number"
    lenth = len(list_of_number)
    for i in xrange(1, lenth):
        if list_of_number[i]<list_of_number[i-1]:
            temp = list_of_number[i]
            list_of_number[i] = list_of_number[i-1]
            pos = i-1
            while(list_of_number[pos]>temp and pos>-1):
                list_of_number[pos+1] = list_of_number[pos]
                pos -= 1
            list_of_number[pos+1] = temp
        print str(i) + ' : ' + str(list_of_number)

if __name__=='__main__':
    NumberList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print "0 : " + str(NumberList)
    InsertSort(NumberList)


