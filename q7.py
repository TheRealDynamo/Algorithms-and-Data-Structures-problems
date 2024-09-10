def find_average(L, l, r):
    return sum(L[l:r+1]) / (r - l + 1)

def rearrange(L, l, r, v):
    i, j = l, r
    while i <= j:
        if L[i] >= v:
            i += 1
        elif L[j] < v:
            j -= 1
        else:
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1
    return j

def average_quick_sort(L, l, r):
    if l < r:
        v = find_average(L, l, r)
        p = rearrange(L, l, r, v)
        average_quick_sort(L, l, p)
        average_quick_sort(L, p + 1, r)
