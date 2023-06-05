from collections import Counter
from math import factorial as fact

pi = 22 / 7
cache_fib = {1: 0, 2: 1}


def remove_value_from_list(sam_list, *value):
    """Remove given value from list"""
    return [i for i in sam_list if i not in value]


def reverse_string0(string):
    """Reverse given string
        \nInput must be string and output is a string"""
    return "".join(map(str, list(string).__reversed__()))


def reverse_string1(string: str) -> str:
    """Reverse given string
        \nInput must be string and output is a string"""
    return string[::-1]


def is_prime0(num):
    """Return boolean value of given number as a prime or not"""
    return not (bool(len([i for i in range(2, num) if num % i == 0])))


def is_prime1(num):
    """Return boolean value of given number as a prime or not"""
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime2(num):
    """Return boolean value of given number as a prime or not"""
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def rem_sub_str0(string, sub_string):
    """Remove substring in the given string"""
    return string[:string.find(sub_string)] + string[string.find(sub_string) + len(sub_string):]


def rem_sub_str1(string: str, sub_string):
    """Remove substring in the given string"""
    return string.replace(sub_string, "", 1)


def rem_dup_list0(sam_list: list):
    """Remove duplicates items in given list and return as a list"""
    out = list()
    for i in sam_list:
        if i not in out:
            out.append(i)
    return out


def rem_dup_list1(sam_list: list):
    """Remove duplicates items in given list and return as a list"""
    return list(dict.fromkeys(sam_list))


def count_element0(val: list):
    """Count element in the given list and return values and count as a dict"""
    out = dict()
    for i in val:
        if i in out.keys():
            out[i] = out.get(i) + 1
        else:
            out[i] = 1
    return out


def count_element1(val):
    """Count element in the given list and return values and count as a dict"""
    return dict(Counter(val))


def find_key0(dict0: dict, value):
    """Find key by value in given dictionary"""
    temp = list()
    for i in dict0.keys():
        if dict0.get(i) == value:
            temp.append(i)
    if len(temp) != 1:
        return temp
    else:
        return temp[0]


def find_key1(dict0, value):
    """Find key by value in given dictionary"""
    return [k for k, v in dict0.items() if v == value]


def least_common_mul(num_list: list) -> int:
    max_num = max(num_list)
    temp = 1
    temp_list = list()
    while True:
        num_list = [i for i in num_list if i != 1]
        if len(num_list) == 0:
            break
        for i in range(2, 1 + max_num):
            if num_list[0] % i == 0:
                temp *= i
                for j in num_list:
                    if j % i == 0:
                        temp_list.append(j // i)
                    else:
                        temp_list.append(j)
                num_list.clear()
                num_list = num_list + temp_list
                temp_list.clear()
    return temp


def fib0(num: int):
    temp = [0, 1]
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        for i in range(num - 2):
            temp.append(temp[-1] + temp[-2])
        return temp[-1]


def fib1(num: int) -> int:
    """Optimized Fibonacci sequence implementation using memoization."""
    if num in cache_fib:
        return cache_fib[num]
    else:
        cache_fib[num] = fib1(num - 2) + fib1(num - 1)
        return cache_fib[num]


def p(n: int, r: int):
    """Calculate Permutation, p(n,r) wil return n!/(n-r)!"""
    try:
        return fact(n) // fact(n - r)
    except Exception as e:
        return e


def c(n: int, r: int):
    """Calculate Combination, c(n,r) wil return n!/r!(n-r)!"""
    try:
        return fact(n) // (fact(r) * fact(n - r))
    except Exception as e:
        return e
