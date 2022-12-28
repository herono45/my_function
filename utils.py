"""
2022/12/28
Taewook Choi
utils.py
"""


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)


print(factorial(8))

