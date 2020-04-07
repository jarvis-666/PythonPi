"""
This is my attempt at learning how to use the Chudnovsky Algorithm to estimate the value of PI
Thanks to the author Pradipta (geekpradd) for her code
"""

import math
from decimal import *
import sys

sys.setrecursionlimit(100000)
getcontext().rounding = ROUND_FLOOR


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def get_iter(k):
    k += 1
    getcontext().prec = k
    sum_iter = 0
    for k in range(k):
        up = factorial(6*k) * (545140134 * k + 13591409)
        down = factorial(3*k) * (factorial(k))**3 * (-262537412640768000) ** k
        sum_iter += (up / down)
    return Decimal(sum_iter)


def pi_value(k):
    up = 426880 * math.sqrt(10005)
    iter = get_iter(k)
    pi = Decimal(up) / iter
    return pi


def shell():
    """
    function to create an interactive shell
    This only runs when the script is being run directly
    Otherwise this script can be imported and its function can be useful to calculate the value
    :return: None
    """
    print("Welcome to the PI calculator. Enter the number of decimal places to estimate the value of pi or enter quit to exit")
    while True:
        print(">>>", end="")
        entry = input()
        if entry == "quit":
            print("Thanks...")
            break
        elif not entry.isdigit():
            print("You did not enter a number, try again...")
        else:
            print(pi_value(int(entry)))


if __name__ == '__main__':
    shell()
