def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('error')

print(spam(1))
print(spam(2))
print(spam(0))
