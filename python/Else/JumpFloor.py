#!/usr/bin/env python
# coding: utf8

__author__ = 'Fuze'

ways = 0


def jump(target, current=0):
    try_left(target, current)
    try_right(target, current)
    return ways


def try_left(target, current=0):
    global ways
    temp = current
    temp += 1
    if temp == target:
        ways += 1
        return None
    elif temp > target:
        return None
    else:
        try_left(target, temp)
        try_right(target, temp)


def try_right(target, current=0):
    global ways
    temp = current
    temp += 2
    if temp == target:
        ways += 1
        return None
    elif temp > target:
        return None
    else:
        try_left(target, temp)
        try_right(target, temp)


# Second edition
def jump_floor(target):
    if target < 0:
        return None
    return 1 if target <= 1 else jump_floor(target - 1) + jump_floor(target - 2)
