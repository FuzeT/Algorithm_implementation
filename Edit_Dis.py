__author__ = 'Fuze'

import sys

def Distance(a, b):
    try:
        a = '#'+str(a)
        b = '#'+str(b)
        list_a = tuple(a)
        list_b = tuple(b)
        temp = [0]*(len(list_a))
        max_dis = len(a)+len(b)
        for i in range(0, len(temp)):
            temp[i] = [0]*(len(list_b))
        for i in range(0, len(list_a)):
            for j in range(0, len(list_b)):
                dia = temp[i-1][j-1] if i>0 and j>0 else -max_dis
                left = temp[i][j-1] if j >0 else -max_dis
                upside = temp[i-1][j] if i>0 else -max_dis
                new_value = max(dia, left-1, upside-1) if list_a[i] == list_b[j] else max(dia-1, left-1, upside-1)
                temp[i][j] = new_value
                temp[0][0] = 0
        return temp
    except Exception, e:
        print e

if __name__=='__main__':
    Matrix = Distance(sys.argv[1], sys.argv[2])
    print "The distance between " + str(sys.argv[1]) + " and " + str(sys.argv[2]) + " is : " + str(abs(Matrix[-1][-1]))[root@
