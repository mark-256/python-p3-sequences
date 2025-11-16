#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    fib_list = [0]
    if length == 1:
        print(fib_list)
        return
    fib_list.append(1)
    if length == 2:
        print(fib_list)
        return
    for i in range(2, length):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(fib_list)
