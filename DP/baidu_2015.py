__author__ = 'Fuze'


def hunger_dp():
    loop_times = input()
    for times in range(loop_times):
        this_max = 0
        rest, bot, top = (int(item) for item in raw_input().split())
        for each_rest in range(rest):
            temp = []
            this_rest = [int(item) for item in raw_input().split()]
            for i in range(this_rest[0]):
                price = this_rest[i * 2 + 1]
                value = this_rest[i * 2 + 2]
                temp.append([0] * (top + 1))
                if i == 0:
                    for j in range(price, top + 1):
                        temp[i][j] = value
                else:
                    for j in range(price, top + 1):
                        temp[i][j] = max(temp[i - 1][j - price] + value, temp[i - 1][j])
            r_max = max(temp[-1])
            r_price = temp[-1].index(r_max)
            if r_price >= bot and r_max > this_max:
                this_max = r_max
        print this_max

hunger_dp()
