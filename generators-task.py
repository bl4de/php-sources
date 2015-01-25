import datetime
# @TODO dokonczyc !!!

def dejs():
    x = 24 * 60 * 60
    while True:
        yield datetime.datetime.now().strftime("%A")


d = dejs()

print d.next()
print d.next()