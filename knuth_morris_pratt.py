from helper import is_not_equal

def kmp_old(s, sub):
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
        while i > 0 and is_not_equal(s[j], sub[i]):#s[j] != sub[i]:
            i = prefixes[i - 1]
        if not is_not_equal(s[j], sub[i]):#s[j] == sub[i]:
            i += 1
        if i == m:
            indices.append(j - m + 1)
            i = prefixes[i - 1]

    return indices


def kmp(s, sub):
    n = len(s)
    m = len(sub)

    prefixes = find_prefixes(sub)
    indices = []
    i = 0
    j = 0
    while i <= n - m + j:
        while j < m and not is_not_equal(s[i], sub[j]): j += 1; i += 1
        if j == m: indices.append(i - m)
        if j == 0: i += 1
        else: j = prefixes[j - 1]
    return indices

def find_prefixes(s):
    m = len(s)
    prefixes = [0] * m
    i = 0
    for j in range(1, m):
        while i > 0 and s[i] != s[j]:
            i = prefixes[i - 1]
        if s[i] == s[j]:
            i += 1
        prefixes[j] = i
    return prefixes










s = "hello world"
sub = "o"
s1 = "abaabcabaabaaba"
sub1 = "abaaba"
#indices = kmp(s, sub)
#print(indices) # Output: [4, 7]

is_not_equal.count = 0
indices2 = kmp(s1, sub1)
print(indices2)
print(f"Function has been called {is_not_equal.count} times.")