from helper import is_not_equal

def find_substring_indices(s, sub):
    indices = []
    n = len(s)
    m = len(sub)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if is_not_equal(s[i + j], sub[j]): #s[i + j] != sub[j]:
                match = False
                break
        if match:
            indices.append(i)
    return indices




s = "abaaababab"
sub = "abab"
is_not_equal.count = 0
indices = find_substring_indices(s, sub)
print(f"Function has been called {is_not_equal.count} times.")
print(indices) # Output: [4, 7, 11]