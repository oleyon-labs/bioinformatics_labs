def find_substring_indices(s, sub):
    indices = []
    n = len(s)
    m = len(sub)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            indices.append(i)

    return indices


s = "hello world"
sub = "o"
indices = find_substring_indices(s, sub)
print(indices) # Output: [4, 7]