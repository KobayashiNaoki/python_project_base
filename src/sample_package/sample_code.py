def add_one(x: int):
    return x + 1


def add_one_cli():
    print('Please enter an integer. This script returns the value with 1 added.')
    x = int(input())
    print(add_one(x))
    return 0
