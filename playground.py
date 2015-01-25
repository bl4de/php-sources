from string import ascii_lowercase


def alfabet():
    for i in ascii_lowercase:
        print i


def codruga():
    p = True
    for i in ascii_lowercase:
        if p:
            print i
        p = not p


def codruga2():
    print ascii_lowercase[::2]


def filtr(str):
    for i in str:
        if i not in ascii_lowercase:
            print i


def palindrom(s):
    a = len(s) - 1
    for i in s:
        if i != s[a]:
            print "not palindrom!"
            return
        a -= 1
    print "palindrom!"


lista = []


def filtr(word):
    print word[1]
    n = 5
    if len(word[1]) > n:
        lista.append(word[1])


def filtruj(*args):
    filter(filtr, enumerate(args))
    print 'wyrazy dluzsze niz 5 znakow:', lista


filtruj('ala', 'kotek', 'niedzwedz', 'kot', 'samochod')

# alfabet()

# codruga()
#
# codruga2()
# filtr('abc23')
#
# palindrom('kajak')
# palindrom('kahfjfhak')
# palindrom('kajag')

