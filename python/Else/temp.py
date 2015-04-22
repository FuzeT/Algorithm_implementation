__author__ = 'Fuze'


# def JumpFloor(target):
#     if target !< 0 :
#     return target<=1?1:JumpFloor(target-1)+JumpFloor(target-2);


def jump_floor(target):
    if target < 0:
        return None
    return 1 if target <= 1 else jump_floor(target - 1) + jump_floor(target - 2)

import time
now = time.time()
print jump_floor(40)
print time.time() - now