# Part (a)
def target_sum(S, t):
    def backtrack(start, target):
        if target == 0:
            return []
        if target < 0:
            return None
        for i in range(start, len(S)):
            result = backtrack(i + 1, target - S[i])
            if result is not None:
                return [S[i]] + result
        return None
    result = backtrack(0, t)
    return result if result is not None else []

# Part (b)
def balanced_code(k):
    def generate(k, prefix):
        if k == 0:
            yield prefix
        else:
            for code in generate(k - 1, prefix + '0'):
                yield code
            for code in generate(k - 1, prefix + '1'):
                yield code

    all_codes = list(generate(2 * k, ''))
    balanced_codes = [code for code in all_codes if code[:k].count('0') == code[k:].count('0')]
    return balanced_codes
