def boyer_moore(s, sub):
    m = len(sub)
    n = len(s)
    
    indices = []
    i = m
    while i<=n:
        i,j = hctam(i, s, sub)
        if j == 0:
            indices.append(i + 1)
        i = i + max(ro1[s[i]], ro2[j])

def hctam(i, s, sub):
    pass