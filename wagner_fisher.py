def wagner_fisher_old(s1, s2):
    n = len(s1)
    m = len(s2)

    # Initialize distance matrix with 0's
    dist = [[0 for j in range(m + 1)] for i in range(n + 1)]

    # Fill in the first row and column of the distance matrix
    for i in range(n + 1):
        dist[i][0] = i
    for j in range(m + 1):
        dist[0][j] = j

    # Fill in the rest of the distance matrix using the Wagner-Fisher algorithm
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min(dist[i - 1][j], dist[i][j - 1], dist[i - 1][j - 1]) + 1

    return dist[n][m]


def compute_edit_distance(dist):
    i, j = len(dist) - 1, len(dist[0]) - 1
    edit_dist = []
    for k in range(max(i, j)):
        if i > 0 and dist[i - 1][j] < dist[i][j]:
            edit_dist.append('D')
            i -= 1
        elif j > 0 and dist[i][j - 1] < dist[i][j]:
            edit_dist.append('I')
            j -= 1
        elif i > 0 and j > 0 and dist[i - 1][j - 1] < dist[i][j]:
            edit_dist.append('R')
            i -= 1
            j -= 1
        else:
            edit_dist.append('M')
            i -= 1
            j -= 1
    return edit_dist[::-1]


def wagner_fisher_full(s1, s2):
    n = len(s1)
    m = len(s2)

    # Initialize distance matrix with 0's
    dist = [[0 for j in range(m + 1)] for i in range(n + 1)]

    # Fill in the first row and column of the distance matrix
    for i in range(n + 1):
        dist[i][0] = i
    for j in range(m + 1):
        dist[0][j] = j

    # Fill in the rest of the distance matrix using the Wagner-Fisher algorithm
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min(dist[i - 1][j], dist[i][j - 1], dist[i - 1][j - 1]) + 1
    
    return compute_edit_distance(dist)

def wagner_fisher(s1, s2):
    n = len(s1)
    m = len(s2)

    # Initialize the first two rows of the distance matrix with 0's
    prev_row = [i for i in range(m + 1)]
    curr_row = [0] * (m + 1)

    # Fill in the rest of the distance matrix using the optimized Wagner-Fisher algorithm
    for i in range(1, n + 1):
        curr_row[0] = i
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr_row[j] = prev_row[j - 1]
            else:
                curr_row[j] = min(prev_row[j], curr_row[j - 1], prev_row[j - 1]) + 1
        prev_row = curr_row[:]
    
    return curr_row[m]




#print(wagner_fisher('saturday', 'sunday'))
#print(wagner_fisher('polynomial', 'exponential'))
#print(wagner_fisher_old('polynomial', 'exponential'))
#print(wagner_fisher('aaaaa', 'bb'))
#print(wagner_fisher('epolynomial', 'polynomial'))
#print(wagner_fisher('cakab','abac'))
#print(wagner_fisher_old('cakab','abac'))
print(wagner_fisher_full('connect', 'conehead'))
print(wagner_fisher_full('connect', 'cone'))