def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        c_even = (n + 1) // 2
        c_odd = n // 2
        evens_part = pow(5, c_even, MOD)
        primes_part = pow(4, c_odd, MOD)
        return (evens_part * primes_part) % MOD