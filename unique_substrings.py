def resolve(string):
    # Will contain all the possible substrings
    substrings = set()

    # Get all the possible substrings from the main string
    for count in xrange(0, len(string)):
        for subStrLen in xrange(0, len(string) - count):
            substrings.add(string[count:count + subStrLen + 1])

    return len(substrings)

t = int(input())
while t>0:
    s = input()
    print(resolve(s))
    t -= 1
