def kmp(s, sub):
    n = len(s)
    m = len(sub)

    # Generate the prefix table
    prefixes = [0] * m
    i = 0
    for j in range(1, m):
        while i > 0 and sub[i] != sub[j]:
            i = prefixes[i - 1]
        if sub[i] == sub[j]:
            i += 1
        prefixes[j] = i

    # Use the prefix table to search for the substring in the string
    indices = []
    i = 0
    for j in range(n):
        while i > 0 and s[j] != sub[i]:
            i = prefixes[i - 1]
        if s[j] == sub[i]:
            i += 1
        if i == m:
            indices.append(j - m + 1)
            i = prefixes[i - 1]

    return indices



s = "hello world"
sub = "o"
indices = kmp(s, sub)
print(indices) # Output: [4, 7]