class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        
        def fib_memo(n):
            if n in memo:
                return memo[n]
            memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
            return memo[n]
        
        return fib_memo(n)
