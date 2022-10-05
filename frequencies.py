"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for i in range(len(items)):
        items[i] = str(items[i])

    count = 0
    for i in items:
        count = 0
        for j in items:
            temp = i
            if j == i:
                count += 1
        frequencies[i] = count
    print(count)
    print(temp)

    #frequencies[items[i]] = count
    return frequencies

print(frequencies(['a', 'b', 'a', 'b', 'b', 'c']))
print(frequencies([100, 'Hello', '100', '100', 100]))
