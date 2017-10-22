# -*- coding: utf-8 -*-
import itertools
import operator

PRE_MAX = 33
POST_MAX = 16

# combination = list(itertools.combinations([i for i in range(1, PRE_MAX + 1)], 6))
# len_combination = len(combination)


# permutation = list(itertools.permutations([i for i in range(1, PRE_MAX + 1)], 6))
# len_permutation = len(permutation)


def c(n, k):
    if k != 0:
        return reduce(operator.mul, range(n - k + 1, n + 1)) / reduce(operator.mul, range(1, k + 1))
    else:
        return 1


def a(n, k):
    if k == 0:
        return 1
    else:
        return reduce(operator.mul, range(n - k + 1, n + 1))


def fac(n):
    return reduce(operator.mul, range(1, n + 1))


def permutation_order(data):
    sum = 0
    for i in range(1, 7):
        for num in range(1, data[i - 1]):
            if num in data[:(i - 1)]:
                continue
            part_sum = a(PRE_MAX - i, 6 - i)
            # print '.............{}'.format(i, ), part_sum
            sum += part_sum
    return sum
print permutation_order([33,32,31,30,29,28]) * 16

def combination_order(data):
    sum = 0
    for i in range(1, 7):
        part_sum = 0
        if i == 1:
            for num in range(1, data[i - 1]):
                part_sum += c(PRE_MAX - num, 6 - i)
        else:
            for num in range(data[i - 2] + 1, data[i - 1]):
                part_sum += c(PRE_MAX - num, 6 - i)
        sum += part_sum
    return sum

# data = [33, 32, 31, 30, 29, 28]
# data = [6,7,8,9,10,11]

# for i in range(len_combination):
#     sum = combination_order(combination[i])
#     # if i != sum:
#     print 'i is {}, and sum is {}, and list is {}'.format(i, sum, combination[i])
# print len_combination, ',,,,,,,,,,,,,,,,'

# for i in range(len_permutation):
#     sum = permutation_order(permutation[i])
#     if i != sum:
#         print 'i is {}, and sum is {}, and list is {}'.format(i, sum, permutation[i])
#
# print len_permutation, ',,,,,,,,,,,,,,,,'