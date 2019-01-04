#! /usr/bin/env python
# @Author : sanyapeng


def get_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)

print(get_fibonacci(12))