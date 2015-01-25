def squares():
    x = 1
    while True:
        yield x
        yield x ** 2
        x = x + 1


sq = squares()
for x in range(3):
    import pdb; pdb.set_trace()  # put PDB here and step into functions

    print "number %s" % sq.next()
    print "square %s" % sq.next()