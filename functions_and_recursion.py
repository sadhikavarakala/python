'''
cities = ["new york", "jc", "denver", "DC"]
heroes = ["superman", "batman", "flash", "spiderman", "ironman"]

def print_len(list):
    print(len(list))

print_len(heroes)
print_len(cities)

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print()

# factorial func

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(7)

# convert to usd to inr

def converter(usd_val):
    inr_val = usd_val * 86
    print(usd_val, "USD =", inr_val, "INR")

converter(500)

# Recursion: when a function calls itself repeatedly

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(9)
print(sum)

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruits = ['mango', 'banana', 'orange']

print_list(fruits)
'''

# lru cache - most recently used cache, memoize
# caches the result of a function call to avoid recomputation, huge performance boost
# counts vowels in a string

from functools import lru_cache

import timing_decorator

# @lru_cache(maxsize=128, typed=False)
# def count_vowels(sentence: str) -> int:
#     return sum(sentence.count(vowel) for vowel in 'aeiouAEIOU')

# @timing_decorator.time_function
# def main() -> None:
#     sentences: list[str] = ['Hello, world',
#                             'I dunno, must be a good day',
#                             'I love python']
    
#     for sentence in sentences:
#         for i in range(1_000_000):
#             count_vowels(sentence)

# if __name__ == "__main__":
#     main()
#     print(count_vowels.cache_info())
#     count_vowels.cache_clear()

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timing_decorator.time_function
def main() -> None:
    result: int = fibonacci(40)
    print(result)

if __name__ == "__main__":
    main()

print(fibonacci.cache_info())