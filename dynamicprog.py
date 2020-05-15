def memoise(f): # decorator for memoisation
    memo = {}
    def _f(*args):
        if not args in memo:
            memo[args] = f(*args)
        return memo[args]
    return _f
