def func1(list_):
    list_.insert(0, 'start')
    list_.insert(0, 'Element')
    list_.append('finish')
    return list_


print(func1(['hello', 5, 'John']))


def func2(*args):
    a = list(args)
    # b = {x: [y for y in range(1, len(a))] for x in args}
    b = {}
    j = 1
    for i in range(len(a)):
        b[a[i]] = j
        j += 1
    return b


print(func2(5, 'qwe', 'John'))


def func3(tuple_):
    lst = list(tuple_)
    a = list(filter(lambda x: x % 2 == 0, lst))
    b = list(map(lambda x: x ** 2, lst))
    return a, b


a, b = func3((1, 2, 3, 4, 5))
print(a)
print(b)
