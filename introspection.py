# print dir(a)
# print help(a.update)

# print [x for x in dir(a) if callable(x)]

# print callable(a)
#
# print getattr(a, '__doc__')
# print getattr(a, 'viewkeys')


def atrybuty(obj):
    for atr in dir(obj):
        # print atr
        if callable(getattr(obj, atr)):
            print atr
            print dir(atr)


atrybuty('aaa')

# print callable(''.format)