import functools
import math
import winsound


# ex1.1.3:

# def divide_by_4(number):
#     return number % 4 == 0
#
#
# def four_dividers(number):
#     return list(filter(divide_by_4, range(1, number + 1)))


# print(four_dividers(12))
# print(four_dividers(3))


# ex1.1.4:
# def add(a, b):
#     return int(a) + int(b)
#
#
# def sum_of_digits(number):
#     return functools.reduce(add, str(number))
#
#
# print(sum_of_digits(268))

# פתרון למטבעות - חשבתי בעצמי!
# def combine_coins(symbol, num_list):
#     return ', '.join(symbol + str(i) for i in num_list)


#
#
# print(combine_coins('$', range(5)))


# ex1.3.1:
# def intersection(list_1, list_2):
#     return list(set(i for i in list_2 if i in list_1))
#
#
# print(intersection([1, 2, 3, 4], [8, 3, 9]))
# print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

# ex1.3.2:
# def is_prime(number):
#     return len([i for i in range(2, number) if number % i == 0]) == 0
#
#
# print(is_prime(42))
# print(is_prime(43))

# ex1.3.3:
# def is_funny(string):
#     return False not in set(False if char != 'h' and char != 'a' else True for char in string)
#
#
# print(is_funny("hahahahahaha"))
# print(is_funny("hahahahaggghaha"))


# ex1.3.4:

# password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
# print(''.join([chr(ord(char) + 2) for char in password]))


# ex3.3.2:

# class UnderAge(Exception):
#     def __init__(self, arg):
#         self._arg = arg
#
#     def __str__(self):
#         return "You are under 18, your age is %d" % self._arg
#
#     def get_arg(self):
#         return self._arg
#
#
# def send_invitation(name, age):
#     try:
#         if int(age) < 18:
#             raise UnderAge(age)
#     except UnderAge as e:
#         print("Function Expected age bigger the 18,"
#               " and instead got %s." % e.get_arg())
#     else:
#         print("You should send an invite to " + name)
#
#
# send_invitation("Elad", 17)

# 4.1.3:
#
# def is_prime(n):
#     # Corner case
#     if n <= 1:
#         return False
#     # Check from 2 to n-1
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# def first_prime_over(n):
#     gen = (i for i in range(n, 10 ** 100) if is_prime(i))
#     print(next(gen))
#
#
# print(first_prime_over(1000000))


# 4.2.2:
# def parse_ranges(ranges_string):
#     gen1 = (i.split('-') for i in ranges_string.split(','))
#     gen2 = (num for i, j in gen1 for num in range(int(i), int(j) + 1))
#     return gen2
#
#
# print(list(parse_ranges("1-2,4-4,8-10")))
# print(list(parse_ranges("0-0,4-8,20-21,43-45")))

# 4.3.4:
# def get_fibo():
#     a0 = 0
#     a1 = 1
#     yield a0
#     while (True):
#         yield a1
#         a1 += a0
#         a0 = a1 - a0
#
#
# fibo_gen = get_fibo()
# for i in range(20):
#     print(next(fibo_gen))


# 5.1.2:
#
# freqs = {"la": 220,
#          "si": 247,
#          "do": 261,
#          "re": 293,
#          "mi": 329,
#          "fa": 349,
#          "sol": 392,
#          }
#
# notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re," \
#         "250-mi,250-fa,250-sol,250-sol,250-sol,500"
#
# scores = notes.split('-')
#
# print(scores)
#
# for i in scores:
#     i = i.split(',')
#     winsound.Beep(freqs[i[0]], int(i[1]))

# 5.2.3:

# def how_many(num20, num10, num5, num1, the_string, wanted_sum):
#     howMany = 0
#     if wanted_sum <= 0:
#         if wanted_sum < 0:
#             return 0
#         print(the_string)
#         return 1
#     if num20 > 0:
#         howMany += how_many(num20 - 1, num10, num5, num1, the_string + " 20", wanted_sum - 20)
#     if num10 > 0:
#         howMany += how_many(num20, num10 - 1, num5, num1, the_string + " 10", wanted_sum - 10)
#     if num5 > 0:
#         howMany += how_many(num20, num10, num5 - 1, num1, the_string + " 5", wanted_sum - 5)
#     if num1 > 0:
#         howMany += how_many(num20, num10, num5, num1 - 1, the_string + " 1", wanted_sum - 1)
#     return howMany
#
#
# print(how_many(3, 5, 2, 5, "", 100))


import antigravity
