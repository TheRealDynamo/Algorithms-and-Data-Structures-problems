# Part (a)
def alpha_recursive(s):
    vowels = 'aeiou'
    if not s:
        return 0
    return (1 if s[0] in vowels else 0) + alpha_recursive(s[1:])

# Part (b)
def alpha_iterative(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Part (c)
def jacobstahl(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return jacobstahl(n-1) + 2 * jacobstahl(n-2)

# Part (d)
def jacobstahl_optimised(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = jacobstahl_optimised(n-1, memo) + 2 * jacobstahl_optimised(n-2, memo)
    return memo[n]
