from string import ascii_lowercase

print [n ** 2 for n in range(10) if n % 2 == 0]

print [n for n in 'alamakota' if n == 'a']

print [n + 1 for n in range(100)]
print [n for n in range(100) if n % 2 == 0]


print {x: ord(x) for x in ascii_lowercase}

words = ('ala', 'kotek', 'niedzwedz', 'kot', 'samochod')
print {x: word for x, word in enumerate(words) if len(word) > 5}