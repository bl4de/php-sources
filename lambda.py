__author__ = 'admin'

fn = lambda x, y: x + y

# print fn(1, 2)


def foo(a, f, x, y):
    return f(x, y) + a


print foo(10, fn, 2, 3)

print [x ** 2 for x in range(50)]

print map(lambda x: x ** 2, range(50))